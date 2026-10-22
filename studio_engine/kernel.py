#!/usr/bin/env python3
"""
SaemPhysics Kernel: The Cognitive OS Layer

Routes all studio requests through attention-based classification, dispatches
to the appropriate engine, and manages three-tier memory:
  - Working memory (run-scoped ephemeral state)
  - Episodic memory (cross-run learning state in repo_learner_state.json)
  - Semantic memory (persistent knowledge graph in content.db)

Based on principles from "Cognitive OS -1" and Feynman's information integrity.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# ===== Memory Tiers =====

class WorkingMemory:
    """Run-scoped ephemeral state. Lives in RUNNER_TEMP or /tmp."""
    
    def __init__(self):
        self.store = {}
        self.temp_dir = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir()))
        self.run_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:12]
        
    def set(self, key: str, value: Any) -> None:
        self.store[key] = value
        
    def get(self, key: str, default: Any = None) -> Any:
        return self.store.get(key, default)
    
    def persist_artifact(self, name: str, data: bytes) -> Path:
        """Content-addressed storage in working memory."""
        sha = hashlib.sha256(data).hexdigest()
        dest = self.temp_dir / "saem_working" / self.run_id / f"{name}_{sha[:16]}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return dest
    
    def clear(self) -> None:
        self.store.clear()


class EpisodicMemory:
    """Cross-run learning state. Persists in data/repo_learner_state.json."""
    
    STATE_FILE = ROOT / "data" / "repo_learner_state.json"
    
    def __init__(self):
        self.state = self._load()
    
    def _load(self) -> dict:
        if self.STATE_FILE.is_file():
            try:
                return json.loads(self.STATE_FILE.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                pass
        return {
            "schema_version": 1,
            "engine": "saem-episodic-memory",
            "path_risks": {},
            "rule_success": {},
            "history": []
        }
    
    def save(self) -> None:
        self.STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.STATE_FILE.write_text(
            json.dumps(self.state, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8"
        )
    
    def record_event(self, path: str, check: str, failed: bool, error_text: str = "") -> None:
        """Record a check outcome for recency-weighted risk scoring."""
        events = self.state["path_risks"].setdefault(path, [])
        events.append({
            "ts": int(time.time()),
            "check": check,
            "failed": failed,
            "error_preview": error_text[:500] if error_text else ""
        })
        self.state["path_risks"][path] = events[-50:]  # cap at 50 events
        self.save()
    
    def record_rule_outcome(self, rule_id: str, passed: bool) -> None:
        """Record whether a self-correction rule actually fixed the problem."""
        rule = self.state["rule_success"].setdefault(rule_id, {"applied": 0, "fixed": 0})
        rule["applied"] += 1
        if passed:
            rule["fixed"] += 1
        self.save()
    
    def predict_risk(self, top_n: int = 5) -> list[tuple[str, float]]:
        """Return paths sorted by recency-weighted failure probability."""
        import math
        now = time.time()
        half_life_days = 14.0
        k = math.log(2) / half_life_days
        
        risks = []
        for path, events in self.state["path_risks"].items():
            w_sum = f_sum = 0.0
            for ev in events:
                dt_days = (now - ev["ts"]) / 86400.0
                w = math.exp(-k * max(0.0, dt_days))
                w_sum += w
                f_sum += w * (1.0 if ev["failed"] else 0.0)
            if w_sum > 0:
                risks.append((path, f_sum / w_sum))
        
        return sorted(risks, key=lambda x: -x[1])[:top_n]
    
    def get_best_rule(self, candidates: list[str]) -> str:
        """Return the rule with highest Laplace-smoothed success rate."""
        best_rule, best_score = "", -1.0
        for rule_id in candidates:
            rule = self.state["rule_success"].get(rule_id, {"applied": 0, "fixed": 0})
            score = (rule["fixed"] + 1) / (rule["applied"] + 2)
            if score > best_score:
                best_score = score
                best_rule = rule_id
        return best_rule


class SemanticMemory:
    """Persistent knowledge graph. Lives in saemphysics.sqlite."""
    
    DB_FILE = ROOT / "saemphysics.sqlite"
    
    def __init__(self):
        self.db_path = self.DB_FILE
        if not self.db_path.is_file():
            print(f"[kernel] warning: {self.db_path} not found; run 'content_engine init' first")
    
    def query(self, sql: str, params: tuple = ()) -> list[dict]:
        """Execute a read-only query and return rows as dicts."""
        if not self.db_path.is_file():
            return []
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute(sql, params).fetchall()
                return [dict(r) for r in rows]
        except sqlite3.Error as exc:
            print(f"[kernel] semantic memory query failed: {exc}", file=sys.stderr)
            return []
    
    def concept_graph(self, topic_id: str) -> dict:
        """Return concept + prerequisites + dependents for a topic."""
        rows = self.query("""
            SELECT c.concept_id, c.concept_name, cl.relation, cl.target_id
            FROM concepts c
            LEFT JOIN concept_links cl ON cl.source_id = c.concept_id
            WHERE c.topic_id = ?
            UNION
            SELECT c.concept_id, c.concept_name, cl.relation, cl.target_id
            FROM concepts c
            JOIN concept_links cl ON cl.target_id = c.concept_id
            JOIN concepts c2 ON c2.concept_id = cl.source_id
            WHERE c2.topic_id = ?
        """, (topic_id, topic_id))
        
        graph = {"nodes": set(), "edges": []}
        for r in rows:
            graph["nodes"].add(r["concept_id"])
            if r["target_id"]:
                graph["edges"].append((r["concept_id"], r["target_id"], r["relation"]))
        graph["nodes"] = list(graph["nodes"])
        return graph


# ===== Attention Router =====

class AttentionRouter:
    """Classify requests using concept-graph attention and prefix routing."""
    
    ROUTES = [
        ("physics", "physics_engine"),
        ("math", "math_engine"),
        ("exam", "exam_engine"),
        ("content", "content_engine"),
        ("matrix", "matrix_pipeline"),
        ("video", "video_learning"),
    ]
    
    def __init__(self, semantic: SemanticMemory):
        self.semantic = semantic
    
    def route(self, request_text: str) -> str:
        """Return the engine module name most likely to handle this request."""
        text_lower = request_text.lower()
        
        # Try keyword match first (fast path)
        for prefix, engine in self.ROUTES:
            if prefix in text_lower:
                return engine
        
        # Fall back to concept-graph attention
        concepts = self._extract_concepts(text_lower)
        if concepts:
            graph = self.semantic.concept_graph(concepts[0])
            if graph["nodes"]:
                # If concept exists in semantic memory, route to content_engine
                return "content_engine"
        
        return "content_engine"  # default scheduler
    
    def _extract_concepts(self, text: str) -> list[str]:
        """Extract physics concept IDs from free text."""
        # Simple pattern: physics:kinematics, math:vectors, etc.
        matches = re.findall(r'(physics|math):([a-z0-9_]+)', text)
        return [f"{domain}:{topic}" for domain, topic in matches]


# ===== Kernel Entry Point =====

class Kernel:
    """The Cognitive OS kernel: routes, dispatches, remembers."""
    
    def __init__(self):
        self.working = WorkingMemory()
        self.episodic = EpisodicMemory()
        self.semantic = SemanticMemory()
        self.router = AttentionRouter(self.semantic)
    
    def dispatch(self, request: dict) -> dict:
        """Main entry: classify -> route -> execute -> remember."""
        request_text = json.dumps(request, ensure_ascii=False)
        engine = self.router.route(request_text)
        
        print(f"[kernel] routing '{request_text[:80]}...' -> {engine}")
        
        # Execute via subprocess (isolation + error capture)
        import subprocess
        try:
            result = subprocess.run(
                [sys.executable, "-m", engine, "run", "--request", "-"],
                input=request_text,
                capture_output=True,
                text=True,
                timeout=300,
                cwd=ROOT
            )
            success = result.returncode == 0
            self.episodic.record_event(
                path=engine,
                check="dispatch",
                failed=not success,
                error_text=result.stderr
            )
            return {
                "status": "success" if success else "failed",
                "engine": engine,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired:
            self.episodic.record_event(engine, "dispatch", True, "timeout after 300s")
            return {"status": "timeout", "engine": engine}
        except Exception as exc:
            self.episodic.record_event(engine, "dispatch", True, str(exc))
            return {"status": "error", "engine": engine, "error": str(exc)}
    
    def predict_next_failures(self, top_n: int = 5) -> list[tuple[str, float]]:
        """Predict which paths are most likely to fail next."""
        return self.episodic.predict_risk(top_n)


def main():
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--request", type=Path, help="JSON request file (or '-' for stdin)")
    p.add_argument("--predict", action="store_true", help="Predict next failures and exit")
    args = p.parse_args()
    
    kernel = Kernel()
    
    if args.predict:
        risks = kernel.predict_next_failures(10)
        print("Predicted risk (recency-weighted):")
        for path, risk in risks:
            print(f"  {risk:.3f}  {path}")
        return 0
    
    if args.request:
        if str(args.request) == "-":
            request = json.load(sys.stdin)
        else:
            request = json.loads(args.request.read_text(encoding="utf-8"))
        result = kernel.dispatch(request)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["status"] == "success" else 1
    
    p.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
