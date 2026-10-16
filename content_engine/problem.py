"""Typed orchestration for supported deterministic physics problem models."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import math
from pathlib import Path
import re
import sqlite3
from datetime import datetime, timezone
from typing import Any
import uuid

from exam_engine.engine import DataValidationError
from math_engine import MathDomainError
from physics_engine import constant_acceleration

SUPPORTED_MODELS = {"constant-acceleration"}


@dataclass(frozen=True)
class ProblemResult:
    problem_id: str
    model_type: str
    position_m: tuple[float, ...]
    velocity_m_per_s: tuple[float, ...]
    independent_position_m: tuple[float, ...]
    checks: tuple[dict[str, Any], ...]
    computation_status: str
    physics_review_status: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_problem(path: Path) -> dict[str, Any]:
    try:
        problem = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DataValidationError(f"cannot read problem JSON {path}: {exc}") from exc
    if not isinstance(problem, dict):
        raise DataValidationError("problem JSON must contain a single object")
    return problem


def solve_problem(problem: dict[str, Any]) -> ProblemResult:
    required = {
        "problem_id", "source_id", "concept_id", "model_type", "inputs",
        "assumptions", "unit_system",
    }
    missing = sorted(required - problem.keys())
    if missing:
        raise DataValidationError(
            "problem is missing required fields: " + ", ".join(missing)
        )
    if not isinstance(problem["model_type"], str) or problem["model_type"] not in SUPPORTED_MODELS:
        raise DataValidationError(
            f"unsupported model_type {problem['model_type']!r}; supported: "
            + ", ".join(sorted(SUPPORTED_MODELS))
        )
    if not isinstance(problem["problem_id"], str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._-]*", problem["problem_id"]
    ):
        raise DataValidationError("problem_id must contain only letters, digits, dots, '_' or '-'")
    if not isinstance(problem["source_id"], str) or not problem["source_id"]:
        raise DataValidationError("source_id must be a non-empty string")
    if not isinstance(problem["concept_id"], str) or not problem["concept_id"]:
        raise DataValidationError("concept_id must be a non-empty string")
    if problem["unit_system"] != "SI":
        raise DataValidationError("constant-acceleration model currently requires SI units")
    if (
        not isinstance(problem["assumptions"], list)
        or not problem["assumptions"]
        or any(not isinstance(value, str) or not value.strip()
               for value in problem["assumptions"])
    ):
        raise DataValidationError("problem assumptions must be a list of non-empty strings")
    inputs = problem["inputs"]
    if not isinstance(inputs, dict):
        raise DataValidationError("problem inputs must be an object")
    input_names = (
        "initial_position_m", "initial_velocity_m_per_s",
        "acceleration_m_per_s2", "time_s",
    )
    if set(inputs) != set(input_names):
        raise DataValidationError(
            "constant-acceleration inputs must contain exactly: "
            + ", ".join(input_names)
        )

    try:
        position, velocity = constant_acceleration(
            inputs["initial_position_m"],
            inputs["initial_velocity_m_per_s"],
            inputs["acceleration_m_per_s2"],
            inputs["time_s"],
        )
        time = float(inputs["time_s"])
        initial_velocity = tuple(float(value) for value in inputs["initial_velocity_m_per_s"])
        acceleration = tuple(float(value) for value in inputs["acceleration_m_per_s2"])
        initial_position = tuple(float(value) for value in inputs["initial_position_m"])
        independent_position = tuple(
            initial_position[index]
            + 0.5 * (initial_velocity[index] + velocity[index]) * time
            for index in range(len(position))
        )
    except (KeyError, TypeError, ValueError, OverflowError, MathDomainError) as exc:
        raise DataValidationError(f"cannot solve constant-acceleration model: {exc}") from exc
    if not all(math.isfinite(value) for value in independent_position):
        raise DataValidationError("independent displacement check produced a non-finite value")

    scale = max(1.0, *(abs(value) for value in (*position, *independent_position)))
    tolerance = max(1e-12, 1e-10 * scale)
    identity_differences = tuple(
        abs(actual - independent)
        for actual, independent in zip(position, independent_position)
    )
    identity_residual = max(identity_differences)
    checks: list[dict[str, Any]] = [
        {
            "check_id": "independent-displacement-identity",
            "description": "Compare s = ut + 1/2 at^2 with s = (u + v)t/2",
            "passed": all(value <= tolerance for value in identity_differences),
            "residual_inf_norm": (
                identity_residual if math.isfinite(identity_residual) else None
            ),
        },
        {
            "check_id": "velocity-equation",
            "description": "Check v = u + at",
            "passed": all(
                abs(actual - (initial_velocity[index] + acceleration[index] * time))
                <= tolerance
                for index, actual in enumerate(velocity)
            ),
        },
    ]
    expected = problem.get("expected_outputs")
    if expected is not None:
        if not isinstance(expected, dict):
            raise DataValidationError("expected_outputs must be an object when provided")
        unexpected_fields = set(expected) - {"position_m", "velocity_m_per_s"}
        if unexpected_fields:
            raise DataValidationError(
                "unsupported expected_outputs fields: "
                + ", ".join(sorted(map(str, unexpected_fields)))
            )
        for field, actual in (
            ("position_m", position),
            ("velocity_m_per_s", velocity),
        ):
            if field not in expected:
                continue
            try:
                if any(isinstance(value, bool) for value in expected[field]):
                    raise ValueError
                expected_values = tuple(float(value) for value in expected[field])
            except (TypeError, ValueError, OverflowError) as exc:
                raise DataValidationError(f"expected_outputs.{field} must be numeric") from exc
            if len(expected_values) != len(actual) or not all(
                math.isfinite(value) for value in expected_values
            ):
                raise DataValidationError(
                    f"expected_outputs.{field} has invalid dimensions or non-finite values"
                )
            differences = tuple(
                abs(value - expected_value)
                for value, expected_value in zip(actual, expected_values)
            )
            residual = max(differences)
            checks.append({
                "check_id": f"expected-{field}",
                "description": f"Compare computed output with supplied expected {field}",
                "passed": all(math.isclose(
                    value, expected_value, rel_tol=1e-10, abs_tol=1e-12
                ) for value, expected_value in zip(actual, expected_values)),
                "residual_inf_norm": residual if math.isfinite(residual) else None,
            })

    return ProblemResult(
        problem_id=str(problem["problem_id"]),
        model_type=str(problem["model_type"]),
        position_m=position,
        velocity_m_per_s=velocity,
        independent_position_m=independent_position,
        checks=tuple(checks),
        computation_status=(
            "passed" if all(check["passed"] for check in checks) else "failed"
        ),
        physics_review_status="pending-human-review",
    )


def record_problem_run(
    connection: sqlite3.Connection,
    problem: dict[str, Any],
    result: ProblemResult,
) -> str:
    """Persist reproducible inputs and outputs without granting physics approval."""
    source = connection.execute(
        "SELECT source_id FROM sources WHERE source_id = ?", (problem["source_id"],)
    ).fetchone()
    concept = connection.execute(
        "SELECT concept_id, domain, topic_id FROM concepts WHERE concept_id = ?",
        (problem["concept_id"],),
    ).fetchone()
    if source is None:
        raise DataValidationError(f"unknown source_id {problem['source_id']!r}")
    if concept is None:
        raise DataValidationError(f"unknown concept_id {problem['concept_id']!r}")
    if concept["domain"] != "physics":
        raise DataValidationError("calculation models must link to a physics concept")
    question_id = problem.get("question_id") or None
    if question_id:
        question = connection.execute(
            "SELECT source_id, topic_id FROM questions WHERE question_id = ?",
            (question_id,),
        ).fetchone()
        if question is None:
            raise DataValidationError(f"unknown question_id {question_id!r}")
        if question["source_id"] != problem["source_id"]:
            raise DataValidationError("problem source_id must match its linked question")
        if question["topic_id"] != concept["topic_id"]:
            raise DataValidationError("problem physics concept must match its linked question topic")
    inputs_json = json.dumps(problem["inputs"], sort_keys=True)
    assumptions_json = json.dumps(problem["assumptions"], sort_keys=True)
    input_hash = hashlib.sha256(inputs_json.encode("utf-8")).hexdigest()
    connection.execute(
        """INSERT INTO problem_models
           (problem_id, question_id, source_id, concept_id, model_type,
            inputs_json, expected_outputs_json, assumptions_json, unit_system, review_status)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(problem_id) DO UPDATE SET
             question_id=excluded.question_id, source_id=excluded.source_id,
             concept_id=excluded.concept_id, model_type=excluded.model_type,
             inputs_json=excluded.inputs_json,
             expected_outputs_json=excluded.expected_outputs_json,
             assumptions_json=excluded.assumptions_json,
             unit_system=excluded.unit_system, review_status=excluded.review_status""",
        (
            result.problem_id, question_id, problem["source_id"], problem["concept_id"],
            result.model_type, inputs_json,
            json.dumps(problem["expected_outputs"], sort_keys=True)
            if problem.get("expected_outputs") is not None else None,
            assumptions_json, problem["unit_system"], "draft",
        ),
    )
    run_id = str(uuid.uuid4())
    connection.execute(
        """INSERT INTO engine_runs
           (run_id, problem_id, engine_name, engine_version, input_hash,
            result_json, check_status, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            run_id, result.problem_id, "content_engine", "1",
            input_hash, json.dumps(result.to_dict(), sort_keys=True),
            "passed" if result.computation_status == "passed" else "failed",
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    return run_id
