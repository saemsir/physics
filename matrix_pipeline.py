"""Build a local concept-matrix index for exam papers and study books.

Text matching proposes concept links; it does not solve arbitrary questions
or certify a question's source, physics, chemistry, or answer.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Sequence
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile

from exam_engine.engine import DataValidationError, load_topics
from knowledge.graph import ConceptGraph, load_graph


ROOT = Path(__file__).resolve().parent
ROUTES_PATH = ROOT / "knowledge" / "solution_routes.csv"
SUPPORTED_SUFFIXES = {".md", ".mmd", ".txt", ".docx"}
UNSUPPORTED_DOCUMENT_SUFFIXES = {
    ".pdf", ".doc", ".odt", ".rtf", ".epub",
    ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp",
}
BOOK_ASSET_DIRECTORIES = {"images", "media", "__pycache__", ".git"}
QUESTION_HEADING = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:(?:question|q)\s*)?"
    r"(\d{1,3})\s*[\).:]\s+\S.*$"
)
BOOK_SECTION_HEADING = re.compile(
    r"(?im)^\s*(?:#{1,6}\s+\S.*|"
    r"(?:chapter|unit|section|part)\s+(?:\d+|[ivxlcdm]+)(?:[.: -]\s*.*|$))$"
)
TOKEN = re.compile(r"[a-z0-9]+")

# The aliases are intentionally short and inspectable. Expand them only after
# checking false positives against representative source material.
ALIASES: dict[str, tuple[str, ...]] = {
    "math:dimensions": ("dimensional analysis", "units", "dimension"),
    "math:scalars-vectors": ("vector", "component", "magnitude", "direction"),
    "math:geometry": ("geometry", "coordinate", "circle", "triangle"),
    "math:trigonometry": ("trigonometry", "trigonometric", "sine", "cosine", "tangent"),
    "math:graphs": ("graph", "plot", "slope", "intercept"),
    "math:derivatives": ("derivative", "differentiate", "rate of change"),
    "math:integrals": ("integral", "integrate", "area under"),
    "math:linear-systems": ("linear system", "simultaneous equation", "gaussian elimination"),
    "math:matrices": ("matrix", "matrices", "row reduction"),
    "math:linear-maps": ("linear map", "linear transformation", "change of basis"),
    "math:eigenmodes": ("eigenvalue", "eigenvector", "eigenmode", "normal mode"),
    "math:least-squares": ("least squares", "regression", "overdetermined"),
    "math:fourier": ("fourier", "frequency component", "fourier series"),
    "math:complex-numbers": ("complex number", "phasor", "imaginary"),
    "math:probability": ("probability", "random variable", "distribution"),
    "math:optimization": ("optimization", "maximum", "minimum", "extremum"),
    "physics:units_measurement": ("measurement", "significant figures", "dimensional consistency"),
    "physics:kinematics": ("kinematics", "displacement", "velocity", "acceleration", "projectile"),
    "physics:laws_of_motion": ("newton law", "force", "momentum", "free body"),
    "physics:work_energy": ("work energy", "kinetic energy", "potential energy", "power"),
    "physics:rotation": ("rotation", "torque", "angular momentum", "moment of inertia"),
    "physics:gravitation": ("gravitation", "gravity", "gravitational", "orbit"),
    "physics:properties_of_matter": ("elasticity", "viscosity", "fluid", "buoyancy", "pressure"),
    "physics:thermodynamics": ("thermodynamics", "heat engine", "entropy", "first law"),
    "physics:kinetic_theory": ("kinetic theory", "ideal gas", "molecular motion"),
    "physics:oscillations_waves": ("oscillation", "simple harmonic", "wave", "frequency", "wavelength"),
    "physics:electrostatics": ("electrostatics", "electric field", "electric potential", "coulomb"),
    "physics:capacitance": ("capacitance", "capacitor", "dielectric"),
    "physics:current_electricity": ("current electricity", "circuit", "resistance", "kirchhoff"),
    "physics:magnetism": ("magnetism", "magnetic field", "lorentz force"),
    "physics:em_induction": ("electromagnetic induction", "faraday law", "inductance", "alternating current"),
    "physics:electromagnetic_waves": ("electromagnetic wave", "maxwell equation"),
    "physics:optics": ("optics", "refraction", "reflection", "interference", "diffraction", "lens"),
    "physics:modern_physics": ("modern physics", "photoelectric", "quantum", "photon"),
    "physics:atoms_nuclei": ("atomic nucleus", "radioactive", "nuclear", "decay constant"),
    "physics:semiconductors": ("semiconductor", "diode", "transistor", "logic gate"),
    "chemistry:stoichiometry": ("stoichiometry", "mole concept", "limiting reagent", "balanced equation"),
    "chemistry:atomic_structure": ("atomic structure", "electron configuration", "quantum number", "orbital"),
    "chemistry:periodicity": ("periodic trend", "periodic table", "electronegativity", "ionization energy"),
    "chemistry:bonding": ("chemical bond", "covalent", "ionic bond", "molecular geometry", "hybridization"),
    "chemistry:states_of_matter": ("states of matter", "gas law", "kinetic molecular", "real gas"),
    "chemistry:thermodynamics": ("chemical thermodynamics", "enthalpy", "gibbs energy", "chemical entropy"),
    "chemistry:equilibrium": ("chemical equilibrium", "equilibrium constant", "le chatelier", "buffer solution"),
    "chemistry:kinetics": ("chemical kinetics", "reaction rate", "rate law", "activation energy"),
    "chemistry:solutions": ("solution concentration", "molarity", "molality", "colligative property"),
    "chemistry:electrochemistry": ("electrochemistry", "electrochemical cell", "redox", "nernst equation"),
    "chemistry:organic": ("organic chemistry", "functional group", "isomer", "nucleophile", "substitution reaction"),
}


@dataclass(frozen=True)
class SourceRow:
    row_id: str
    text: str


@dataclass(frozen=True)
class SolutionRoute:
    concept_id: str
    engine_id: str
    capability_id: str
    required_input_schema: str
    solution_approach: str
    visual_approach: str
    visual_status: str
    narration_approach: str
    narration_status: str
    readiness: str


def _extract_docx(path: Path) -> str:
    try:
        with ZipFile(path) as archive:
            document = ElementTree.fromstring(archive.read("word/document.xml"))
    except (OSError, KeyError, BadZipFile, ElementTree.ParseError) as exc:
        raise DataValidationError(f"cannot read DOCX {path}: {exc}") from exc
    paragraphs: list[str] = []
    for paragraph in document.iter():
        if paragraph.tag.rsplit("}", 1)[-1] == "p":
            text = "".join(
                node.text or ""
                for node in paragraph.iter()
                if node.tag.rsplit("}", 1)[-1] == "t"
            )
            if text.strip():
                paragraphs.append(text)
    return "\n".join(paragraphs)


def _read_text(path: Path) -> str:
    try:
        if path.suffix.lower() == ".docx":
            return _extract_docx(path)
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise DataValidationError(f"cannot read input {path}: {exc}") from exc


def _discover(
    directory: Path, *, ignore_book_assets: bool = False
) -> tuple[list[Path], list[str]]:
    if not directory.is_dir():
        raise DataValidationError(f"input directory does not exist: {directory}")
    supported: list[Path] = []
    unsupported: list[str] = []
    for path in sorted(directory.rglob("*")):
        if ignore_book_assets and any(
            part.casefold() in BOOK_ASSET_DIRECTORIES
            for part in path.relative_to(directory).parts[:-1]
        ):
            continue
        if (
            not path.is_file()
            or path.name.startswith("~$")
            or path.name.lower() == "readme.md"
        ):
            continue
        if path.suffix.lower() in SUPPORTED_SUFFIXES:
            supported.append(path)
        elif path.suffix.lower() == ".pdf":
            converted = path.with_suffix(".md")
            if not converted.is_file() or converted.stat().st_mtime < path.stat().st_mtime:
                unsupported.append(path.relative_to(directory).as_posix())
        elif path.suffix.lower() in UNSUPPORTED_DOCUMENT_SUFFIXES:
            unsupported.append(path.relative_to(directory).as_posix())
    return supported, unsupported


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def _split_questions(path: Path, root: Path, text: str) -> list[SourceRow]:
    headings = list(QUESTION_HEADING.finditer(text))
    if not headings:
        chunks = [text.strip()] if text.strip() else []
    else:
        chunks = [
            text[heading.start() : headings[index + 1].start() if index + 1 < len(headings) else len(text)].strip()
            for index, heading in enumerate(headings)
        ]
    relative_path = path.relative_to(root).as_posix()
    prefix = _slug(relative_path)
    return [
        SourceRow(f"{prefix}-q{index:03d}", chunk)
        for index, chunk in enumerate(chunks, start=1)
    ]


def _split_book_sections(path: Path, root: Path, text: str) -> list[SourceRow]:
    headings = list(BOOK_SECTION_HEADING.finditer(text))
    if not headings:
        sections = [text.strip()] if text.strip() else []
    else:
        sections = []
        preamble = text[: headings[0].start()].strip()
        if preamble:
            sections.append(preamble)
        sections.extend(
            text[
                heading.start() :
                headings[index + 1].start() if index + 1 < len(headings) else len(text)
            ].strip()
            for index, heading in enumerate(headings)
        )
    prefix = _slug(path.relative_to(root).as_posix())
    return [
        SourceRow(f"{prefix}-s{index:03d}", section)
        for index, section in enumerate(sections, start=1)
    ]


def _terms_for(concept_id: str, concept_name: str) -> tuple[str, ...]:
    values = [concept_name, *ALIASES.get(concept_id, ())]
    unique: list[str] = []
    for value in values:
        normalized = " ".join(TOKEN.findall(value.lower()))
        if normalized and normalized not in unique:
            unique.append(normalized)
    return tuple(unique)


def _concept_evidence(text: str, graph: ConceptGraph) -> dict[str, dict]:
    normalized = " ".join(TOKEN.findall(text.lower()))
    evidence: dict[str, dict] = {}
    for concept in graph.concepts:
        concept_name = " ".join(TOKEN.findall(concept.concept_name.lower()))
        aliases = _terms_for(concept.concept_id, concept.concept_name)
        matched: list[tuple[str, float]] = []
        for term in aliases:
            if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", normalized):
                weight = 1.5 if term == concept_name else (1.0 if " " in term else 0.4)
                matched.append((term, weight))
        if matched:
            evidence[concept.concept_id] = {
                "phrases": [term for term, _ in matched],
                "score": max(weight for _, weight in matched)
                + 0.15 * (len(matched) - 1),
            }
    return evidence


def match_concepts(text: str, graph: ConceptGraph) -> dict[str, dict]:
    """Return inspectable keyword evidence for concepts mentioned in text."""
    return _concept_evidence(text, graph)


def _score_matrix(
    rows: Sequence[SourceRow], concept_ids: Sequence[str], graph: ConceptGraph
) -> tuple[list[list[float]], list[dict[str, dict]]]:
    matrix: list[list[float]] = []
    evidence_rows: list[dict[str, dict]] = []
    for row in rows:
        evidence = _concept_evidence(row.text, graph)
        scale = max((item["score"] for item in evidence.values()), default=0.0)
        matrix.append(
            [
                evidence.get(concept_id, {}).get("score", 0.0) / scale if scale else 0.0
                for concept_id in concept_ids
            ]
        )
        evidence_rows.append(evidence)
    return matrix, evidence_rows


def _load_solution_routes(path: Path, graph: ConceptGraph) -> tuple[SolutionRoute, ...]:
    fields = (
        "concept_id",
        "engine_id",
        "capability_id",
        "required_input_schema",
        "solution_approach",
        "visual_approach",
        "visual_status",
        "narration_approach",
        "narration_status",
        "readiness",
    )
    allowed_statuses = {"available", "planned", "unavailable"}
    concepts = graph.by_id()
    routes: list[SolutionRoute] = []
    seen: set[tuple[str, str]] = set()
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != fields:
                raise DataValidationError(
                    f"{path}: expected columns in this order: {', '.join(fields)}"
                )
            for line, row in enumerate(reader, start=2):
                if None in row or any(value is None for value in row.values()):
                    raise DataValidationError(f"{path}:{line}: malformed route row")
                normalized = {key: value.strip() for key, value in row.items()}
                if any(not value for value in normalized.values()):
                    raise DataValidationError(f"{path}:{line}: route fields cannot be blank")
                route = SolutionRoute(**normalized)
                if route.concept_id not in concepts:
                    raise DataValidationError(
                        f"{path}:{line}: unknown concept_id {route.concept_id!r}"
                    )
                if route.visual_status not in allowed_statuses or route.narration_status not in allowed_statuses:
                    raise DataValidationError(
                        f"{path}:{line}: output status must be one of "
                        + ", ".join(sorted(allowed_statuses))
                    )
                key = (route.concept_id, route.capability_id)
                if key in seen:
                    raise DataValidationError(f"{path}:{line}: duplicate solution route")
                seen.add(key)
                routes.append(route)
    except (OSError, UnicodeError, csv.Error) as exc:
        raise DataValidationError(f"cannot read solution routes {path}: {exc}") from exc
    return tuple(routes)


def analyze_question(text: str, graph: ConceptGraph, routes: Sequence[SolutionRoute]) -> dict:
    concept_ids = [concept.concept_id for concept in graph.concepts]
    concepts = graph.by_id()
    direct, evidence_rows = _score_matrix((SourceRow("question", text),), concept_ids, graph)
    direct_scores = direct[0]
    position = {concept_id: index for index, concept_id in enumerate(concept_ids)}
    transform = [
        [float(row == column) for column in range(len(concept_ids))]
        for row in range(len(concept_ids))
    ]
    for link in graph.links:
        source, target = position[link.source_id], position[link.target_id]
        weight = 0.65 if link.relation == "requires" else 0.8
        transform[source][target] += weight
    propagated = _multiply((direct_scores,), transform)[0]
    propagated_scale = max(propagated, default=0.0)
    if propagated_scale:
        propagated = [value / propagated_scale for value in propagated]

    ranked = []
    for index, concept_id in enumerate(concept_ids):
        if direct_scores[index] == 0 and propagated[index] == 0:
            continue
        score = 0.75 * direct_scores[index] + 0.25 * propagated[index]
        ranked.append(
            {
                "concept_id": concept_id,
                "concept_name": concepts[concept_id].concept_name,
                "domain": concepts[concept_id].domain,
                "direct_score": round(direct_scores[index], 4),
                "graph_score": round(propagated[index], 4),
                "ranking_score": round(score, 4),
                "matched_phrases": evidence_rows[0].get(concept_id, {}).get("phrases", []),
                "match_type": "direct" if direct_scores[index] else "graph-related",
            }
        )
    ranked.sort(key=lambda item: (-item["ranking_score"], item["concept_id"]))
    top_routes = []
    route_index: dict[str, list[SolutionRoute]] = {}
    for route in routes:
        route_index.setdefault(route.concept_id, []).append(route)
    for match in ranked:
        for route in route_index.get(match["concept_id"], ()):
            top_routes.append(
                {
                    "concept_id": route.concept_id,
                    "capability_id": route.capability_id,
                    "engine_id": route.engine_id,
                    "readiness": route.readiness,
                    "required_input_schema": route.required_input_schema,
                    "solution_approach": route.solution_approach,
                    "visual_approach": route.visual_approach,
                    "visual_status": route.visual_status,
                    "narration_approach": route.narration_approach,
                    "narration_status": route.narration_status,
                }
            )
    score_gap = (
        ranked[0]["ranking_score"] - ranked[1]["ranking_score"]
        if len(ranked) > 1
        else (ranked[0]["ranking_score"] if ranked else 0.0)
    )
    if not ranked:
        match_status = "no-concept-match"
    elif ranked[0]["direct_score"] == 0:
        match_status = "graph-only-review-required"
    elif score_gap >= 0.25 and ranked[0]["direct_score"] >= 0.7:
        match_status = "clear-candidate-review-required"
    else:
        match_status = "ambiguous-review-required"
    return {
        "status": match_status,
        "scores_are_probabilities": False,
        "score_note": (
            "Scores rank evidence within this question; they are not calibrated "
            "probabilities of correctness."
        ),
        "concepts": ranked,
        "solution_routes": top_routes,
        "automatic_solution": False,
    }


def _multiply(left: Sequence[Sequence[float]], right: Sequence[Sequence[float]]) -> list[list[float]]:
    if not left or not right or len(left[0]) != len(right):
        raise DataValidationError("matrix dimensions do not align for concept propagation")
    return [
        [
            sum(left[row][inner] * right[inner][column] for inner in range(len(right)))
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def _matrix(row_labels: Sequence[str], column_labels: Sequence[str], values: list[list[float]]) -> dict:
    return {
        "row_labels": list(row_labels),
        "column_labels": list(column_labels),
        "values": values,
        "shape": [len(row_labels), len(column_labels)],
    }


def _prefer_docx_over_converted_copy(paths: Sequence[Path]) -> list[Path]:
    priority = {".docx": 0, ".mmd": 1, ".md": 2, ".txt": 3}
    chosen: dict[tuple[Path, str], Path] = {}
    for path in paths:
        key = (path.parent, path.stem.casefold())
        current = chosen.get(key)
        if current is None or priority[path.suffix.lower()] < priority[current.suffix.lower()]:
            chosen[key] = path
    return sorted(chosen.values())


def build_network(exam_papers_dir: Path, books_dir: Path) -> tuple[dict, list[str]]:
    topics = load_topics(ROOT / "data" / "physics_topics.csv")
    graph = load_graph(
        ROOT / "knowledge" / "concepts.csv",
        ROOT / "knowledge" / "links.csv",
        topics,
    )
    routes = _load_solution_routes(ROUTES_PATH, graph)
    paper_paths, unsupported_papers = _discover(exam_papers_dir)
    book_paths, unsupported_books = _discover(books_dir, ignore_book_assets=True)
    book_paths = _prefer_docx_over_converted_copy(book_paths)
    input_errors: list[dict[str, str]] = []
    questions: list[SourceRow] = []
    indexed_paper_files = 0
    for path in paper_paths:
        relative_path = path.relative_to(exam_papers_dir).as_posix()
        try:
            text = _read_text(path)
        except DataValidationError as exc:
            input_errors.append(
                {"path": relative_path, "error": str(exc).replace(str(path), relative_path)}
            )
            continue
        indexed_paper_files += 1
        questions.extend(_split_questions(path, exam_papers_dir, text))
    books: list[SourceRow] = []
    indexed_book_files = 0
    for path in book_paths:
        relative_path = path.relative_to(books_dir).as_posix()
        try:
            text = _read_text(path)
        except DataValidationError as exc:
            input_errors.append(
                {"path": f"book/{relative_path}", "error": str(exc).replace(str(path), relative_path)}
            )
            continue
        indexed_book_files += 1
        books.extend(_split_book_sections(path, books_dir, text))
    if not questions and not books:
        detail = "; ".join(
            f"{item['path']}: {item['error']}" for item in input_errors
        )
        message = "no readable exam questions or study books were found"
        raise DataValidationError(f"{message}: {detail}" if detail else message)

    concept_ids = [concept.concept_id for concept in graph.concepts]
    question_direct, _ = _score_matrix(questions, concept_ids, graph)
    book_direct, _ = _score_matrix(books, concept_ids, graph)
    requires = [[0.0 for _ in concept_ids] for _ in concept_ids]
    uses_math = [[0.0 for _ in concept_ids] for _ in concept_ids]
    positions = {concept_id: index for index, concept_id in enumerate(concept_ids)}
    for link in graph.links:
        source, target = positions[link.source_id], positions[link.target_id]
        if link.relation == "requires":
            requires[source][target] = 0.65
        else:
            uses_math[source][target] = 0.8
    propagation = [
        [
            (1.0 if row == column else 0.0)
            + requires[row][column]
            + uses_math[row][column]
            for column in range(len(concept_ids))
        ]
        for row in range(len(concept_ids))
    ]
    linked_questions = _multiply(question_direct, propagation) if questions else []
    linked_books = _multiply(book_direct, propagation) if books else []
    question_analyses = [
        {
            "question_id": question.row_id,
            "analysis": analyze_question(question.text, graph, routes),
        }
        for question in questions
    ]

    engine_ids = tuple(
        dict.fromkeys(
            (
                "math_engine",
                "physics_engine",
                "chemistry_engine",
                *(route.engine_id for route in routes),
            )
        )
    )
    engine_matrix = [[0.0 for _ in engine_ids] for _ in concept_ids]
    engine_positions = {engine_id: index for index, engine_id in enumerate(engine_ids)}
    for route in routes:
        engine_matrix[positions[route.concept_id]][engine_positions[route.engine_id]] = 1.0

    active_engines = {
        engine_id: {
            "available": any(route.engine_id == engine_id for route in routes),
            "supported": [
                route.capability_id for route in routes if route.engine_id == engine_id
            ],
        }
        for engine_id in engine_ids
    }
    active_engines["chemistry_engine"]["available"] = any(
        route.engine_id == "chemistry_engine" for route in routes
    )
    active_engines["animation_engine"] = {
        "available": any(route.visual_status == "available" for route in routes),
        "supported": [
            route.visual_approach for route in routes if route.visual_status == "available"
        ],
    }
    active_engines["narration_draft"] = {
        "available": any(route.narration_status == "available" for route in routes),
        "supported": [
            route.narration_approach
            for route in routes
            if route.narration_status == "available"
        ],
    }
    active_engines["visuals"] = {
        "available": any(route.visual_status == "available" for route in routes),
        "supported": [
            route.visual_approach for route in routes if route.visual_status == "available"
        ],
    }
    active_engines["audio_render"] = {"available": False, "supported": []}
    output_ids = ("animation_engine", "narration_draft", "visuals", "audio_render")
    output_matrix: list[list[float]] = []
    for concept_id in concept_ids:
        concept_routes = [route for route in routes if route.concept_id == concept_id]
        output_matrix.append(
            [
                float(any(route.visual_status == "available" for route in concept_routes)),
                float(any(route.narration_status == "available" for route in concept_routes)),
                float(any(route.visual_status == "available" for route in concept_routes)),
                0.0,
            ]
        )
    capability_ids = tuple(dict.fromkeys(route.capability_id for route in routes))
    capability_matrix = [[0.0 for _ in capability_ids] for _ in concept_ids]
    capability_positions = {capability_id: index for index, capability_id in enumerate(capability_ids)}
    for route in routes:
        capability_matrix[positions[route.concept_id]][capability_positions[route.capability_id]] = 1.0

    unsupported = [
        *(f"exam_papers/{path}" for path in unsupported_papers),
        *(f"book/{path}" for path in unsupported_books),
    ]
    return (
        {
            "schema_version": 1,
            "status": "partial-inputs" if input_errors or unsupported else "draft-concept-index",
            "limitations": [
                "Keyword matches are candidate links, not human-verified classifications.",
                "A concept match is not a parsed mathematical model or a solved answer.",
                "Only explicitly listed engine capabilities are implemented; unsupported routes are not run.",
                "Source text is processed locally and is not included in this output.",
            ],
            "counts": {
                "paper_files": len(paper_paths),
                "paper_files_indexed": indexed_paper_files,
                "questions": len(questions),
                "book_files": indexed_book_files,
                "book_files_seen": len(book_paths),
                "book_sections": len(books),
                "concepts": len(concept_ids),
                "unsupported_files": len(unsupported),
                "input_errors": len(input_errors),
            },
            "concepts": [
                {
                    "concept_id": concept.concept_id,
                    "name": concept.concept_name,
                    "domain": concept.domain,
                }
                for concept in graph.concepts
            ],
            "question_concept_matrix": _matrix(
                [question.row_id for question in questions], concept_ids, question_direct
            ),
            "question_linked_concept_matrix": _matrix(
                [question.row_id for question in questions], concept_ids, linked_questions
            ),
            "question_analyses": question_analyses,
            "book_concept_matrix": _matrix(
                [book.row_id for book in books], concept_ids, book_direct
            ),
            "book_linked_concept_matrix": _matrix(
                [book.row_id for book in books], concept_ids, linked_books
            ),
            "concept_requires_matrix": _matrix(concept_ids, concept_ids, requires),
            "concept_uses_math_matrix": _matrix(concept_ids, concept_ids, uses_math),
            "concept_to_solver_matrix": _matrix(concept_ids, engine_ids, engine_matrix),
            "concept_to_capability_matrix": _matrix(
                concept_ids, capability_ids, capability_matrix
            ),
            "concept_to_output_matrix": _matrix(concept_ids, output_ids, output_matrix),
            "solution_routes": [
                {
                    "concept_id": route.concept_id,
                    "engine_id": route.engine_id,
                    "capability_id": route.capability_id,
                    "required_input_schema": route.required_input_schema,
                    "solution_approach": route.solution_approach,
                    "visual_approach": route.visual_approach,
                    "visual_status": route.visual_status,
                    "narration_approach": route.narration_approach,
                    "narration_status": route.narration_status,
                    "readiness": route.readiness,
                }
                for route in routes
            ],
            "engine_capabilities": active_engines,
            "unsupported_files": unsupported,
            "input_errors": input_errors,
            "review_required": True,
        },
        unsupported,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Index exam papers and study books as linked concept matrices."
    )
    parser.add_argument("--exam-papers", type=Path, default=ROOT / "exam_papers")
    parser.add_argument("--books", type=Path, default=ROOT / "book")
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "matrix_network.json")
    question_input = parser.add_mutually_exclusive_group()
    question_input.add_argument(
        "--question",
        help="analyze one question string locally without adding its text to the output",
    )
    question_input.add_argument(
        "--question-file",
        type=Path,
        help="analyze one text, Markdown, or DOCX question file locally",
    )
    args = parser.parse_args(argv)
    try:
        if args.question is not None or args.question_file is not None:
            question_text = (
                args.question
                if args.question is not None
                else _read_text(args.question_file)
            )
            topics = load_topics(ROOT / "data" / "physics_topics.csv")
            graph = load_graph(
                ROOT / "knowledge" / "concepts.csv",
                ROOT / "knowledge" / "links.csv",
                topics,
            )
            routes = _load_solution_routes(ROUTES_PATH, graph)
            report = {
                "schema_version": 1,
                "status": "candidate-analysis",
                "question_analysis": analyze_question(question_text, graph, routes),
                "question_text_included": False,
                "review_required": True,
            }
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            print(f"Wrote question concept ranking to {args.output}")
            return 0
        report, unsupported = build_network(args.exam_papers, args.books)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    except (DataValidationError, OSError) as exc:
        print(f"matrix_pipeline: error: {exc}", file=sys.stderr)
        return 2
    print(
        f"Wrote {report['counts']['questions']} question rows and indexed "
        f"{report['counts']['book_sections']} book sections from "
        f"{report['counts']['book_files']} book files across "
        f"{report['counts']['concepts']} concepts to {args.output}"
    )
    input_errors = report["input_errors"]
    if unsupported or input_errors:
        print(
            f"matrix_pipeline: warning: {len(unsupported)} unsupported and "
            f"{len(input_errors)} invalid files were not indexed; see the output report",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
