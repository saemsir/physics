# Exam-question metadata

`exam_question_metadata.csv` is the normalized ledger used by the local
recommendation command. Local JEE Advanced PDFs have been cataloged and
machine-generated Physics topic candidates are present, but the candidate rows
are pending review and do not count as verified exam data. The repository
still has no independently verified, source-linked JEE Advanced question
dataset.

## One metadata row per question

Record only bibliographic and analytical metadata for copyrighted papers.
The schema intentionally has no question-text, answer-choice, solution, or
figure field. Full text may be kept in a separate, access-controlled source
only when the source is explicitly licensed for that use or written permission
is recorded. A public download link does not itself grant redistribution
rights.

- `exam`: `neet`, `jee-main`, or `jee-advanced`. Preserve legacy exam labels
  (for example, AIPMT or IIT-JEE) in `exam_name`; do not silently assume that
  historic formats are directly comparable to current exams.
- `year`, `session`, and `paper_id`: identify a distinct sitting/paper.
- `topic_id`: must match an ID in `physics_topics.csv`.
- `source_name`, `source_url`, and `source_type`: identify the exact official,
  publisher, or coaching-institute source and a stable public location.
- `rights_status` and `rights_reference`: record what is known about rights.
  `metadata-only` is suitable when the question itself is not licensed for
  redistribution; cite the license or permission for `open-license` and
  `permission-granted`, and document public-domain status and jurisdiction
  for `public-domain`.
- `question_locator`: give a question number or section/page locator, not the
  copied question.
- `review_status`: only `verified` rows with source and topic tags checked by
  a human contribute to recommendations. This is not a claim that the answer
  has been solved correctly.
- `answer_verified`, `reviewer`, `reviewed_at`, and `notes`: document
  educational review separately from source verification.

The intended historical window is the 30 calendar years ending with the
requested `--as-of-year` (1997–2026 when the as-of year is 2026). Availability
and exam continuity vary by exam; the tool does not invent or backfill missing
papers.

## Add data and run

From the repository root, add source-checked metadata rows, then run:

```bash
python tools/import_exam_candidates.py
python -m exam_engine recommend --exam jee-main
python -m exam_engine recommend --exam neet --as-of-year 2026 \
  --output output/neet-video-ideas.md
python -m exam_engine backtest --exam jee-advanced --as-of-year 2026
python -m exam_engine predict-test --exam jee-advanced --as-of-year 2026 \
  --questions 10 --simulations 10000 --seed 2026 \
  --output output/jee-advanced-physics-blueprint.json
```

The importer catalogs the local JEE Advanced PDF copies and extracts question
locators plus keyword-based topic candidates from their Markdown conversions.
It records only metadata, never question text. Source covers identify Career
Point on 28 copies; two 2025 copies have no publisher mark. Exact original
download URLs and paper integrity are not recorded, so paper records remain
`needs-source-review`; candidate topic rows remain `pending`, with unknown
rights and unverified answers. Duplicate copies are not double-counted.
Review the source, PDF, locator, and topic for each candidate before changing
its status to `verified`. The importer cannot certify that a source is
official, that a coaching answer is correct, or that a keyword match is the
right topic.
No local cover identifies Allen, Motion, PW, or NTA. JEE Advanced is conducted
by an IIT organizing institute; do not attribute these papers to NTA without
paper-specific evidence. Provide exact source links and file mappings to
replace the provisional attributions.

The command emits ten 16:9, approximately three-minute lesson briefs and ten
9:16, approximately one-minute lesson briefs. The brief uses original
visual-first explanation, physical intuition, and explicit reasoning; it is
not an imitation of another creator's scripts, artwork, or distinctive
presentation.

When no verified observations exist for an exam, the engine emits a clearly
labelled uniform curriculum-baseline batch rather than implying that historical
evidence exists. With data, it reports smoothed, recency-weighted shares of
the verified historical paper mix. These shares describe the supplied sample;
they are not calibrated probabilities that a topic or question will appear on
an upcoming exam. Use `backtest` to compare held-out historical papers with a
uniform-catalog baseline before relying on rankings.

`predict-test` uses the selected exam's verified metadata to create a seeded
Monte Carlo, topic-only Physics practice-test blueprint and estimates how often
each topic appears across simulated tests. It normalizes topic counts within
each paper, applies the same eight-year recency half-life and symmetric
Dirichlet smoothing, then samples topics from that distribution. JEE Main and
historic IIT-JEE rows are not mixed into JEE Advanced. The requested number of
question slots is a practice setting, not an official-paper pattern. The
reported shares and simulated coverage are not calibrated chances of exact
future questions; validate with the rolling-origin `backtest` command. When
there are no verified records, the CLI explicitly labels the output as
prior-only and warns that it is not a data-driven forecast.

## Ranking model and limitations

For each verified paper, count tagged questions by topic and normalize those
counts so that the paper contributes one topic-share distribution regardless
of its total question count. Give a paper from year `y` weight
`exp(-ln(2) * (as_of_year - y) / 8)`, an eight-year half-life. For `K` catalog
topics, add a symmetric prior mass of `1` to each topic and normalize:

`share(topic) = (1 + sum_p(weight(p) * paper_share(p, topic))) / (K + sum_p(weight(p)))`

This is an ensemble-inspired smoothing and recency scheme, not a physical
model of exam setters and not a forecast probability. The uniform prior keeps
the distribution normalized and makes unsupported topics visible instead of
assigning them an unjustified zero. Rank ties retain the curated topic-catalog
order. Each row still needs source and tag verification; no row in the current
ledger is populated.

`backtest` uses rolling-origin evaluation: each eligible year's verified
papers are held out, the ranking is recomputed using only earlier records in
that target year's prior 30-year window, and the topic distribution is scored
with multi-class Brier score against each held-out paper's normalized topic
mix. The uniform-catalog baseline is reported beside the model; lower Brier
score is better. Top-10 coverage is the share of held-out question tags in
the ten selected topics. Metrics can be unstable or biased when source
coverage is sparse or inconsistent; they do not establish calibrated
predictions of future papers.

The implementation follows a small, explicit computation pipeline: validate
the fixed record representation; group and normalize by paper; weight and
aggregate evidence; produce deterministic, inspectable briefs; and test edge
cases with synthetic fixtures that are never added to the real dataset. The
reference books inform broad principles of normalized uncertainty, finite
representations, information integrity, and verification; they do not provide
exam data or justify copying their text or figures.

Run focused checks with:

```bash
python -m unittest discover -s tests -v
```

## Source-linked content network

`sources.csv`, `papers.csv`, `questions.csv`, and `question_concepts.csv` are
the Git-versioned index inputs for the local SQLite network built with
`python -m content_engine init`. Question rows contain metadata and source
locators only, not copied question wording. The current JEE paper entries are
explicitly unreviewed local files; none are considered verified question
records. Follow [../docs/content_network.md](../docs/content_network.md) before
adding paper/question records or using a reference in generated content.
