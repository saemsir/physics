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

## Fixed 20-video batch workflow

`data/video_batches/batch_001.json` is an owner-approved-for-storyboarding
batch of ten original questions: five calculation problems and five concept
explainers. It links each item to the relevant Feynman section without copying
book questions, prose, or figures. The Feynman conversions have unknown rights
status; citations are research pointers, not permission to reuse their
material. The JEE scan catalog remains separate and contributes no unverified
exam questions. Owner approval here is not exam-source verification or final
physics/release approval.

Validate and expand the content into twenty render briefs:

```bash
python -m content_engine batch-plan
python -m content_engine batch-plan --output /tmp/batch_001_plan.json
```

The batch contract enforces 10 vertical 9:16 videos at 60 seconds and 10
horizontal 16:9 videos at 180 seconds, ages 14–21, mixed problem/concept
content, exact `Saem Physics` / `NEET JEE MIT` text branding, and timed
storyboard beats. Three constant-acceleration solutions are checked by the
existing physics engine. Collision and energy examples have independent
formula audits; those are not substitutes for physics-teacher approval. The
approved plan contains twenty render briefs. Render selected briefs with Manim;
the batch renderer verifies each MP4's dimensions and duration and writes a
SHA-256 report:

```bash
python tools/render_video_batch.py \
  --quality preview \
  --video-ids b001-e01-projectile-components-vertical \
               b001-e01-projectile-components-horizontal \
  --output-dir /tmp/batch_001_preview
python tools/render_video_batch.py \
  --quality high --formats vertical --resume \
  --output-dir /tmp/batch_001_vertical
python tools/render_video_batch.py \
  --quality high --formats horizontal --resume \
  --output-dir /tmp/batch_001_horizontal
```

The Manim template animates an original diagram for each concept/problem. The
current exports are silent, branded visual drafts with on-screen explanations;
they do not contain recorded narration, final captions, physics-release
approval, or the user's image logo. Finish these in post-production and review
all exports before release. `--resume` verifies and reuses completed videos
after an interrupted Colab session.

The owner approved English and the text-only brand lockup because no image
logo asset has been supplied. Provide an approved transparent PNG or SVG logo
before release rendering. The visual direction is original to Saem Physics
rather than an imitation of another creator. Add a recorded narration track,
correct captions, review all scenes, and obtain physics/release approval before
publishing.

## GitHub/Codespaces and Google Colab

Use Codespaces/GitHub for editing and review. Open
`notebooks/render_in_colab.ipynb` in Google Colab to clone a selected Git
revision, install Manim's pinned Python dependencies and system tools, rebuild
the disposable database, validate the reviewed batch, compile the lesson, and
render a low-quality preview. CI validates the audio profile metadata but does
not read voice recordings; see `docs/audio_profile.md` for the private
sample-analysis procedure.
For a reproducible release candidate, set the notebook's `REVISION` to a
reviewed commit SHA rather than `main`. Colab outputs are temporary; keep only
small source artifacts and approvals in Git, and store large renders elsewhere.

Colab rendering is a documented workflow but must be exercised in a real
Colab runtime before relying on it for a release. The release process still
requires a complete render review and corrected captions/audio.

For the step-by-step input procedure, narration guidance, current system
boundaries, specifications, and upgrade roadmap, see
[`video_production_architecture.md`](video_production_architecture.md).
