"""Compile checked model output and concept links into a renderer-neutral lesson IR."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sqlite3

from animation_engine import motion_scene_spec
from exam_engine.engine import DataValidationError

LESSON_IR_VERSION = 1


def compile_lesson(
    connection: sqlite3.Connection,
    problem: dict,
    result: dict,
) -> dict:
    if result.get("computation_status") != "passed":
        raise DataValidationError("cannot compile a lesson from failed computational checks")
    topic = connection.execute(
        "SELECT * FROM concepts WHERE concept_id = ?", (problem["concept_id"],)
    ).fetchone()
    if topic is None:
        raise DataValidationError(f"unknown concept_id {problem['concept_id']!r}")
    if topic["domain"] != "physics":
        raise DataValidationError("lesson problem concept must be a physics concept")
    related = connection.execute(
        """SELECT c.concept_id, c.concept_name, c.domain, l.relation
           FROM concept_links l JOIN concepts c ON c.concept_id = l.target_id
           WHERE l.source_id = ? ORDER BY l.relation, c.concept_id""",
        (topic["concept_id"],),
    ).fetchall()
    source = connection.execute(
        """SELECT source_id, title, citation, source_url, local_path,
                  rights_status, rights_reference
           FROM sources WHERE source_id = ?""",
        (problem["source_id"],),
    ).fetchone()
    if source is None:
        raise DataValidationError(f"unknown source_id {problem['source_id']!r}")
    concept_ids = [topic["concept_id"], *(row["concept_id"] for row in related)]
    placeholders = ", ".join("?" for _ in concept_ids)
    references = connection.execute(
        f"""SELECT cs.concept_id, c.concept_name, cs.source_id, s.title,
                   s.citation, s.source_url, s.local_path, s.rights_status,
                   s.rights_reference, cs.source_locator, cs.relation,
                   cs.review_status
            FROM concept_sources cs
            JOIN concepts c ON c.concept_id = cs.concept_id
            JOIN sources s ON s.source_id = cs.source_id
            WHERE cs.concept_id IN ({placeholders})
            ORDER BY cs.concept_id, cs.source_id, cs.source_locator""",
        concept_ids,
    ).fetchall()

    assumptions = problem["assumptions"]
    inputs = problem["inputs"]
    duration = problem.get("duration_seconds", 45)
    if isinstance(duration, bool) or not isinstance(duration, int) or duration <= 0:
        raise DataValidationError("duration_seconds must be a positive integer")
    lesson_id = problem.get("lesson_id", f"lesson-{problem['problem_id']}")
    if not isinstance(lesson_id, str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._-]*", lesson_id
    ):
        raise DataValidationError("lesson_id must contain only letters, digits, dots, '_' or '-'")
    text_fields = (
        "title", "audience", "language", "central_question",
        "learning_outcome", "solution_narration", "source_locator",
    )
    for field in text_fields:
        value = problem.get(field)
        if value is not None and not isinstance(value, str):
            raise DataValidationError(f"{field} must be a string")
    try:
        trajectory = motion_scene_spec(
            inputs["initial_position_m"],
            inputs["initial_velocity_m_per_s"],
            inputs["acceleration_m_per_s2"],
            inputs["time_s"],
        ).to_dict()
    except (KeyError, TypeError, ValueError) as exc:
        raise DataValidationError(f"cannot build motion visual specification: {exc}") from exc
    scenes = [
        {
            "scene_id": "motion-question",
            "sequence": 1,
            "scene_type": "question-hook",
            "purpose": "State the motion question and identify the given quantities.",
            "visual_spec": {
                "model_type": problem["model_type"],
                "initial_position_m": inputs["initial_position_m"],
                "initial_velocity_m_per_s": inputs["initial_velocity_m_per_s"],
                "acceleration_m_per_s2": inputs["acceleration_m_per_s2"],
                "time_s": inputs["time_s"],
            },
            "narration": problem.get("central_question", ""),
            "approval_status": "draft",
        },
        {
            "scene_id": "motion-solution",
            "sequence": 2,
            "scene_type": "calculation-backed-motion",
            "purpose": "Show the predicted motion and compare two displacement calculations.",
            "visual_spec": {
                "position_m": result["position_m"],
                "velocity_m_per_s": result["velocity_m_per_s"],
                "independent_position_m": result["independent_position_m"],
                "checks": result["checks"],
                "trajectory": trajectory,
            },
            "narration": problem.get("solution_narration", ""),
            "approval_status": "draft",
        },
    ]
    return {
        "ir_version": LESSON_IR_VERSION,
        "lesson_id": lesson_id,
        "problem_id": problem["problem_id"],
        "question_id": problem.get("question_id"),
        "title": problem.get("title", topic["concept_name"]),
        "audience": problem.get("audience", "JEE / physics learners"),
        "language": problem.get("language", "en"),
        "duration_seconds": duration,
        "central_question": problem.get("central_question", ""),
        "learning_outcome": problem.get("learning_outcome", ""),
        "concepts": [
            {
                "concept_id": topic["concept_id"],
                "concept_name": topic["concept_name"],
                "role": "teaches",
            },
            *[
                {
                    "concept_id": row["concept_id"],
                    "concept_name": row["concept_name"],
                    "role": "uses_math" if row["relation"] == "uses_math" else "prerequisite",
                }
                for row in related
            ],
        ],
        "claims": [
            {
                "claim_id": "model-output",
                "statement": (
                    "For the stated constant-acceleration model, the computed position "
                    "and velocity follow from the supplied SI inputs."
                ),
                "source_id": source["source_id"],
                "source_citation": source["citation"],
                "source_url": source["source_url"] or None,
                "source_local_path": source["local_path"] or None,
                "source_locator": problem.get("source_locator", ""),
                "rights_status": source["rights_status"],
                "verification_status": result["computation_status"],
                "physics_review_status": "pending-human-review",
            }
        ],
        "concept_references": [
            {
                "concept_id": row["concept_id"],
                "concept_name": row["concept_name"],
                "source_id": row["source_id"],
                "title": row["title"],
                "citation": row["citation"],
                "source_url": row["source_url"] or None,
                "source_local_path": row["local_path"] or None,
                "rights_status": row["rights_status"],
                "rights_reference": row["rights_reference"],
                "source_locator": row["source_locator"],
                "relation": row["relation"],
                "review_status": row["review_status"],
            }
            for row in references
        ],
        "assumptions": assumptions,
        "calculation": result,
        "scenes": scenes,
        "approvals": {
            "editorial": "draft",
            "physics": "pending",
            "design": "pending",
            "render": "pending",
            "release": "pending",
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


def persist_lesson(
    connection: sqlite3.Connection,
    ir: dict,
) -> None:
    encoded = json.dumps(ir, sort_keys=True)
    connection.execute(
        """INSERT INTO lessons
           (lesson_id, question_id, problem_id, title, audience, language,
            duration_seconds, ir_version, ir_json, editorial_status, physics_status,
            design_status, release_status, render_status, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft', 'pending', 'pending',
                   'pending', 'pending', ?)
           ON CONFLICT(lesson_id) DO UPDATE SET
             question_id=excluded.question_id, problem_id=excluded.problem_id,
             title=excluded.title, audience=excluded.audience, language=excluded.language,
             duration_seconds=excluded.duration_seconds, ir_version=excluded.ir_version,
             ir_json=excluded.ir_json, editorial_status='draft',
             physics_status='pending', design_status='pending',
             release_status='pending', render_status='pending',
             created_at=excluded.created_at""",
        (
            ir["lesson_id"], ir.get("question_id"), ir["problem_id"], ir["title"],
            ir["audience"], ir["language"], ir["duration_seconds"], ir["ir_version"],
            encoded, ir["created_at"],
        ),
    )
    connection.execute("DELETE FROM lesson_concepts WHERE lesson_id = ?", (ir["lesson_id"],))
    connection.execute("DELETE FROM lesson_scenes WHERE lesson_id = ?", (ir["lesson_id"],))
    for concept in ir["concepts"]:
        connection.execute(
            "INSERT INTO lesson_concepts VALUES (?, ?, ?)",
            (ir["lesson_id"], concept["concept_id"], concept["role"]),
        )
    for scene in ir["scenes"]:
        connection.execute(
            """INSERT INTO lesson_scenes VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                ir["lesson_id"], scene["scene_id"], scene["sequence"],
                scene["scene_type"], scene["purpose"],
                json.dumps(scene["visual_spec"], sort_keys=True), scene["narration"],
                scene["approval_status"],
            ),
        )


def write_lesson(ir: dict, path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ir, indent=2, sort_keys=True) + "\n", encoding="utf-8")
