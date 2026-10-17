"""Generate original, matrix-informed lesson-design plans.

This is a transparent, review-driven planner, not a model trained on raw
copyrighted books or video/audio files.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import random
import secrets
import sys
from typing import Any

from exam_engine.engine import DataValidationError
from matrix_pipeline import ROOT, build_network


DEFAULT_HISTORY = ROOT / "output" / "video_style_history.json"
STYLE_PROFILES: dict[str, dict[str, Any]] = {
    "concept_first": {
        "label": "Concept-first investigation",
        "base_weight": 1.0,
        "question_factor": 0.75,
        "concept_domains": {"physics": 1.5, "mathematics": 1.0},
        "concept_ids": {},
        "beats": [
            ("Question", "Pose one precise question and state what is known."),
            ("Model", "Name the quantities, assumptions, and convention."),
            ("Reasoning", "Build the explanation from the model, one step at a time."),
            ("Check", "Test units, a limiting case, or an independent consequence."),
            ("Takeaway", "State what the result means and where it applies."),
        ],
    },
    "worked_problem": {
        "label": "Worked-problem reasoning",
        "base_weight": 0.8,
        "question_factor": 2.0,
        "concept_domains": {"physics": 1.0, "mathematics": 0.8},
        "concept_ids": {},
        "beats": [
            ("Read", "Extract the givens, target, and constraints."),
            ("Choose", "Select a governing model and justify its assumptions."),
            ("Solve", "Show the essential algebra without skipping sign or unit checks."),
            ("Verify", "Substitute or test a special case independently."),
            ("Generalize", "Identify the reusable idea without promising an exam prediction."),
        ],
    },
    "representation_bridge": {
        "label": "Representation bridge",
        "base_weight": 0.75,
        "question_factor": 0.9,
        "concept_domains": {"mathematics": 1.6, "physics": 0.8},
        "concept_ids": {
            "math:matrices": 2.0,
            "math:linear-maps": 2.0,
            "math:eigenmodes": 1.8,
            "math:fourier": 1.8,
            "math:graphs": 1.6,
            "math:derivatives": 1.5,
            "math:integrals": 1.5,
        },
        "beats": [
            ("Original form", "Show the question in its natural representation."),
            ("Bridge", "Define a useful second representation and its mapping."),
            ("Transform", "Derive how the relevant operation changes."),
            ("Work", "Use the transformed representation on a small example."),
            ("Return", "Map back and verify in the original variables."),
        ],
    },
    "geometric_calculus": {
        "label": "Geometric calculus",
        "base_weight": 0.65,
        "question_factor": 0.8,
        "concept_domains": {"mathematics": 1.3, "physics": 0.8},
        "concept_ids": {
            "math:derivatives": 2.1,
            "math:integrals": 2.1,
            "math:graphs": 1.8,
            "math:optimization": 1.5,
        },
        "beats": [
            ("Quantity", "Define the changing quantity and its units."),
            ("Local view", "Connect slope or rate to a small change in the model."),
            ("Accumulation", "Interpret the relevant sum or integral over an interval."),
            ("Example", "Compute one original, dimensionally consistent example."),
            ("Check", "Compare geometric and algebraic reasoning."),
        ],
    },
    "physical_model": {
        "label": "Physical-model exploration",
        "base_weight": 0.9,
        "question_factor": 0.85,
        "concept_domains": {"physics": 1.8, "mathematics": 0.7},
        "concept_ids": {},
        "beats": [
            ("System", "Define the system boundary and the observable."),
            ("Mechanism", "Show the physical interaction or change being modeled."),
            ("Equation", "Connect the mechanism to a stated mathematical model."),
            ("Prediction", "Derive a measurable consequence."),
            ("Limit", "Check a boundary case and state the model's limits."),
        ],
    },
}

VISUAL_TREATMENTS = (
    "coordinate_plot",
    "state_transition",
    "geometric_construction",
    "equation_evolution",
)
AUDIO_PALETTES: dict[str, dict[str, str]] = {
    "quiet_precision": {
        "bed": "Prefer silence; keep the narration and mathematical detail clear.",
        "cue": "Use one quiet, dry tick only when a meaningful step is completed.",
    },
    "soft_percussion": {
        "bed": "Use a sparse, low-level original percussive pulse between explanations.",
        "cue": "Use a muted original tap to mark a transition, never every equation.",
    },
    "warm_tonal": {
        "bed": "Use a restrained, original sustained tone only under non-dense passages.",
        "cue": "Use a short, soft tonal accent for a conceptual reveal.",
    },
    "spatial_minimal": {
        "bed": "Use near-silence with a subtle original spatial texture, if useful.",
        "cue": "Use a brief, low-level airy transition between representations.",
    },
}
VISUAL_AFFINITIES: dict[str, dict[str, Any]] = {
    "coordinate_plot": {
        "base": 0.8,
        "domains": {"mathematics": 0.4},
        "concepts": {
            "math:graphs": 1.5,
            "math:derivatives": 1.2,
            "math:integrals": 1.2,
            "math:fourier": 1.0,
        },
    },
    "state_transition": {
        "base": 0.8,
        "domains": {"physics": 0.4},
        "concepts": {
            "physics:kinematics": 1.3,
            "physics:oscillations_waves": 1.2,
            "physics:current_electricity": 1.0,
            "physics:em_induction": 1.0,
        },
    },
    "geometric_construction": {
        "base": 0.8,
        "domains": {"mathematics": 0.3, "physics": 0.3},
        "concepts": {
            "math:geometry": 1.2,
            "math:scalars-vectors": 1.2,
            "math:matrices": 1.0,
            "math:linear-maps": 1.0,
            "physics:optics": 0.8,
        },
    },
    "equation_evolution": {
        "base": 0.8,
        "domains": {"mathematics": 0.3},
        "concepts": {
            "math:linear-systems": 1.2,
            "math:matrices": 1.0,
            "math:derivatives": 1.0,
            "math:integrals": 1.0,
        },
    },
}
AUDIO_AFFINITIES: dict[str, dict[str, Any]] = {
    "quiet_precision": {
        "base": 1.0,
        "domains": {"mathematics": 0.4},
        "concepts": {
            "math:matrices": 0.8,
            "math:linear-systems": 0.8,
            "math:derivatives": 0.6,
            "math:integrals": 0.6,
        },
        "question": 0.1,
    },
    "soft_percussion": {
        "base": 0.8,
        "domains": {"physics": 0.3},
        "concepts": {
            "physics:kinematics": 0.7,
            "physics:current_electricity": 0.6,
            "physics:oscillations_waves": 0.5,
        },
        "question": 0.4,
    },
    "warm_tonal": {
        "base": 0.8,
        "domains": {"physics": 0.5},
        "concepts": {
            "physics:work_energy": 0.6,
            "physics:thermodynamics": 0.6,
            "physics:modern_physics": 0.5,
        },
        "question": 0.1,
    },
    "spatial_minimal": {
        "base": 0.8,
        "domains": {"physics": 0.3},
        "concepts": {
            "math:fourier": 0.8,
            "physics:oscillations_waves": 0.8,
            "physics:electromagnetic_waves": 0.8,
            "physics:electrostatics": 0.4,
        },
        "question": 0.1,
    },
}
MAX_MATRIX_CONCEPTS = 5
MIN_RELATIVE_MATRIX_SCORE = 0.3


def _read_json(path: Path, description: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DataValidationError(f"cannot read {description} {path}: {exc}") from exc


def _validate_network(network: Any) -> dict[str, Any]:
    if not isinstance(network, dict) or not isinstance(network.get("concepts"), list):
        raise DataValidationError("matrix network must contain a concepts list")
    concept_ids: set[str] = set()
    for item in network["concepts"]:
        if not isinstance(item, dict) or not isinstance(item.get("id", item.get("concept_id")), str):
            raise DataValidationError("matrix network contains a malformed concept")
        concept_id = item.get("id", item.get("concept_id"))
        if concept_id in concept_ids:
            raise DataValidationError(f"matrix network contains duplicate concept {concept_id!r}")
        concept_ids.add(concept_id)
    for key in (
        "question_concept_matrix",
        "book_concept_matrix",
        "book_linked_concept_matrix",
    ):
        matrix = network.get(key)
        if matrix is None:
            continue
        if not isinstance(matrix, dict):
            raise DataValidationError(f"{key} must be a matrix object")
        labels = matrix.get("column_labels")
        values = matrix.get("values")
        rows = matrix.get("row_labels")
        if not isinstance(labels, list) or not isinstance(values, list) or not isinstance(rows, list):
            raise DataValidationError(f"{key} has malformed labels or values")
        if labels != [item.get("id", item.get("concept_id")) for item in network["concepts"]]:
            raise DataValidationError(f"{key} concept columns do not match the concept catalog")
        if len(values) != len(rows) or any(
            not isinstance(row, list) or len(row) != len(labels) for row in values
        ):
            raise DataValidationError(f"{key} values do not match the declared matrix shape")
        if any(
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not math.isfinite(value)
            or value < 0
            for row in values
            for value in row
        ):
            raise DataValidationError(f"{key} must contain finite non-negative scores")
    input_errors = network.get("input_errors", [])
    if not isinstance(input_errors, list) or any(
        not isinstance(item, dict)
        or not isinstance(item.get("path"), str)
        or not isinstance(item.get("error"), str)
        for item in input_errors
    ):
        raise DataValidationError("matrix network contains malformed input_errors")
    unsupported = network.get("unsupported_files", [])
    if not isinstance(unsupported, list) or any(
        not isinstance(path, str) for path in unsupported
    ):
        raise DataValidationError("matrix network contains malformed unsupported_files")
    return network


def _matrix_scores(matrix: dict[str, Any], row_label: str) -> dict[str, float]:
    try:
        row_index = matrix["row_labels"].index(row_label)
    except ValueError as exc:
        raise DataValidationError(f"unknown matrix row {row_label!r}") from exc
    values = matrix["values"][row_index]
    scale = max(values, default=0.0)
    if not scale:
        raise DataValidationError(f"matrix row {row_label!r} has no concept matches")
    scores = {
        concept_id: float(score) / scale
        for concept_id, score in zip(matrix["column_labels"], values)
        if score / scale >= MIN_RELATIVE_MATRIX_SCORE
    }
    return dict(
        sorted(scores.items(), key=lambda item: (-item[1], item[0]))[
            :MAX_MATRIX_CONCEPTS
        ]
    )


def select_concepts(
    network: dict[str, Any],
    *,
    concept_ids: list[str] | None = None,
    question_id: str | None = None,
    book_section_id: str | None = None,
) -> tuple[dict[str, float], str]:
    selectors = sum(bool(value) for value in (concept_ids, question_id, book_section_id))
    if selectors != 1:
        raise DataValidationError(
            "select exactly one of concept IDs, a question ID, or a book-section ID"
        )
    concepts = {
        item.get("id", item.get("concept_id")): item for item in network["concepts"]
    }
    if concept_ids:
        unknown = sorted(set(concept_ids) - concepts.keys())
        if unknown:
            raise DataValidationError("unknown concept ID(s): " + ", ".join(unknown))
        return {concept_id: 1.0 for concept_id in dict.fromkeys(concept_ids)}, "selected-concepts"
    if question_id:
        analyses = network.get("question_analyses", [])
        match = next(
            (item for item in analyses if item.get("question_id") == question_id),
            None,
        )
        if match is None:
            raise DataValidationError(f"unknown question ID {question_id!r}")
        ranking = match.get("analysis", {}).get("concepts", [])
        if not isinstance(ranking, list):
            raise DataValidationError(f"question {question_id!r} has malformed concept rankings")
        scores: dict[str, float] = {}
        for item in ranking:
            if not isinstance(item, dict):
                raise DataValidationError(
                    f"question {question_id!r} has a malformed concept ranking"
                )
            concept_id = item.get("concept_id")
            score = item.get("direct_score")
            if concept_id not in concepts:
                continue
            if (
                not isinstance(score, (int, float))
                or isinstance(score, bool)
                or not math.isfinite(score)
                or score < 0
            ):
                raise DataValidationError(
                    f"question {question_id!r} has an invalid score for {concept_id!r}"
                )
            if score > 0:
                scores[concept_id] = float(score)
        if not scores:
            raise DataValidationError(f"question {question_id!r} has no candidate concepts")
        scale = max(scores.values())
        ranked_scores = sorted(
            (
                (concept_id, score / scale)
                for concept_id, score in scores.items()
                if score / scale >= MIN_RELATIVE_MATRIX_SCORE
            ),
            key=lambda item: (-item[1], item[0]),
        )[:MAX_MATRIX_CONCEPTS]
        return dict(ranked_scores), "question"
    matrix = network.get("book_concept_matrix")
    if matrix is None:
        raise DataValidationError("matrix network has no direct book concept matrix")
    return _matrix_scores(matrix, book_section_id or ""), "book-section"


def _load_observations(path: Path | None, valid_concepts: set[str]) -> list[dict[str, Any]]:
    if path is None:
        return []
    observations = _read_json(path, "video observations")
    if not isinstance(observations, list):
        raise DataValidationError("video observations must be a JSON list")
    seen_ids: set[str] = set()
    for index, item in enumerate(observations):
        if not isinstance(item, dict) or set(item) != {
            "video_id", "concept_ids", "style_id", "visual_treatment",
            "audio_palette", "rating",
        }:
            raise DataValidationError(
                f"video observation {index + 1} must contain only video_id, concept_ids, "
                "style_id, visual_treatment, audio_palette, and rating"
            )
        if (
            not isinstance(item["video_id"], str)
            or not item["video_id"].strip()
            or item["video_id"] in seen_ids
        ):
            raise DataValidationError(f"video observation {index + 1} has an invalid video_id")
        seen_ids.add(item["video_id"])
        if not isinstance(item["style_id"], str) or item["style_id"] not in STYLE_PROFILES:
            raise DataValidationError(
                f"video observation {item['video_id']!r} has unknown style_id"
            )
        if (
            not isinstance(item["visual_treatment"], str)
            or item["visual_treatment"] not in VISUAL_TREATMENTS
        ):
            raise DataValidationError(
                f"video observation {item['video_id']!r} has unknown visual_treatment"
            )
        if (
            not isinstance(item["audio_palette"], str)
            or item["audio_palette"] not in AUDIO_PALETTES
        ):
            raise DataValidationError(
                f"video observation {item['video_id']!r} has unknown audio_palette"
            )
        if (
            not isinstance(item["concept_ids"], list)
            or not item["concept_ids"]
            or any(
                not isinstance(concept_id, str) or concept_id not in valid_concepts
                for concept_id in item["concept_ids"]
            )
        ):
            raise DataValidationError(
                f"video observation {item['video_id']!r} has invalid concept_ids"
            )
        if (
            not isinstance(item["rating"], int)
            or isinstance(item["rating"], bool)
            or not 1 <= item["rating"] <= 5
        ):
            raise DataValidationError(
                f"video observation {item['video_id']!r} rating must be an integer from 1 to 5"
            )
    return observations


def _feedback_multipliers(
    observations: list[dict[str, Any]],
    selected_concepts: set[str],
    dimension: str,
    options: tuple[str, ...] | list[str],
) -> dict[str, float]:
    scores: dict[str, list[float]] = defaultdict(list)
    for item in observations:
        observed_concepts = set(item["concept_ids"])
        if observed_concepts & selected_concepts:
            scores[item[dimension]].append((item["rating"] - 1) / 4)
    multipliers: dict[str, float] = {}
    for option in options:
        ratings = scores[option]
        posterior_mean = (2.0 + sum(ratings)) / (4.0 + len(ratings))
        multipliers[option] = 0.5 + posterior_mean
    return multipliers


def _style_weights(
    selected: dict[str, float], selection_type: str, feedback: dict[str, float]
) -> dict[str, float]:
    weights: dict[str, float] = {}
    for style_id, profile in STYLE_PROFILES.items():
        affinity = profile["base_weight"]
        affinity *= profile["question_factor"] if selection_type == "question" else 1.0
        for concept_id, evidence in selected.items():
            domain = concept_id.split(":", 1)[0]
            affinity += evidence * profile["concept_domains"].get(domain, 0.15)
            affinity += evidence * profile["concept_ids"].get(concept_id, 0.0)
        weights[style_id] = max(0.05, affinity) * feedback[style_id]
    return weights


def _treatment_weight(
    selected: dict[str, float],
    selection_type: str,
    treatment: dict[str, Any],
) -> float:
    total_evidence = max(1.0, sum(selected.values()))
    affinity = sum(
        evidence
        * (
            treatment["domains"].get(concept_id.split(":", 1)[0], 0.0)
            + treatment["concepts"].get(concept_id, 0.0)
        )
        for concept_id, evidence in selected.items()
    ) / total_evidence
    question_bonus = treatment.get("question", 0.0) if selection_type == "question" else 0.0
    return treatment["base"] + affinity + question_bonus


def _fingerprint(concept_ids: list[str], style_id: str, visual: str, audio: str) -> str:
    identity = "|".join((*sorted(concept_ids), style_id, visual, audio))
    return hashlib.sha256(identity.encode("utf-8")).hexdigest()


def _load_history(path: Path) -> set[str]:
    if not path.exists():
        return set()
    payload = _read_json(path, "video style history")
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("used_fingerprints"), list)
        or any(not isinstance(item, str) for item in payload["used_fingerprints"])
    ):
        raise DataValidationError(f"invalid video style history file: {path}")
    return set(payload["used_fingerprints"])


def _write_history(path: Path, fingerprints: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_name(path.name + ".tmp")
    try:
        temporary_path.write_text(
            json.dumps({"used_fingerprints": sorted(fingerprints)}, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary_path.replace(path)
    except OSError as exc:
        raise DataValidationError(f"cannot write video style history {path}: {exc}") from exc


def _warn_incomplete_network(network: dict[str, Any]) -> None:
    for item in network.get("input_errors", []):
        print(
            f"warning: skipped invalid matrix input {item.get('path', '<unknown>')}: "
            f"{item.get('error', 'unspecified input error')}",
            file=sys.stderr,
        )
    unsupported = network.get("unsupported_files", [])
    if unsupported:
        print(
            "warning: unsupported matrix inputs were skipped: " + ", ".join(unsupported),
            file=sys.stderr,
        )


def generate_plan(
    network: dict[str, Any],
    *,
    concept_ids: list[str] | None = None,
    question_id: str | None = None,
    book_section_id: str | None = None,
    observations: list[dict[str, Any]] | None = None,
    history_path: Path | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    network = _validate_network(network)
    selected, selection_type = select_concepts(
        network,
        concept_ids=concept_ids,
        question_id=question_id,
        book_section_id=book_section_id,
    )
    concept_catalog = {
        item.get("id", item.get("concept_id")): item for item in network["concepts"]
    }
    observation_rows = observations or []
    selected_ids = set(selected)
    style_feedback = _feedback_multipliers(
        observation_rows, selected_ids, "style_id", tuple(STYLE_PROFILES)
    )
    visual_feedback = _feedback_multipliers(
        observation_rows, selected_ids, "visual_treatment", VISUAL_TREATMENTS
    )
    audio_feedback = _feedback_multipliers(
        observation_rows, selected_ids, "audio_palette", tuple(AUDIO_PALETTES)
    )
    style_weights = _style_weights(selected, selection_type, style_feedback)
    concept_labels = [
        {
            "concept_id": concept_id,
            "name": concept_catalog[concept_id].get(
                "name", concept_catalog[concept_id].get("concept_name", concept_id)
            ),
            "domain": concept_catalog[concept_id].get("domain", "unknown"),
            "matrix_score": round(score, 4),
        }
        for concept_id, score in selected.items()
    ]
    prior_fingerprints = _load_history(history_path) if history_path else set()
    candidates: list[dict[str, Any]] = []
    for style_id, style_weight in style_weights.items():
        for visual in VISUAL_TREATMENTS:
            for audio in AUDIO_PALETTES:
                fingerprint = _fingerprint(list(selected), style_id, visual, audio)
                if fingerprint not in prior_fingerprints:
                    visual_weight = _treatment_weight(
                        selected, selection_type, VISUAL_AFFINITIES[visual]
                    ) * visual_feedback[visual]
                    audio_weight = _treatment_weight(
                        selected, selection_type, AUDIO_AFFINITIES[audio]
                    ) * audio_feedback[audio]
                    candidates.append(
                        {
                            "style_id": style_id,
                            "visual": visual,
                            "audio": audio,
                            "fingerprint": fingerprint,
                            "weight": style_weight * visual_weight * audio_weight,
                        }
                    )
    if not candidates:
        raise DataValidationError(
            "all unique style/visual/audio combinations have been used for this concept set"
        )
    total_weight = sum(item["weight"] for item in candidates)
    chooser = random.Random(seed if seed is not None else secrets.randbits(128))
    draw = chooser.random() * total_weight
    chosen = candidates[-1]
    for candidate in candidates:
        draw -= candidate["weight"]
        if draw < 0:
            chosen = candidate
            break
    style_id = chosen["style_id"]
    style_probability = sum(
        item["weight"] for item in candidates if item["style_id"] == style_id
    ) / total_weight
    visual_probability = sum(
        item["weight"] for item in candidates if item["visual"] == chosen["visual"]
    ) / total_weight
    audio_probability = sum(
        item["weight"] for item in candidates if item["audio"] == chosen["audio"]
    ) / total_weight
    plan = {
        "schema_version": 1,
        "status": "draft-requires-subject-and-teacher-review",
        "selection_type": selection_type,
        "matrix_source_id": question_id or book_section_id,
        "concepts": concept_labels,
        "selection_note": (
            "Matrix scores are evidence-ranking weights, not probabilities of correctness, "
            "exam appearance, or learning outcomes."
        ),
        "teaching_approach": {
            "id": style_id,
            "name": STYLE_PROFILES[style_id]["label"],
            "selection_probability": round(style_probability, 6),
            "beats": [
                {"beat": title, "purpose": purpose}
                for title, purpose in STYLE_PROFILES[style_id]["beats"]
            ],
        },
        "visual_treatment": chosen["visual"],
        "treatment_probabilities": {
            "visual": round(visual_probability, 6),
            "audio_palette": round(audio_probability, 6),
            "selected_combination": round(chosen["weight"] / total_weight, 6),
        },
        "audio_design": {
            "palette": chosen["audio"],
            **AUDIO_PALETTES[chosen["audio"]],
            "sound_effects_are_suggestions_not_generated_audio": True,
        },
        "narration_guidance": [
            "Use original wording; define quantities, assumptions, signs, and units.",
            "Explain one inference at a time, then independently check the result.",
            "Write and review the spoken form of every important equation.",
            "Do not imitate a particular creator's voice, script, visuals, or signature pacing.",
        ],
        "learning_signal": {
            "reviewed_video_observations": len(observation_rows),
            "method": (
                "concept-overlap ratings update teaching, visual, and audio preferences "
                "with independent neutral Beta(2,2) priors"
            ),
            "raw_video_or_audio_analyzed": False,
        },
        "uniqueness_fingerprint": chosen["fingerprint"],
        "probability_note": (
            "This is a normalized sampling weight over remaining original production options, "
            "not a calibrated probability of quality."
        ),
        "review_required": True,
    }
    if history_path:
        prior_fingerprints.add(chosen["fingerprint"])
        _write_history(history_path, prior_fingerprints)
    return plan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build an original, matrix-informed lesson plan with a unique weighted style draw."
    )
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument("--concepts", nargs="+", help="concept IDs from the local concept graph")
    selector.add_argument("--question-id", help="question row ID from the local exam-paper matrix")
    selector.add_argument("--book-section-id", help="section row ID from the local book matrix")
    parser.add_argument("--matrix", type=Path, help="existing matrix_network.json (default: build locally)")
    parser.add_argument("--exam-papers", type=Path, default=ROOT / "exam_papers")
    parser.add_argument("--books", type=Path, default=ROOT / "book")
    parser.add_argument("--observations", type=Path, help="reviewed-video observation JSON")
    parser.add_argument("--history", type=Path, default=DEFAULT_HISTORY)
    parser.add_argument("--seed", type=int, help="optional reproducible random seed")
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "video_lesson_plan.json")
    args = parser.parse_args(argv)
    try:
        network = (
            _validate_network(_read_json(args.matrix, "matrix network"))
            if args.matrix
            else build_network(args.exam_papers, args.books)[0]
        )
        _warn_incomplete_network(network)
        catalog = {
            item.get("id", item.get("concept_id")) for item in network.get("concepts", [])
        }
        observations = _load_observations(args.observations, catalog)
        plan = generate_plan(
            network,
            concept_ids=args.concepts,
            question_id=args.question_id,
            book_section_id=args.book_section_id,
            observations=observations,
            history_path=args.history,
            seed=args.seed,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    except (DataValidationError, OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"Wrote original lesson-design plan to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
