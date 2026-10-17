"""Create a concise, human/assistant-ready brief for an original video batch."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any

from exam_engine.engine import DataValidationError, load_topics
from knowledge.graph import load_graph
from matrix_pipeline import ROOT, match_concepts


FORMAT_PRESETS: dict[str, dict[str, Any]] = {
    "both": {
        "outputs": [
            {"format": "vertical", "count_per_episode": 1, "duration_seconds": 60, "aspect_ratio": "9:16"},
            {"format": "horizontal", "count_per_episode": 1, "duration_seconds": 180, "aspect_ratio": "16:9"},
        ],
        "deliverables_per_episode": 2,
    },
    "vertical": {
        "outputs": [
            {"format": "vertical", "count_per_episode": 1, "duration_seconds": 60, "aspect_ratio": "9:16"},
        ],
        "deliverables_per_episode": 1,
    },
    "horizontal": {
        "outputs": [
            {"format": "horizontal", "count_per_episode": 1, "duration_seconds": 180, "aspect_ratio": "16:9"},
        ],
        "deliverables_per_episode": 1,
    },
}
DEFAULT_CREATIVE_DIRECTION = (
    "Make the reasoning correct and easy to inspect, then make the explanation "
    "memorable and visually beautiful. Use original visual metaphors, intentional "
    "composition, clear typography, purposeful motion, expressive but restrained "
    "pacing, and thoughtful sound. Do not imitate a creator's signature style."
)


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug[:48].strip("-") or "physics-video-batch"


def _concept_suggestions(text: str) -> list[dict[str, Any]]:
    topics = load_topics(ROOT / "data" / "physics_topics.csv")
    graph = load_graph(
        ROOT / "knowledge" / "concepts.csv",
        ROOT / "knowledge" / "links.csv",
        topics,
    )
    matches = match_concepts(text, graph)
    catalog = graph.by_id()
    ranked = sorted(
        (
            {
                "concept_id": concept_id,
                "name": catalog[concept_id].concept_name,
                "candidate_score": round(float(item["score"]), 4),
                "matched_phrases": item["phrases"],
            }
            for concept_id, item in matches.items()
        ),
        key=lambda item: (-item["candidate_score"], item["concept_id"]),
    )
    return ranked[:8]


def build_request(
    brief: str,
    *,
    batch_id: str | None = None,
    episodes: int = 10,
    formats: str = "both",
) -> dict[str, Any]:
    if not isinstance(brief, str) or not brief.strip():
        raise DataValidationError("brief must contain a topic or teaching request")
    if not isinstance(episodes, int) or isinstance(episodes, bool) or not 1 <= episodes <= 10:
        raise DataValidationError("episodes must be an integer from 1 to 10")
    if formats not in FORMAT_PRESETS:
        raise DataValidationError("formats must be both, vertical, or horizontal")
    request_id = batch_id or f"{_slug(brief)}-{hashlib.sha256(brief.encode()).hexdigest()[:8]}"
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", request_id):
        raise DataValidationError("batch_id must use lowercase letters, digits, '.', '_' or '-'")
    suggestions = _concept_suggestions(brief)
    return {
        "schema_version": 1,
        "request_id": request_id,
        "status": "intake-ready-for-original-authoring",
        "owner_brief": brief.strip(),
        "suggested_concepts": suggestions,
        "concept_match_note": (
            "Suggestions are keyword evidence from the local concept graph, not confirmed "
            "curriculum mappings. Review or replace them before authoring."
        ),
        "batch": {
            "episode_count": episodes,
            "formats": FORMAT_PRESETS[formats]["outputs"],
            "deliverable_count": episodes * FORMAT_PRESETS[formats]["deliverables_per_episode"],
            "narration_language": "English",
            "audience": {
                "minimum_age": 14,
                "maximum_age": 21,
                "level": "school physics through JEE/NEET foundation; define symbols and state assumptions",
            },
        },
        "creative_direction": DEFAULT_CREATIVE_DIRECTION,
        "authoring_checklist": [
            "Create original questions/examples and narration; do not copy book prose, exam questions, transcripts, or figures.",
            "Trace each academic claim to an exact source section and check rights before reuse.",
            "State assumptions, variables, signs, units, derivation, and an independent answer check.",
            "For each episode propose an original visual hook, narration beats, editing rhythm, sound plan, and misconception check.",
            "Draft a complete batch_*.json manifest that passes `python -m content_engine batch-plan --manifest <path>`.",
            "Keep physics review, owner approval, preview QC, and publication as separate gates.",
        ],
        "handoff": {
            "assistant": "Use this request file as the brief to author and review the complete episode manifest.",
            "github": "Commit this request and the approved manifest to the repository; dispatch the Render approved batch workflow with the manifest path.",
            "colab": "Set BATCH_MANIFEST to the approved manifest path in notebooks/render_in_colab.ipynb and use a reviewed REVISION.",
            "render_command": (
                "python tools/render_video_batch.py --manifest <approved-manifest.json> "
                "--quality high --output-dir output/<batch-id>"
            ),
            "render_safety": "Only an approved, validated manifest can be rendered; this request itself is not video content or an approval.",
        },
    }


def create_interactive_request(
    *,
    batch_id: str | None = None,
    episodes: int = 10,
    formats: str = "both",
) -> dict[str, Any]:
    print("Describe the lesson batch in your own words.")
    print("Example: JEE kinematics, focus on reading velocity-time graphs.")
    try:
        brief = input("Your brief: ")
    except EOFError as exc:
        raise DataValidationError("no brief was supplied on standard input") from exc
    return build_request(
        brief,
        batch_id=batch_id,
        episodes=episodes,
        formats=formats,
    )


def write_request(request: dict[str, Any], output: Path) -> None:
    output = Path(output)
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(request, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except (OSError, UnicodeError) as exc:
        raise DataValidationError(f"cannot write batch request {output}: {exc}") from exc


def main_from_args(args: Any) -> int:
    try:
        request = (
            build_request(
                args.brief,
                batch_id=args.batch_id,
                episodes=args.episodes,
                formats=args.formats,
            )
            if args.brief
            else create_interactive_request(
                batch_id=args.batch_id,
                episodes=args.episodes,
                formats=args.formats,
            )
        )
        output = args.output or ROOT / "requests" / f"{request['request_id']}.json"
        write_request(request, output)
    except DataValidationError as exc:
        print(f"content_engine: error: {exc}", file=sys.stderr)
        return 2
    print(
        f"Created {request['batch']['deliverable_count']} deliverable request "
        f"for {request['batch']['episode_count']} episode(s): {output}"
    )
    print("Next: ask the assistant to author this request, then render its approved manifest.")
    return 0
