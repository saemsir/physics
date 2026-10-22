#!/usr/bin/env python3
"""Saem Sentinel: centralised online learner for repository health.

Memory lives in data/repo_learner_state.json so it travels with the repo
(centralised across CI runners, Codespaces, phones). Learning signals:
per-rule success rates (Laplace-smoothed) and recency-weighted path risk
(same half-life math as exam_engine).
"""
from __future__ import annotations

import argparse
import json
import math
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "data" / "repo_learner_state.json"
HALF_LIFE_DAYS = 14.0


def load_state() -> dict:
    if STATE.is_file():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass
    return {"schema_version": 1, "rules": {}, "path_events": {}, "history": []}


def save_state(st: dict) -> None:
    st["history"] = st["history"][-50:]
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, indent=2, sort_keys=True) + "\n", encoding="utf-8")


# ---------------- prediction: recency-weighted failure risk ----------------
def path_risk(st: dict, now: float) -> dict[str, float]:
    k = math.log(2) / HALF_LIFE_DAYS
    risks = {}
    for path, events in st.get("path_events", {}).items():
        w_sum = f_sum = 0.0
        for ev in events[-40:]:
            w = math.exp(-k * max(0.0, (now - ev["ts"]) / 86400.0))
            w_sum += w
            f_sum += w * (1.0 if ev.get("failed") else 0.0)
        risks[path] = (1.0 + f_sum) / (2.0 + w_sum)
    return risks


# ---------------- correction rules: deterministic + idempotent ----------------
def _fix_batch_fields(root: Path) -> list[str]:
    changed = []
    for p in sorted((root / "data" / "video_batches").glob("batch_*.json")):
        try:
            b = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(b, dict):
            continue
        d = dict(b)
        d.setdefault("status", "draft-owner-review")
        d.setdefault("brand", {"name": "Saem Physics", "tagline": "NEET JEE MIT"})
        d.setdefault("audience", {"minimum_age": 14, "maximum_age": 21})
        for ep in d.get("episodes") or []:
            if not isinstance(ep, dict):
                continue
            ep.setdefault("solution_review_status", "pending-owner-review")
            if not isinstance(ep.get("reference"), dict):
                ep["reference"] = {
                    "title": "SaemPhysics source ledger",
                    "section": "pending-owner-review",
                    "local_path": "data/README.md",
                }
        if d != b:
            p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            changed.append(str(p.relative_to(root)))
    return changed


def _fix_gemini_model(root: Path) -> list[str]:
    p = root / "scripts" / "gemini_generate_request.py"
    if not p.is_file():
        return []
    t = p.read_text(encoding="utf-8")
    new = re.sub(r'model\s*=\s*["\']gemini-[^"\']*["\']', 'model="gemini-1.5-flash"', t)
    if new != t:
        p.write_text(new, encoding="utf-8")
        return [str(p.relative_to(root))]
    return []


def _fix_torch_weights(root: Path) -> list[str]:
    p = root / "tools" / "local_narration.py"
    if not p.is_file():
        return []
    t = p.read_text(encoding="utf-8")
    if "_saem_load_patched" in t:
        return []
    patch = (
        "\ndef _patch_torch_load():\n"
        "    import torch\n"
        '    if getattr(torch, "_saem_load_patched", False):\n        return\n'
        "    _o = torch.load\n"
        "    def _l(*a, **k):\n"
        '        k.setdefault("weights_only", False)\n'
        "        return _o(*a, **k)\n"
        "    torch.load = _l\n"
        '    torch._saem_load_patched = True\n\n'
    )
    t = t.replace("def synthesize_local_wav", patch + "def synthesize_local_wav", 1)
    t = t.replace("    from TTS.api import TTS", "    _patch_torch_load()\n    from TTS.api import TTS", 1)
    p.write_text(t, encoding="utf-8")
    return [str(p.relative_to(root))]


def _fix_missing_dep(root: Path, m: re.Match) -> list[str]:
    mod = m.group(1)
    dist = {"cv2": "opencv-python-headless", "PIL": "pillow", "sklearn": "scikit-learn"}.get(mod, mod)
    p = root / "requirements.txt"
    lines = p.read_text(encoding="utf-8").splitlines() if p.is_file() else []
    if any(l.strip().split(">=")[0].split("==")[0].strip() == dist for l in lines if l.strip()):
        return []
    p.write_text("\n".join(lines + [dist]) + "\n", encoding="utf-8")
    return [str(p.relative_to(root))]


RULES = [
    {"id": "batch_schema", "match": r"reference must be an object|must be a non-empty string|solution_review_status", "fix": lambda r, m: _fix_batch_fields(r)},
    {"id": "gemini_model", "match": r"404 NOT_FOUND", "fix": lambda r, m: _fix_gemini_model(r)},
    {"id": "torch_weights_only", "match": r"Weights only load failed|WeightsUnpickler", "fix": lambda r, m: _fix_torch_weights(r)},
    {"id": "missing_dep", "match": r"ModuleNotFoundError: No module named ['\"]([A-Za-z0-9_]+)", "fix": _fix_missing_dep},
]


def rule_score(st: dict, rid: str) -> float:
    r = st["rules"].get(rid, {"applied": 0, "fixed": 0})
    return (r["fixed"] + 1) / (r["applied"] + 2)


# ---------------- commands ----------------
def cmd_ingest(a) -> int:
    st = load_state()
    now = int(a.ts or time.time())
    err = ""
    if a.error_file and Path(a.error_file).is_file():
        err = Path(a.error_file).read_text(encoding="utf-8", errors="replace")[-2000:]
    evs = st["path_events"].setdefault(a.path, [])
    evs.append({"ts": now, "failed": bool(a.failed), "check": a.check})
    st["path_events"][a.path] = evs[-40:]
    save_state(st)
    print(json.dumps({"ingested": a.path, "failed": bool(a.failed), "error_chars": len(err)}))
    return 0


def cmd_predict(a) -> int:
    st = load_state()
    risks = sorted(path_risk(st, time.time()).items(), key=lambda kv: -kv[1])
    for path, risk in risks[: a.top]:
        print(f"risk {risk:.3f}  {path}")
    return 0


def cmd_correct(a) -> int:
    st = load_state()
    text = Path(a.error_file).read_text(encoding="utf-8", errors="replace") if a.error_file else ""
    matched = []
    for rule in RULES:
        m = re.search(rule["match"], text)
        if m:
            matched.append((rule, m))
    if not matched:
        print(json.dumps({"rule": "", "files": []}))
        return 0
    matched.sort(key=lambda rm: -rule_score(st, rm[0]["id"]))
    rule, m = matched[0]
    files = rule["fix"](ROOT, m)
    st["rules"].setdefault(rule["id"], {"applied": 0, "fixed": 0})
    st["rules"][rule["id"]]["applied"] += 1
    st["rules"][rule["id"]]["last_used"] = int(time.time())
    save_state(st)
    print(json.dumps({"rule": rule["id"], "files": files}))
    return 0


def cmd_outcome(a) -> int:
    st = load_state()
    r = st["rules"].setdefault(a.rule, {"applied": 0, "fixed": 0})
    if a.passed:
        r["fixed"] += 1
    st["history"].append({"ts": int(time.time()), "rule": a.rule, "passed": bool(a.passed)})
    save_state(st)
    print(json.dumps({"rule": a.rule, "score": rule_score(st, a.rule)}))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("ingest")
    i.add_argument("--path", required=True)
    i.add_argument("--check", required=True)
    i.add_argument("--failed", type=int, required=True)
    i.add_argument("--error-file")
    i.add_argument("--ts", type=int)
    pr = sub.add_parser("predict")
    pr.add_argument("--top", type=int, default=5)
    c = sub.add_parser("correct")
    c.add_argument("--error-file", required=True)
    o = sub.add_parser("outcome")
    o.add_argument("--rule", required=True)
    o.add_argument("--passed", type=int, required=True)
    a = p.parse_args()
    return {"ingest": cmd_ingest, "predict": cmd_predict, "correct": cmd_correct, "outcome": cmd_outcome}[a.cmd](a)


if __name__ == "__main__":
    raise SystemExit(main())
