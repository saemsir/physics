"""Validate, coordinate, and record repeatable multi-engine studio runs."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import date, datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from typing import Any
import uuid

ROOT = Path(__file__).resolve().parents[1]
MAX_TASKS = 50
RUN_SCHEMA_VERSION = 1
TASK_ID = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._-]{0,63}$")
SUPPORTED_ACTIONS = {
    "content.initialize",
    "content.summary",
    "content.solve",
    "content.compile_lesson",
    "math.solve_linear",
    "physics.constant_acceleration",
    "exam.recommend",
    "exam.backtest",
    "exam.forecast",
    "exam.import_candidates",
    "matrix.build",
    "audio.analyze_reference",
    "production.index_references",
    "production.record_review",
    "video.request",
    "video.lesson_plan",
    "video.batch_plan",
    "video.render_batch",
}
ACTION_PARAMETERS = {
    "content.initialize": {"database"},
    "content.summary": {"database"},
    "content.solve": {"problem", "database"},
    "content.compile_lesson": {"problem", "database"},
    "math.solve_linear": {"matrix", "rhs"},
    "physics.constant_acceleration": {
        "initial_position_m",
        "initial_velocity_m_per_s",
        "acceleration_m_per_s2",
        "time_s",
    },
    "exam.recommend": {"exam", "as_of_year", "target_year", "topics", "data"},
    "exam.backtest": {"exam", "as_of_year", "target_year", "topics", "data"},
    "exam.forecast": {
        "exam",
        "target_year",
        "question_count",
        "simulations",
        "seed",
        "topics",
        "data",
    },
    "exam.import_candidates": set(),
    "matrix.build": {"exam_papers", "books"},
    "audio.analyze_reference": {"wav"},
    "production.index_references": {"videos_dir", "database"},
    "production.record_review": {
        "database",
        "video_title",
        "concept_ids",
        "editing",
        "narration_pacing",
        "narration_clarity",
        "narration_sync",
        "sound",
        "visual_clarity",
        "notes",
    },
    "video.request": {"brief", "batch_id", "episodes", "formats"},
    "video.lesson_plan": {
        "matrix",
        "matrix_path",
        "concept_ids",
        "question_id",
        "book_section_id",
        "observations",
        "history",
        "seed",
    },
    "video.batch_plan": {"manifest", "matrix", "production_database"},
    "video.render_batch": {
        "manifest",
        "formats",
        "video_ids",
        "quality",
        "fps",
        "resume",
        "output_dir",
    },
}
REQUIRED_PARAMETERS = {
    "content.solve": {"problem"},
    "content.compile_lesson": {"problem"},
    "math.solve_linear": {"matrix", "rhs"},
    "physics.constant_acceleration": {
        "initial_position_m",
        "initial_velocity_m_per_s",
        "acceleration_m_per_s2",
        "time_s",
    },
    "video.request": {"brief"},
    "video.batch_plan": {"manifest"},
    "video.render_batch": {"manifest"},
    "audio.analyze_reference": {"wav"},
    "production.index_references": {"videos_dir"},
    "production.record_review": {
        "video_title",
        "concept_ids",
        "editing",
        "narration_pacing",
        "narration_clarity",
        "narration_sync",
        "sound",
        "visual_clarity",
    },
}


class StudioRequestError(ValueError):
    """Raised for malformed or unsafe studio requests."""


def _json_value(value: Any) -> Any:
    if is_dataclass(value):
        return _json_value(asdict(value))
    if isinstance(value, dict):
        return {str(key): _json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json_value(item) for item in value]
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, (str, int, float, bool)) or value is None:
        if isinstance(value, float) and not math.isfinite(value):
            raise StudioRequestError("engine result contains a non-finite number")
        return value
    raise StudioRequestError(
        f"engine returned unsupported result type {type(value).__name__}"
    )


def _read_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise StudioRequestError(f"cannot read {label} {path}: {exc}") from exc


def _write_json(path: Path, value: Any) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(_json_value(value), indent=2, ensure_ascii=False, allow_nan=False)
            + "\n",
            encoding="utf-8",
        )
    except (OSError, UnicodeError, TypeError, ValueError) as exc:
        raise StudioRequestError(f"cannot write JSON artifact {path}: {exc}") from exc


def _task_dependencies(task: dict[str, Any]) -> set[str]:
    dependencies = set(task.get("depends_on", []))

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            reference = value.get("$ref")
            if isinstance(reference, str):
                task_id = reference.split("#", 1)[0]
                if task_id:
                    dependencies.add(task_id)
            for item in value.values():
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(task.get("params", {}))
    return dependencies


def validate_request(request: Any) -> dict[str, Any]:
    if not isinstance(request, dict):
        raise StudioRequestError("request must be a JSON object")
    unknown_request_fields = set(request) - {
        "schema_version",
        "run_id",
        "output_dir",
        "tasks",
    }
    if unknown_request_fields:
        raise StudioRequestError(
            "unknown request field(s): " + ", ".join(sorted(unknown_request_fields))
        )
    schema_version = request.get("schema_version")
    if (
        isinstance(schema_version, bool)
        or not isinstance(schema_version, int)
        or schema_version != 1
    ):
        raise StudioRequestError("schema_version must be 1")
    run_id = request.get("run_id")
    if run_id is not None and (
        not isinstance(run_id, str)
        or not TASK_ID.fullmatch(run_id)
    ):
        raise StudioRequestError("run_id must contain 1-64 letters, digits, '.', '_' or '-'")
    output_dir = request.get("output_dir", "output/studio")
    if (
        not isinstance(output_dir, str)
        or not output_dir.strip()
        or Path(output_dir).is_absolute()
        or ".." in Path(output_dir).parts
    ):
        raise StudioRequestError("output_dir must be a repository-relative path without '..'")
    tasks = request.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise StudioRequestError("tasks must be a non-empty array")
    if len(tasks) > MAX_TASKS:
        raise StudioRequestError(f"a run may contain at most {MAX_TASKS} tasks")
    seen: set[str] = set()
    for position, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise StudioRequestError(f"tasks[{position}] must be an object")
        unknown_task_fields = set(task) - {"id", "action", "params", "depends_on"}
        if unknown_task_fields:
            raise StudioRequestError(
                f"tasks[{position}] has unknown field(s): "
                + ", ".join(sorted(unknown_task_fields))
            )
        task_id = task.get("id")
        if not isinstance(task_id, str) or not TASK_ID.fullmatch(task_id):
            raise StudioRequestError(f"tasks[{position}].id is invalid")
        if task_id in seen:
            raise StudioRequestError(f"duplicate task id {task_id!r}")
        seen.add(task_id)
        action = task.get("action")
        if not isinstance(action, str) or action not in SUPPORTED_ACTIONS:
            raise StudioRequestError(
                f"{task_id}: unsupported action {task.get('action')!r}; "
                f"choose from {', '.join(sorted(SUPPORTED_ACTIONS))}"
            )
        params = task.get("params", {})
        if not isinstance(params, dict):
            raise StudioRequestError(f"{task_id}.params must be an object")
        unknown_parameters = set(params) - ACTION_PARAMETERS[action]
        if unknown_parameters:
            raise StudioRequestError(
                f"{task_id}: unknown parameter(s) for {action}: "
                + ", ".join(sorted(unknown_parameters))
            )
        missing_parameters = REQUIRED_PARAMETERS.get(action, set()) - set(params)
        if missing_parameters:
            raise StudioRequestError(
                f"{task_id}: missing parameter(s) for {action}: "
                + ", ".join(sorted(missing_parameters))
            )
        if action == "video.lesson_plan":
            selectors = {
                "concept_ids",
                "question_id",
                "book_section_id",
            } & set(params)
            if len(selectors) != 1:
                raise StudioRequestError(
                    f"{task_id}: video.lesson_plan requires exactly one of "
                    "concept_ids, question_id, or book_section_id"
                )
            if ("matrix" in params) == ("matrix_path" in params):
                raise StudioRequestError(
                    f"{task_id}: video.lesson_plan requires exactly one of matrix or matrix_path"
                )
        dependencies = task.get("depends_on", [])
        if not isinstance(dependencies, list) or any(
            not isinstance(dependency, str) for dependency in dependencies
        ):
            raise StudioRequestError(f"{task_id}.depends_on must be an array of task IDs")
    positions = {task["id"]: index for index, task in enumerate(tasks)}
    for task in tasks:
        for dependency in _task_dependencies(task):
            if dependency not in seen:
                raise StudioRequestError(
                    f"{task['id']}: dependency {dependency!r} does not exist"
                )
    _validate_acyclic(tasks)
    for index, task in enumerate(tasks):
        for dependency in _task_dependencies(task):
            if positions[dependency] >= index:
                raise StudioRequestError(
                    f"{task['id']}: dependency {dependency!r} must appear earlier in tasks"
                )
    return {
        "schema_version": 1,
        "run_id": run_id or f"run-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}-{uuid.uuid4().hex[:8]}",
        "output_dir": output_dir,
        "tasks": tasks,
    }


def _validate_acyclic(tasks: list[dict[str, Any]]) -> None:
    task_map = {task["id"]: task for task in tasks}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in visiting:
            raise StudioRequestError(f"task dependency cycle includes {task_id!r}")
        if task_id in visited:
            return
        visiting.add(task_id)
        for dependency in _task_dependencies(task_map[task_id]):
            visit(dependency)
        visiting.remove(task_id)
        visited.add(task_id)

    for task in tasks:
        visit(task["id"])


def _resolve_references(value: Any, results: dict[str, Any]) -> Any:
    if isinstance(value, dict):
        reference = value.get("$ref")
        if isinstance(reference, str):
            task_id, separator, pointer = reference.partition("#")
            if task_id not in results:
                raise StudioRequestError(
                    f"reference {reference!r} is not available; list dependencies before use"
                )
            resolved = results[task_id]
            if separator and pointer:
                if not pointer.startswith("/"):
                    raise StudioRequestError(
                        f"reference pointer in {reference!r} must start with '/'"
                    )
                for component in pointer[1:].split("/"):
                    component = component.replace("~1", "/").replace("~0", "~")
                    try:
                        resolved = (
                            resolved[int(component)]
                            if isinstance(resolved, list)
                            else resolved[component]
                        )
                    except (KeyError, IndexError, ValueError, TypeError) as exc:
                        raise StudioRequestError(
                            f"reference {reference!r} does not resolve"
                        ) from exc
            return resolved
        return {key: _resolve_references(item, results) for key, item in value.items()}
    if isinstance(value, list):
        return [_resolve_references(item, results) for item in value]
    return value


class StudioEngine:
    """One local coordinator; specialized engines remain independently testable."""

    def __init__(self, root: Path = ROOT) -> None:
        self.root = Path(root).resolve()

    def _repo_path(self, value: Any, label: str) -> Path:
        if not isinstance(value, str) or not value.strip():
            raise StudioRequestError(f"{label} must be a non-empty path string")
        path = Path(value)
        resolved = path.resolve() if path.is_absolute() else (self.root / path).resolve()
        try:
            resolved.relative_to(self.root)
        except ValueError as exc:
            raise StudioRequestError(f"{label} must stay within the repository root") from exc
        return resolved

    def _repository_path_string(self, path: Path) -> str:
        try:
            return Path(path).resolve().relative_to(self.root).as_posix()
        except ValueError:
            return Path(path).as_posix()

    def run(
        self,
        request: Any,
        *,
        output_override: Path | None = None,
    ) -> dict[str, Any]:
        normalized = validate_request(request)
        output_root = (
            Path(output_override).resolve()
            if output_override is not None
            else self._repo_path(normalized["output_dir"], "output_dir")
            / normalized["run_id"]
        )
        if output_root.exists() and any(output_root.iterdir()):
            raise StudioRequestError(
                f"output directory is not empty: {output_root}; choose a new run_id or directory"
            )
        output_root.mkdir(parents=True, exist_ok=True)
        start_time = datetime.now(timezone.utc).isoformat()
        task_results: dict[str, Any] = {}
        task_reports: list[dict[str, Any]] = []
        report_by_id: dict[str, dict[str, Any]] = {}

        for task in normalized["tasks"]:
            dependencies = _task_dependencies(task)
            failed_dependencies = sorted(
                dependency
                for dependency in dependencies
                if report_by_id[dependency]["status"] != "succeeded"
            )
            if failed_dependencies:
                report = {
                    "id": task["id"],
                    "action": task["action"],
                    "status": "blocked",
                    "error": "dependency task(s) failed: " + ", ".join(failed_dependencies),
                }
            else:
                try:
                    params = _resolve_references(task.get("params", {}), task_results)
                    result = self._dispatch(task["action"], params, output_root)
                    task_results[task["id"]] = result
                    result_path = output_root / f"{task['id']}.json"
                    _write_json(result_path, result)
                    report = {
                        "id": task["id"],
                        "action": task["action"],
                        "status": "succeeded",
                        "result_file": result_path.relative_to(self.root).as_posix()
                        if result_path.is_relative_to(self.root)
                        else result_path.as_posix(),
                    }
                except Exception as exc:
                    report = {
                        "id": task["id"],
                        "action": task["action"],
                        "status": "failed",
                        "error": f"{type(exc).__name__}: {exc}",
                    }
            task_reports.append(report)
            report_by_id[task["id"]] = report

        succeeded = sum(task["status"] == "succeeded" for task in task_reports)
        failed = sum(task["status"] == "failed" for task in task_reports)
        blocked = sum(task["status"] == "blocked" for task in task_reports)
        status = (
            "succeeded"
            if failed == 0 and blocked == 0
            else "failed"
            if succeeded == 0
            else "partial"
        )
        run_report = {
            "schema_version": RUN_SCHEMA_VERSION,
            "run_id": normalized["run_id"],
            "status": status,
            "started_at": start_time,
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "repository_revision": self._revision(),
            "request_sha256": hashlib.sha256(
                json.dumps(normalized, sort_keys=True, ensure_ascii=False).encode("utf-8")
            ).hexdigest(),
            "task_counts": {
                "total": len(task_reports),
                "succeeded": succeeded,
                "failed": failed,
                "blocked": blocked,
            },
            "tasks": task_reports,
            "capability_note": (
                "A successful engine task is not equivalent to academic, audio, video, "
                "accessibility, or publication approval."
            ),
        }
        _write_json(output_root / "run.json", run_report)
        return run_report

    def _revision(self) -> str | None:
        git_dir = self.root / ".git"
        if not git_dir.exists():
            return None
        try:
            result = subprocess.run(
                ["git", "-C", str(self.root), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError):
            return None
        return result.stdout.strip()

    def _dispatch(
        self,
        action: str,
        params: dict[str, Any],
        output_root: Path,
    ) -> Any:
        if action == "content.initialize":
            from content_engine.database import ContentDatabase

            database = ContentDatabase(
                self._repo_path(params.get("database", "output/content.sqlite"), "database")
            )
            database.initialize(self.root)
            return {
                "database": self._repository_path_string(database.path),
                "summary": database.summary(),
            }

        if action == "content.summary":
            from content_engine.database import ContentDatabase

            database = ContentDatabase(
                self._repo_path(params.get("database", "output/content.sqlite"), "database")
            )
            if not database.path.is_file():
                raise StudioRequestError(
                    f"database not found: {database.path}; run content.initialize first"
                )
            return {
                "database": self._repository_path_string(database.path),
                "summary": database.summary(),
            }

        if action in {"content.solve", "content.compile_lesson"}:
            return self._content_lesson(action, params)

        if action == "math.solve_linear":
            from math_engine.linear_algebra import solve_linear_system

            solution = solve_linear_system(params.get("matrix"), params.get("rhs"))
            return {
                "solution": solution.values,
                "residual_inf_norm": solution.residual_inf_norm,
                "numeric_type": "IEEE-754 binary64",
                "warning": "Check model assumptions and conditioning independently.",
            }

        if action == "physics.constant_acceleration":
            from physics_engine.kinematics import constant_acceleration

            position, velocity = constant_acceleration(
                params.get("initial_position_m"),
                params.get("initial_velocity_m_per_s"),
                params.get("acceleration_m_per_s2"),
                params.get("time_s"),
            )
            return {
                "position_m": position,
                "velocity_m_per_s": velocity,
                "model": "constant acceleration in a specified inertial frame",
                "warning": "Validate model assumptions and initial conditions independently.",
            }

        if action in {"exam.recommend", "exam.backtest", "exam.forecast"}:
            return self._exam(action, params)

        if action == "exam.import_candidates":
            from tools.import_exam_candidates import import_candidates

            return import_candidates(self.root)

        if action == "matrix.build":
            from matrix_pipeline import build_network

            exam_dir = self._repo_path(
                params.get("exam_papers", "exam_papers"), "exam_papers"
            )
            books_dir = self._repo_path(params.get("books", "book"), "books")
            network, warnings = build_network(exam_dir, books_dir)
            return {
                "network": network,
                "warnings": warnings,
                "indexed_questions": len(network.get("question_analyses", [])),
                "indexed_book_sections": network.get("book_concept_matrix", {}).get(
                    "shape", [0, 0]
                )[0],
                "limitations": (
                    "Concept matches are keyword evidence, not verified question tags."
                ),
            }

        if action == "audio.analyze_reference":
            from tools.analyze_voice_sample import analyze

            wav_path = self._repo_path(params.get("wav"), "wav")
            return analyze(wav_path)

        if action == "production.index_references":
            from production_knowledge import ProductionKnowledge

            database = self._repo_path(
                params.get("database", "output/production_knowledge.sqlite"),
                "database",
            )
            result = ProductionKnowledge(database).index_videos(
                self._repo_path(params.get("videos_dir"), "videos_dir")
            )
            result["database"] = self._repository_path_string(database)
            return result

        if action == "production.record_review":
            from production_knowledge import ProductionKnowledge

            database = self._repo_path(
                params.get("database", "output/production_knowledge.sqlite"),
                "database",
            )
            review_id = ProductionKnowledge(database).record_review(
                video_title=params["video_title"],
                concept_ids=params["concept_ids"],
                editing=params["editing"],
                narration_pacing=params["narration_pacing"],
                narration_clarity=params["narration_clarity"],
                narration_sync=params["narration_sync"],
                sound=params["sound"],
                visual_clarity=params["visual_clarity"],
                notes=params.get("notes", ""),
            )
            return {
                "review_id": review_id,
                "database": self._repository_path_string(database),
                "status": "recorded",
            }

        if action == "video.request":
            from content_engine.request import build_request

            batch_request = build_request(
                params.get("brief", ""),
                batch_id=params.get("batch_id"),
                episodes=params.get("episodes", 10),
                formats=params.get("formats", "both"),
            )
            path = (
                output_root
                / "artifacts"
                / "requests"
                / f"{batch_request['request_id']}.json"
            )
            _write_json(path, batch_request)
            return {
                "request": batch_request,
                "request_file": path.relative_to(output_root).as_posix(),
            }

        if action == "video.lesson_plan":
            from video_learning import generate_plan

            matrix = params.get("matrix")
            if matrix is None:
                matrix_path = params.get("matrix_path")
                if matrix_path is None:
                    raise StudioRequestError(
                        "video.lesson_plan requires matrix or matrix_path; "
                        "use a matrix.build task and reference its network"
                    )
                matrix = _read_json(
                    self._repo_path(matrix_path, "matrix_path"), "matrix network"
                )
            observation_path = params.get("observations")
            observations = (
                _read_json(
                    self._repo_path(observation_path, "observations"),
                    "reviewed video observations",
                )
                if observation_path
                else None
            )
            history_path = self._repo_path(
                params.get("history", "output/video_learning_history.json"),
                "history",
            )
            return generate_plan(
                matrix,
                concept_ids=params.get("concept_ids"),
                question_id=params.get("question_id"),
                book_section_id=params.get("book_section_id"),
                observations=observations,
                history_path=history_path,
                seed=params.get("seed"),
            )

        if action == "video.batch_plan":
            from content_engine.batch import load_batch, validate_batch

            manifest_path = self._repo_path(params.get("manifest"), "manifest")
            manifest = load_batch(manifest_path)
            plan = validate_batch(manifest, self.root)
            result: dict[str, Any] = {
                "batch_id": manifest["batch_id"],
                "status": manifest["status"],
                "manifest": self._repository_path_string(manifest_path),
                "deliverables": plan,
            }
            matrix = params.get("matrix")
            if matrix is not None:
                from production_knowledge import ProductionKnowledge

                database = self._repo_path(
                    params.get("production_database", "output/production_knowledge.sqlite"),
                    "production_database",
                )
                result["production_advice"] = ProductionKnowledge(
                    database
                ).advise_batch(manifest, matrix)
            return result

        if action == "video.render_batch":
            return self._render_batch(params, output_root)

        raise StudioRequestError(f"action {action!r} has no registered handler")

    def _content_lesson(self, action: str, params: dict[str, Any]) -> dict[str, Any]:
        from content_engine.__main__ import _run_problem
        from content_engine.database import ContentDatabase
        from content_engine.lesson import compile_lesson
        from content_engine.problem import load_problem

        problem_path = self._repo_path(params.get("problem"), "problem")
        database = ContentDatabase(
            self._repo_path(params.get("database", "output/content.sqlite"), "database")
        )
        if action == "content.solve":
            problem, result, run_id = _run_problem(database, problem_path)
            return {
                "problem_id": problem["problem_id"],
                "run_id": run_id,
                "computation_status": result.computation_status,
                "result": result.to_dict(),
            }
        problem, result, run_id = _run_problem(database, problem_path)
        connection = database.connect()
        try:
            lesson = compile_lesson(connection, problem, result.to_dict())
        finally:
            connection.close()
        lesson["engine_run_id"] = run_id
        return lesson

    def _exam(self, action: str, params: dict[str, Any]) -> Any:
        from exam_engine.engine import (
            EXAMS,
            forecast_test,
            load_backtest,
            load_recommendations,
            load_topics,
            render_test_forecast,
            render_video_batch,
        )

        exam = params.get("exam", "jee-advanced")
        if exam not in EXAMS:
            raise StudioRequestError(f"exam must be one of {', '.join(EXAMS)}")
        topics = load_topics(
            self._repo_path(params.get("topics", "data/physics_topics.csv"), "topics")
        )
        data_path = self._repo_path(
            params.get("data", "data/exam_question_metadata.csv"), "data"
        )
        year = params.get("target_year", params.get("as_of_year", date.today().year))
        if action == "exam.recommend":
            recommendations = load_recommendations(
                data_path, topics, exam=exam, as_of_year=year
            )
            return {
                "exam": exam,
                "as_of_year": year,
                "recommendations": recommendations,
                "rendered_briefs": render_video_batch(
                    recommendations, exam=exam, as_of_year=year
                ),
            }
        if action == "exam.backtest":
            result = load_backtest(
                data_path, topics, exam=exam, as_of_year=year
            )
            return {"exam": exam, "as_of_year": year, "backtest": result}
        forecast = forecast_test(
            data_path,
            topics,
            exam=exam,
            target_year=year,
            question_count=params.get("question_count", 10),
            simulations=params.get("simulations", 10_000),
            seed=params.get("seed", 2026),
        )
        return render_test_forecast(forecast)

    def _render_batch(
        self,
        params: dict[str, Any],
        output_root: Path,
    ) -> dict[str, Any]:
        from content_engine.batch import load_batch
        from exam_engine.engine import DataValidationError
        from tools.render_video_batch import render

        manifest_path = self._repo_path(params.get("manifest"), "manifest")
        manifest = load_batch(manifest_path)
        quality = params.get("quality", "preview")
        if quality not in {"preview", "high"}:
            raise StudioRequestError("quality must be preview or high")
        if quality == "high" and manifest.get("status") != "approved-for-storyboarding":
            raise StudioRequestError(
                "high-quality rendering requires approved-for-storyboarding status"
            )
        output_dir = self._repo_path(
            params.get("output_dir", (output_root / "renders").relative_to(self.root).as_posix()),
            "render output_dir",
        )
        formats = params.get("formats", ["vertical", "horizontal"])
        video_ids = params.get("video_ids")
        if not isinstance(formats, list) or not formats:
            raise StudioRequestError("formats must be a non-empty array")
        if any(not isinstance(item, str) for item in formats):
            raise StudioRequestError("formats must contain only strings")
        if video_ids is not None and not isinstance(video_ids, list):
            raise StudioRequestError("video_ids must be an array")
        fps = params.get("fps", 15 if quality == "preview" else 30)
        if fps not in {15, 30}:
            raise StudioRequestError("fps must be 15 or 30")
        try:
            report_path = render(
                manifest_path,
                output_dir,
                video_ids=video_ids,
                formats=formats,
                quality=quality,
                fps=fps,
                resume=bool(params.get("resume", False)),
            )
        except (OSError, subprocess.CalledProcessError, DataValidationError) as exc:
            raise StudioRequestError(f"video render failed: {exc}") from exc
        return _read_json(report_path, "video render report")
