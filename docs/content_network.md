# Content network and rendering workflow

## Source of truth and local database

Keep the network's versioned source data in Git:

- `data/sources.csv`: source identity, local path/URL, citation, rights status,
  and extraction quality.
- `data/papers.csv`: exam, year, paper identity, and source/review status. Old
  exams preserve their historical name instead of being relabelled as a modern
  exam.
- `data/questions.csv`: question locator, topic, and human review metadata;
  deliberately has no question-text or answer-choice column.
- `data/question_concepts.csv`: reviewed links from a question to any number of
  math and physics concepts.
- `data/concept_sources.csv`: concept-to-book/course references with section
  locators and independent source/rights review status.
- `knowledge/concepts.csv` and `knowledge/links.csv`: the concept graph.
- `data/content_schema.sql`: versioned relational schema and query view.

SQLite is a generated local index, not the collaboration source of truth.
Rebuild or refresh it after updating tracked records:

```bash
python -m content_engine init
python -m content_engine summary
python -m content_engine papers
python -m content_engine sources
python -m content_engine map-paper --paper-id iitjee-2008-1
python -m content_engine map-topic --topic kinematics
python -m content_engine recommend --exam jee-main
python -m content_engine backtest --exam jee-advanced
```

The default `data/saemphysics.sqlite` is ignored by Git. Commit schema changes,
catalog records, and review decisions; do not rely on a developer's local
database file being synchronized through GitHub. For team-scale concurrent
editing, move the same IDs, relationships, and migration discipline to a
managed server database rather than sharing a mutable SQLite file.

The imported 2007–2011 paper records are intentionally marked for source
review. The repository copies do not establish the original publisher, source
URL, redistribution rights, or question-answer correctness. The 2007 Paper 1
file is an invalid two-byte stub. Other papers are image-heavy; a Markdown
conversion does not make their questions machine-verified. Add one question
row only after a reviewer has recorded the exact paper locator, topic, source,
and review status. Keep copyrighted question text and figures out of public
metadata unless reuse rights explicitly allow it.

The Strang course, Feynman computation reference, and SICP conversion are
cataloged with rights or extraction status still requiring review. A concept
reference is a provenance pointer, not permission to quote or reproduce
source text. Generated lesson IR carries the reference and rights status so
the educator can choose and approve usable sources.

The `content_engine recommend` and `content_engine backtest` commands use the
same ranking and evaluation implementation as `exam_engine`, exporting only
verified records for supported modern exams with traceable source URLs. Legacy
IIT-JEE rows remain distinct until an explicit, reviewed exam-equivalence
policy is adopted.

## Problem-to-lesson integration example

The original (non-exam) fixture exercises the supported constant-acceleration
path end to end:

```bash
python -m content_engine solve --problem data/kinematics_demo.json
python -m content_engine compile-lesson --problem data/kinematics_demo.json
```

The typed solver calls `physics_engine`, checks the result with an independent
average-velocity displacement identity, and records an engine run. The lesson
compiler joins the model to source provenance and the existing math/physics
concept graph, then creates versioned renderer-neutral JSON. The animation
engine generates sampled physical coordinates; the Manim scene maps those
coordinates to screen coordinates. Computation passing is not a physics
approval: editorial, physics, design, render, and release gates stay pending.

Only explicitly supported models may execute. Unsupported model types,
malformed inputs, unknown sources/concepts, failed checks, or missing database
references stop the workflow rather than producing a success-shaped fallback.
Add new solver dispatch only with model-specific analytical tests, units,
assumptions, and failure cases.

## GitHub/Codespaces and Google Colab

Use Codespaces/GitHub for editing and review. Open
`notebooks/render_in_colab.ipynb` in Google Colab to clone a selected Git
revision, install Manim's pinned Python dependencies and system tools, rebuild
the disposable database, compile the lesson, and render a low-quality preview.
For a reproducible release candidate, set the notebook's `REVISION` to a
reviewed commit SHA rather than `main`. Colab outputs are temporary; keep only
small source artifacts and approvals in Git, and store large renders elsewhere.

Colab rendering is a documented workflow but must be exercised in a real
Colab runtime before relying on it for a release. The release process still
requires a complete render review and corrected captions/audio.
