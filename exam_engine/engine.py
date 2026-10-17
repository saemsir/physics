"""Load source-checked exam metadata and rank physics topics transparently."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
import math
from pathlib import Path
import random
from typing import Iterable

EXAMS = ("neet", "jee-main", "jee-advanced")
HISTORICAL_YEARS = 30
RECENCY_HALF_LIFE_YEARS = 8.0
DIRICHLET_PRIOR_MASS = 1.0
VIDEO_TOPIC_COUNT = 10
RIGHTS_STATUSES = {
    "metadata-only",
    "open-license",
    "permission-granted",
    "public-domain",
    "unknown",
}
REVIEW_STATUSES = {"pending", "verified", "disputed"}
REQUIRED_RECORD_FIELDS = (
    "question_id",
    "exam",
    "exam_name",
    "year",
    "session",
    "paper_id",
    "subject",
    "topic_id",
    "source_name",
    "source_url",
    "source_type",
    "rights_status",
    "rights_reference",
    "question_locator",
    "question_format",
    "difficulty",
    "marks",
    "answer_verified",
    "review_status",
    "reviewer",
    "reviewed_at",
    "notes",
)
REQUIRED_TOPIC_FIELDS = (
    "topic_id",
    "topic_name",
    "unit",
    "horizontal_angle",
    "vertical_hook",
)


class DataValidationError(ValueError):
    """Raised when source metadata cannot be safely interpreted."""


@dataclass(frozen=True)
class ExamRecord:
    question_id: str
    exam: str
    year: int
    session: str
    paper_id: str
    topic_id: str
    source_name: str
    source_url: str
    rights_status: str
    review_status: str

    @property
    def paper_key(self) -> tuple[str, int, str, str]:
        return (self.exam, self.year, self.session, self.paper_id)


@dataclass(frozen=True)
class Topic:
    topic_id: str
    topic_name: str
    unit: str
    horizontal_angle: str
    vertical_hook: str


@dataclass(frozen=True)
class Recommendation:
    topic: Topic
    historical_share: float
    question_records: int
    supported_papers: int
    total_papers: int
    basis: str


@dataclass(frozen=True)
class BacktestResult:
    years_evaluated: tuple[int, ...]
    papers_evaluated: int
    model_brier_score: float
    uniform_brier_score: float
    mean_top_ten_coverage: float


@dataclass(frozen=True)
class ForecastResult:
    exam: str
    target_year: int
    question_count: int
    simulation_count: int
    seed: int
    status: str
    model: str
    verified_question_records: int
    verified_papers: int
    first_verified_year: int | None
    last_verified_year: int | None
    topic_shares: tuple[Recommendation, ...]
    topic_appearance_probabilities: tuple[tuple[str, float], ...]
    sampled_topic_ids: tuple[str, ...]


def _read_csv(path: Path, required_fields: tuple[str, ...]) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames is None:
                raise DataValidationError(f"{path}: CSV has no header row")
            if tuple(reader.fieldnames) != required_fields:
                raise DataValidationError(
                    f"{path}: expected columns in this exact order: "
                    + ", ".join(required_fields)
                )
            rows = []
            for line_number, row in enumerate(reader, start=2):
                if None in row:
                    raise DataValidationError(
                        f"{path}:{line_number}: row has more values than columns"
                    )
                if all(not (value or "").strip() for value in row.values()):
                    continue
                if any(value is None for value in row.values()):
                    raise DataValidationError(
                        f"{path}:{line_number}: row has fewer values than columns"
                    )
                rows.append({key: value.strip() for key, value in row.items()})
            return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        raise DataValidationError(f"cannot read {path}: {exc}") from exc


def load_topics(path: Path) -> tuple[Topic, ...]:
    rows = _read_csv(path, REQUIRED_TOPIC_FIELDS)
    if len(rows) < VIDEO_TOPIC_COUNT:
        raise DataValidationError(
            f"{path}: topic catalog must contain at least {VIDEO_TOPIC_COUNT} topics"
        )
    topics: list[Topic] = []
    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        if any(not value for value in row.values()):
            raise DataValidationError(f"{path}:{line_number}: topic fields cannot be blank")
        if row["topic_id"] in seen:
            raise DataValidationError(
                f"{path}:{line_number}: duplicate topic_id {row['topic_id']!r}"
            )
        seen.add(row["topic_id"])
        topics.append(Topic(**row))
    return tuple(topics)


def _validate_record(
    row: dict[str, str],
    *,
    path: Path,
    line_number: int,
    topic_ids: set[str],
) -> ExamRecord:
    required = (
        "question_id",
        "exam",
        "year",
        "session",
        "paper_id",
        "subject",
        "topic_id",
        "source_name",
        "source_url",
        "source_type",
        "rights_status",
        "question_locator",
        "review_status",
    )
    missing = [field for field in required if not row[field]]
    if missing:
        raise DataValidationError(
            f"{path}:{line_number}: required fields are blank: {', '.join(missing)}"
        )
    if row["exam"] not in EXAMS:
        raise DataValidationError(
            f"{path}:{line_number}: exam must be one of {', '.join(EXAMS)}"
        )
    if row["subject"].casefold() != "physics":
        raise DataValidationError(f"{path}:{line_number}: only Physics rows are supported")
    if row["topic_id"] not in topic_ids:
        raise DataValidationError(
            f"{path}:{line_number}: unknown topic_id {row['topic_id']!r}"
        )
    if row["rights_status"] not in RIGHTS_STATUSES:
        raise DataValidationError(
            f"{path}:{line_number}: invalid rights_status {row['rights_status']!r}"
        )
    if row["rights_status"] in {
        "open-license",
        "permission-granted",
        "public-domain",
    } and not row["rights_reference"]:
        raise DataValidationError(
            f"{path}:{line_number}: {row['rights_status']} requires rights_reference"
        )
    if row["review_status"] not in REVIEW_STATUSES:
        raise DataValidationError(
            f"{path}:{line_number}: invalid review_status {row['review_status']!r}"
        )
    if not row["source_url"].startswith(("https://", "http://")):
        raise DataValidationError(
            f"{path}:{line_number}: source_url must be an http(s) URL"
        )
    try:
        year = int(row["year"])
    except ValueError as exc:
        raise DataValidationError(
            f"{path}:{line_number}: year must be a four-digit calendar year"
        ) from exc
    if not 1900 <= year <= date.today().year:
        raise DataValidationError(f"{path}:{line_number}: year is outside the supported range")
    return ExamRecord(
        question_id=row["question_id"],
        exam=row["exam"],
        year=year,
        session=row["session"],
        paper_id=row["paper_id"],
        topic_id=row["topic_id"],
        source_name=row["source_name"],
        source_url=row["source_url"],
        rights_status=row["rights_status"],
        review_status=row["review_status"],
    )


def _verified_records(
    path: Path,
    topics: Iterable[Topic],
    *,
    exam: str,
    as_of_year: int,
    first_year: int | None = None,
) -> tuple[ExamRecord, ...]:
    if exam not in EXAMS:
        raise DataValidationError(f"exam must be one of {', '.join(EXAMS)}")
    if not 1900 <= as_of_year <= date.today().year:
        raise DataValidationError("as_of_year must be a valid past or current calendar year")
    topic_ids = {topic.topic_id for topic in topics}
    rows = _read_csv(path, REQUIRED_RECORD_FIELDS)
    records = []
    question_ids: set[str] = set()
    if first_year is None:
        first_year = as_of_year - HISTORICAL_YEARS + 1
    for line_number, row in enumerate(rows, start=2):
        record = _validate_record(
            row,
            path=path,
            line_number=line_number,
            topic_ids=topic_ids,
        )
        if record.question_id in question_ids:
            raise DataValidationError(
                f"{path}:{line_number}: duplicate question_id {record.question_id!r}"
            )
        question_ids.add(record.question_id)
        if (
            record.exam == exam
            and record.review_status == "verified"
            and first_year <= record.year <= as_of_year
        ):
            records.append(record)
    return tuple(records)


def _rank_records(
    records: tuple[ExamRecord, ...],
    topics: tuple[Topic, ...],
    *,
    as_of_year: int,
) -> tuple[Recommendation, ...]:
    if not records:
        return tuple(
            Recommendation(
                topic=topic,
                historical_share=1 / len(topics),
                question_records=0,
                supported_papers=0,
                total_papers=0,
                basis="uniform-curriculum-baseline",
            )
            for topic in topics
        )

    papers: dict[tuple[str, int, str, str], dict[str, int]] = {}
    topic_record_counts = {topic.topic_id: 0 for topic in topics}
    topic_papers = {topic.topic_id: set() for topic in topics}
    for record in records:
        counts = papers.setdefault(record.paper_key, {})
        counts[record.topic_id] = counts.get(record.topic_id, 0) + 1
        topic_record_counts[record.topic_id] += 1
        topic_papers[record.topic_id].add(record.paper_key)

    evidence = {topic.topic_id: 0.0 for topic in topics}
    total_weight = 0.0
    for paper_key, counts in papers.items():
        _, year, _, _ = paper_key
        age = as_of_year - year
        weight = math.exp(-math.log(2) * age / RECENCY_HALF_LIFE_YEARS)
        question_total = sum(counts.values())
        for topic_id, count in counts.items():
            evidence[topic_id] += weight * count / question_total
        total_weight += weight

    prior = DIRICHLET_PRIOR_MASS
    denominator = prior * len(topics) + total_weight
    return tuple(
        Recommendation(
            topic=topic,
            historical_share=(prior + evidence[topic.topic_id]) / denominator,
            question_records=topic_record_counts[topic.topic_id],
            supported_papers=len(topic_papers[topic.topic_id]),
            total_papers=len(papers),
            basis="recency-weighted-historical-paper-mix",
        )
        for topic in topics
    )


def load_recommendations(
    data_path: Path,
    topics: tuple[Topic, ...],
    *,
    exam: str,
    as_of_year: int,
) -> tuple[Recommendation, ...]:
    """Rank topics using a smoothed, recency-weighted historical paper mix.

    The normalized shares describe the observed dataset, not the chance of a
    topic appearing on a future paper. Each distinct paper contributes one
    normalized topic distribution so differences in paper question counts do
    not dominate. A symmetric Dirichlet prior supplies a uniform baseline.
    """
    records = _verified_records(
        data_path,
        topics,
        exam=exam,
        as_of_year=as_of_year,
    )
    return _rank_records(records, topics, as_of_year=as_of_year)


def forecast_test(
    data_path: Path,
    topics: tuple[Topic, ...],
    *,
    exam: str = "jee-advanced",
    target_year: int | None = None,
    question_count: int = 10,
    simulations: int = 10_000,
    seed: int = 2026,
) -> ForecastResult:
    """Sample a physics practice-test topic blueprint from verified history.

    Topic shares are smoothed historical paper mixtures, not calibrated chances
    of exact questions appearing on a future exam. The sample is a topic-only
    practice blueprint and does not reproduce an official exam format.
    """
    if target_year is None:
        target_year = date.today().year
    if not isinstance(question_count, int) or isinstance(question_count, bool) or not 1 <= question_count <= 200:
        raise DataValidationError("question_count must be an integer from 1 to 200")
    if not isinstance(simulations, int) or isinstance(simulations, bool) or not 100 <= simulations <= 100_000:
        raise DataValidationError("simulations must be an integer from 100 to 100000")
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise DataValidationError("seed must be an integer")
    if not topics:
        raise DataValidationError("topic catalog must contain at least one topic")

    records = _verified_records(
        data_path,
        topics,
        exam=exam,
        as_of_year=target_year,
        first_year=1900,
    )
    shares = _rank_records(records, topics, as_of_year=target_year)
    probabilities = [item.historical_share for item in shares]
    cumulative: list[float] = []
    running_total = 0.0
    for probability in probabilities:
        running_total += probability
        cumulative.append(running_total)
    cumulative[-1] = 1.0

    rng = random.Random(seed)
    appearances = [0] * len(topics)
    sampled_topics: list[str] = []
    for simulation in range(simulations):
        seen: set[int] = set()
        for _ in range(question_count):
            draw = rng.random()
            index = next(
                (position for position, boundary in enumerate(cumulative) if draw < boundary),
                len(cumulative) - 1,
            )
            seen.add(index)
            if simulation == 0:
                sampled_topics.append(topics[index].topic_id)
        for index in seen:
            appearances[index] += 1

    paper_keys = {record.paper_key for record in records}
    years = [record.year for record in records]
    return ForecastResult(
        exam=exam,
        target_year=target_year,
        question_count=question_count,
        simulation_count=simulations,
        seed=seed,
        status=(
            "historical-data-informed"
            if records
            else "prior-only-no-verified-exam-records"
        ),
        model=(
            "8-year-half-life paper-normalized topic shares with symmetric "
            "Dirichlet smoothing; seeded categorical Monte Carlo"
        ),
        verified_question_records=len(records),
        verified_papers=len(paper_keys),
        first_verified_year=min(years) if years else None,
        last_verified_year=max(years) if years else None,
        topic_shares=shares,
        topic_appearance_probabilities=tuple(
            (topic.topic_id, appearances[index] / simulations)
            for index, topic in enumerate(topics)
        ),
        sampled_topic_ids=tuple(sampled_topics),
    )


def render_test_forecast(forecast: ForecastResult) -> dict[str, object]:
    """Return a JSON-compatible report without implying exact-question certainty."""
    topic_appearance = dict(forecast.topic_appearance_probabilities)
    return {
        "schema_version": 1,
        "exam": forecast.exam,
        "target_year": forecast.target_year,
        "scope": "Physics topic blueprint only; not an exact-question or full-exam prediction",
        "status": forecast.status,
        "model": forecast.model,
        "simulation": {
            "question_slots": forecast.question_count,
            "runs": forecast.simulation_count,
            "seed": forecast.seed,
        },
        "data_coverage": {
            "verified_question_records": forecast.verified_question_records,
            "verified_papers": forecast.verified_papers,
            "first_verified_year": forecast.first_verified_year,
            "last_verified_year": forecast.last_verified_year,
        },
        "limitations": [
            "Only human-verified source-linked records for the selected exam through the target year are used.",
            "JEE Main and historic IIT-JEE data are not pooled into JEE Advanced because exam formats and distributions differ.",
            "Topic shares and simulated test coverage are not calibrated probabilities of future questions.",
            "The sampled blueprint contains topic IDs only; it does not create, reproduce, or solve questions.",
            "Question count is user-selected and does not imply the official exam pattern.",
            (
                "No verified records were available; the output uses only a uniform prior and is not a data-driven forecast."
                if forecast.status == "prior-only-no-verified-exam-records"
                else "Historical coverage may be incomplete or inconsistent; validate forecasts with rolling-origin backtests."
            ),
        ],
        "topic_forecast": [
            {
                "topic_id": item.topic.topic_id,
                "topic_name": item.topic.topic_name,
                "estimated_historical_share": item.historical_share,
                "estimated_probability_present_in_sampled_test": topic_appearance[
                    item.topic.topic_id
                ],
                "verified_question_records": item.question_records,
                "verified_papers": item.supported_papers,
            }
            for item in forecast.topic_shares
        ],
        "sampled_practice_blueprint": [
            {"slot": index, "topic_id": topic_id}
            for index, topic_id in enumerate(forecast.sampled_topic_ids, start=1)
        ],
    }


def load_backtest(
    data_path: Path,
    topics: tuple[Topic, ...],
    *,
    exam: str,
    as_of_year: int,
) -> BacktestResult:
    """Evaluate prior-year topic distributions against later held-out papers."""
    all_records = _verified_records(
        data_path,
        topics,
        exam=exam,
        as_of_year=as_of_year,
        first_year=1900,
    )
    current_window_start = as_of_year - HISTORICAL_YEARS + 1
    years_evaluated: set[int] = set()
    model_scores: list[float] = []
    uniform_scores: list[float] = []
    top_ten_coverages: list[float] = []
    topic_ids = tuple(topic.topic_id for topic in topics)
    uniform_share = 1 / len(topics)

    target_years = sorted(
        {record.year for record in all_records if current_window_start <= record.year <= as_of_year}
    )
    for target_year in target_years:
        training_start = target_year - HISTORICAL_YEARS + 1
        training_records = tuple(
            record
            for record in all_records
            if training_start <= record.year < target_year
        )
        held_out = tuple(record for record in all_records if record.year == target_year)
        if not training_records or not held_out:
            continue
        ranking = _rank_records(training_records, topics, as_of_year=target_year - 1)
        predicted = {result.topic.topic_id: result.historical_share for result in ranking}
        top_topics = {
            result.topic.topic_id
            for result in sorted(ranking, key=lambda result: -result.historical_share)[
                :VIDEO_TOPIC_COUNT
            ]
        }
        paper_topic_counts: dict[tuple[str, int, str, str], dict[str, int]] = {}
        for record in held_out:
            counts = paper_topic_counts.setdefault(record.paper_key, {})
            counts[record.topic_id] = counts.get(record.topic_id, 0) + 1
        for counts in paper_topic_counts.values():
            total = sum(counts.values())
            actual = {topic_id: counts.get(topic_id, 0) / total for topic_id in topic_ids}
            model_scores.append(
                sum((predicted[topic_id] - actual[topic_id]) ** 2 for topic_id in topic_ids)
            )
            uniform_scores.append(
                sum((uniform_share - actual[topic_id]) ** 2 for topic_id in topic_ids)
            )
            top_ten_coverages.append(
                sum(actual[topic_id] for topic_id in top_topics)
            )
            years_evaluated.add(target_year)

    if not model_scores:
        raise DataValidationError(
            f"not enough verified {exam} records for a rolling-origin backtest; "
            "add at least one training year and a later held-out year"
        )
    return BacktestResult(
        years_evaluated=tuple(sorted(years_evaluated)),
        papers_evaluated=len(model_scores),
        model_brier_score=sum(model_scores) / len(model_scores),
        uniform_brier_score=sum(uniform_scores) / len(uniform_scores),
        mean_top_ten_coverage=sum(top_ten_coverages) / len(top_ten_coverages),
    )


def _ordered_recommendations(
    recommendations: tuple[Recommendation, ...],
) -> tuple[Recommendation, ...]:
    return tuple(
        sorted(
            recommendations,
            key=lambda result: -result.historical_share,
        )
    )


def render_video_batch(
    recommendations: tuple[Recommendation, ...],
    *,
    exam: str,
    as_of_year: int,
) -> str:
    """Render a repeatable batch of ten long-form and ten short-form briefs."""
    ranked = _ordered_recommendations(recommendations)
    selected = ranked[:VIDEO_TOPIC_COUNT]
    baseline = all(
        result.basis == "uniform-curriculum-baseline" for result in selected
    )
    years = f"{as_of_year - HISTORICAL_YEARS + 1}–{as_of_year}"
    lines = [
        f"# Physics video brief batch: {exam}",
        "",
        f"- **Generated for:** {as_of_year}",
        f"- **Historical window:** {years}",
        "- **Evidence note:** "
        + (
            "No verified records were found for this exam and window. This is "
            "a uniform curriculum-baseline topic list, not an evidence-based "
            "ranking or exam forecast."
            if baseline
            else "Topic shares summarize only the verified records in this "
            "dataset. They are not calibrated probabilities of future exam "
            "questions; use them as practice-planning evidence, not guarantees."
        ),
        "- **Editorial approach:** original visual-first explanation, physical "
        "intuition, explicit assumptions, and a checkable derivation. Create "
        "original examples and visuals; do not reproduce protected questions.",
        "",
        "## Horizontal videos — 16:9, approximately 3 minutes",
        "",
    ]
    for index, result in enumerate(selected, start=1):
        topic = result.topic
        lines.extend(
            [
                f"### H{index:02d}. {topic.topic_name}: see the structure",
                "",
                f"- **Core idea:** {topic.horizontal_angle}.",
                "- **Three-minute arc:** 0:00 pose a concrete puzzle; 0:20 draw "
                "the physical model; 0:55 derive the key relationship; 1:50 "
                "test a limiting case or misconception; 2:35 solve one "
                "original representative problem and recap.",
                "- **Visual plan:** begin with one uncluttered physical "
                "diagram; animate only the quantities that carry the argument; "
                "finish with a labelled check.",
                f"- **Exam connection:** build an original {exam} level "
                "problem around this concept and explain why the method works.",
                f"- **Historical support:** {result.question_records} "
                f"verified tagged records across {result.supported_papers} "
                f"papers; smoothed historical share "
                f"{result.historical_share:.1%} "
                f"({result.basis.replace('-', ' ')}).",
                "",
            ]
        )
    lines.extend(["## Vertical videos — 9:16, approximately 1 minute", ""])
    for index, result in enumerate(selected, start=1):
        topic = result.topic
        lines.extend(
            [
                f"### V{index:02d}. {topic.topic_name}: one fast insight",
                "",
                f"- **0–5 s hook:** {topic.vertical_hook}",
                "- **5–40 s:** show one diagram or example, state the governing "
                "principle, and make one inference visible.",
                "- **40–55 s check:** ask the learner to predict a sign, "
                "direction, limiting case, or next step before revealing it.",
                "- **55–60 s close:** summarize the reusable idea and invite "
                "the learner to try a fresh, original problem.",
                f"- **Evidence:** {result.question_records} verified tagged "
                f"records in {result.supported_papers} papers; historical "
                f"share {result.historical_share:.1%} "
                f"({result.basis.replace('-', ' ')}).",
                "",
            ]
        )
    return "\n".join(lines)
