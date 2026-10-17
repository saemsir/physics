# SaemPhysics AI Animation Studio

An engineering workspace for producing original, visual physics lessons for
[SaemPhysics](https://www.youtube.com/@SaemPhysics). The first audience is NEET,
JEE Main/Advanced, and Olympiad students; explanations should also be useful to
curious learners beyond those exams.

The teacher owns the physics and pedagogy. AI assists with bounded tasks, code
makes visuals repeatable, Git records decisions, and explicit teacher approval
gates protect each lesson. Start with one correct, understandable scene; do
not try to automate a complete video from a single prompt.

## Production pipeline

| Stage | Input | Output | Approval |
|---|---|---|---|
| Editorial | Topic, learner, misconception | Brief and learning objective | Teacher: objective and central question |
| Physics | Claim and model | Assumptions, derivation, checks, sources | Teacher: physics and derivation |
| Design | Approved physics | Script, storyboard, scene cards | Teacher: explanation and visual encoding |
| Animation | Approved scene cards | Manim source and preview | Teacher: preview at normal speed |
| Post-production | Approved visuals and narration | Edited video, audio, corrected captions | Teacher: synchronization and accessibility |
| Release | Final export and source | QC-approved video and archived source | Teacher: final export and publication |

A correction at an earlier stage triggers a review of affected later stages.
AI output is a draft, not an approval.

## Repository map

```text
config/                  Shared visual identity
docs/                    Architecture, channel brief, source policy, visual teaching principles
episodes/                Episode-specific brief, physics, script and scenes
templates/               Brief, review, storyboard and release templates
book/                    Reference material; check source permissions before reuse
data/                    Exam-question metadata schema and physics topic catalog
content_engine/          Versioned SQLite index, provenance links and lesson compiler
studio_engine/           Versioned JSON coordinator for supported repository engines
exam_engine/             Evidence-labelled topic ranking and video-brief CLI
knowledge/               Validated concept graph across physics and mathematics
math_engine/              Deterministic linear algebra primitives
physics_engine/           Validated physics model functions
animation_engine/         Calculation-backed visual specifications
tests/                   Focused engine tests
```

The first sample is `episodes/vectors_001/`. Its status is a working draft:
the physics notes, storyboard and source scene are recorded, but the teacher
must still approve the lesson and inspect an actual render.
`episodes/laplace_001/` is a separate, source-grounded lesson-design pilot
that demonstrates the representation-bridge storyboard pattern; it is not
physics-approved or rendered yet.
Extract reusable components into `library/` after the first scene has been
reviewed and the repeated patterns are clear.

## Set up the environment

Use Python 3.11 or 3.12 with the pinned Manim Community Edition dependency.
Manim also needs system tools for rendering. Follow the
[official Manim installation guide](https://docs.manim.community/en/stable/installation.html)
for your operating system.

```bash
python --version
git --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
manim --version
```

Render a low-quality preview of the sample:

```bash
python -m manim -pql episodes/vectors_001/scenes.py VectorComponents
```

Watch the complete render at normal speed before approving it. Manim writes
generated media under `media/`; rendered exports and caches do not belong in
Git. See `docs/architecture.md` for reproducibility and the approval workflow.
See `docs/audio_profile.md` for the original narration direction and the
private, local voice-sample analysis procedure.

## Unified Studio coordinator

`studio_engine` is the portable, versioned JSON interface for running several
existing engines in one request. It records a run manifest and one JSON result
per task, supports deterministic seeds and explicit task dependencies, and
works anywhere the repository's Python dependencies are installed:

```bash
python -m studio_engine actions
python -m studio_engine validate --request config/studio_request.example.json
python -m studio_engine run --request config/studio_request.example.json
```

The request contract is documented in
[docs/studio_engine.md](docs/studio_engine.md) and
[schemas/studio_request.schema.json](schemas/studio_request.schema.json).
This is an orchestrator, not a new solver: it delegates to existing modules,
keeps review gates intact, and reports unsupported generation honestly.
In particular, it can plan audio but cannot synthesize or mix it; the batch
renderer makes silent visual drafts and is currently tied to its fixed Manim
scene. A task succeeding is not approval for academic correctness, rights,
accessibility, final rendering, or publication.
For audio, the coordinator can measure local PCM WAV technical properties and
include lesson sound-design guidance; it cannot synthesize or mix audio.

## Build exam-focused video briefs

The exam engine uses verified, source-linked question metadata to prioritize
physics topics and produce ten 16:9 three-minute and ten 9:16 one-minute
original video briefs:

```bash
python -m exam_engine recommend --exam jee-main
python -m exam_engine recommend --exam jee-advanced --as-of-year 2026 \
  --output output/jee-advanced-video-ideas.md
python -m exam_engine backtest --exam jee-main
python -m exam_engine predict-test --exam jee-advanced --as-of-year 2026 \
  --questions 10 --simulations 10000 --seed 2026 \
  --output output/jee-advanced-physics-blueprint.json
python -m exam_engine map-topic --topic electrostatics
python -m math_engine solve-linear --matrix '[[2,1],[1,3]]' --rhs '[5,7]'
python -m physics_engine constant-acceleration --position-m '[0,0]' \
  --velocity-m-per-s '[3,2]' --acceleration-m-per-s2 '[0,-9.8]' --time-s 1
python -m unittest discover -s tests -v
```

Start with `data/README.md` before adding records. The metadata ledger can
contain pending source and keyword-topic candidates, but only manually verified
records contribute to predictions; it does not contain copied exam text. With
no observations for a selected exam, the command labels its output as a uniform
curriculum baseline. With records, it reports smoothed historical topic shares,
not guaranteed or calibrated predictions of upcoming questions. Every proposed
explanation remains subject to source-rights, physics, and teacher review. Run
`backtest` to compare rolling-origin topic rankings with a uniform baseline
before using the results to prioritize study or video production.

`predict-test` samples a repeatable, topic-only Physics practice-test blueprint
using verified source-linked records for the selected exam, an eight-year
recency half-life, symmetric Dirichlet smoothing, and a seeded Monte Carlo
simulation. It does not predict exact questions, pool JEE Main/IIT-JEE records
into JEE Advanced, or reproduce the official exam format. The slot count is a
user-selected practice setting. The repository currently has no verified
question records, so the JEE Advanced command reports a uniform-prior
demonstration rather than a data-driven forecast. Add reviewed metadata before
interpreting forecast weights; use rolling-origin `backtest` to test the model
on held-out historical papers.

## Mathematics, physics, and animation foundation

The concept graph in `knowledge/` connects each exam topic to math prerequisites
and related concepts; each verified question record is attached through its
`topic_id`. The Gilbert Strang reference present here is the MIT OCW
18.085 Fall 2008 course material, whose first chapter is **Applied Linear
Algebra**—not a separately verified edition of a book with that exact title.
See `knowledge/README.md` for the scope, source notes, and mapping workflow.

The initial calculation layer contains small dense linear algebra routines,
constant-acceleration kinematics, and a calculation-backed vector-animation
specification. These are reviewed, testable primitives, not a solver for every
physics problem. Floating-point calculations and models can fail; they report
invalid inputs, expose residuals, and require independent physics checks. Use
`docs/architecture.md` for the staged path toward broader solvers and renders.

## Linked content network and Colab rendering

The Git-tracked CSV records and SQL schema define the source/paper/question/
concept network. Build the disposable SQLite index and exercise the
calculation-to-lesson path with the original kinematics integration example:

```bash
python -m content_engine init
python -m content_engine papers
python -m content_engine map-paper --paper-id iitjee-2008-1
python -m content_engine solve --problem data/kinematics_demo.json
python -m content_engine compile-lesson --problem data/kinematics_demo.json
python -m content_engine recommend --exam jee-main
```

### Start a batch from a plain-language request

Use the interactive gateway, or pass the brief directly. It saves an editable
JSON request with concept-match candidates, episode count, chosen formats, and
creative/review requirements; it does not invent answers or claim to render a
finished video.

```bash
python -m content_engine studio
python -m content_engine studio \
  --brief "Make an original JEE kinematics batch about reading motion graphs" \
  --episodes 6 --formats both
```

The request is saved under `requests/` by default. Commit it and give that file
to the assistant to author an original episode manifest. Review the physics,
sources, scripts, and storyboards; then run `batch-plan` on that completed
manifest. The episode count can be 1–10; `--formats` accepts `both`,
`vertical`, or `horizontal`.

For rendering, push the approved manifest and either:

* In GitHub, open **Actions → Render approved video batch → Run workflow**,
  select the manifest path, formats, and preview/high quality. Download the
  resulting artifact. High-quality renders require `approved-for-storyboarding`.
* In Colab, set `BATCH_MANIFEST` to the manifest path and `REVISION` to its
  reviewed commit SHA in `notebooks/render_in_colab.ipynb`, then run the cells.

Both paths require a complete validated manifest. They render silent visual
drafts, not finished narrated videos; inspect the render and complete narration,
caption, accessibility, and release review separately.

The indexed JEE papers are source placeholders, not verified question-bank
records. Add question metadata only after manually checking its exact paper
locator, rights, topic mapping, and answer. Open
`notebooks/render_in_colab.ipynb` in Google Colab and run its cells from top
to bottom. It installs the Manim system dependencies and pinned Python
requirements, validates the example problem batch, builds a disposable
database under `/content`, compiles the original kinematics demo, and renders
and verifies one low-resolution MP4. Outputs are stored locally under
`/content/saemphysics`; run the notebook's download cell before the runtime
ends, then upload the files to Drive manually if desired. Watch the preview
before setting `RENDER_FULL_BATCH = True`; a full high-quality batch can take
a long time. For repeatable renders, set the notebook's
`REVISION` to a reviewed commit SHA. See
[docs/content_network.md](docs/content_network.md) for the data contract,
review gates, and collaboration workflow.

## Index exam papers and study books as concept matrices

Add text-based exam papers to `exam_papers/` and study material to `book/`.
Then run:

```bash
python convert_pdfs.py
python matrix_pipeline.py
python matrix_pipeline.py --question \
  "A projectile has initial velocity and constant acceleration. Find its position."
python matrix_pipeline.py --question-file exam_papers/sample_question.md \
  --output output/question_analysis.json
```

`convert_pdfs.py` converts PDFs under `exam_papers/` and `book/` into
page-labelled `.md` files using local text extraction; pages without embedded
text are marked for OCR/manual review. It requires PyMuPDF, installed from
`requirements.txt`. The matrix pipeline reads `.mmd`, Markdown, UTF-8 text,
and DOCX; it splits numbered question headings into question rows and
book chapter/section/page headings into book rows, then creates normalized
question/book-to-concept matrices from the curated physics, chemistry, and
mathematics graph. If source and converted copies share a filename, the DOCX
is preferred, followed by `.mmd`, `.md`, and `.txt`.
It also emits prerequisite/math-link matrices and domain-to-engine/output
route matrices in `output/matrix_network.json`. Override the input/output
paths with `--exam-papers`, `--books`, and `--output`.

`.mmd` is accepted as Markdown-like text; the indexer does not interpret
Mermaid diagrams as physics models. Keep original documents and structured
project files in their suitable formats rather than renaming everything to
`.mmd`.

These are inspectable, keyword-based candidate mappings, not automatic
solutions or verified classifications. The currently implemented solvers
cover small dense linear systems and constant-acceleration kinematics; there
is no chemistry solver or audio renderer. The report labels supported
capabilities and unavailable routes explicitly. PDFs/scans are reported as
unsupported (there is no OCR); convert them to reviewed text first. Question
and book text is processed locally and is not copied into the generated
matrix report. Review source rights, concept matches, assumptions, and answers
before using any result in a lesson. A one-question analysis ranks direct
phrase evidence, propagates scores to graph-linked concepts, and lists
data-defined solver/explanation/visual routes from
`knowledge/solution_routes.csv`. Its scores are relative rankings, not
probabilities. Routes currently require typed inputs; concept recognition
does not parse equations or execute a solver. Every rebuild reloads the concept
graph and solution-route catalog, validates referenced concepts and
prerequisite cycles, and regenerates relationship matrices for all indexed
inputs. When you add a book, tell me and I can inspect newly matched concepts
and whether reviewed edges/routes need updating; the folder is not watched
automatically while no session is running.

Create an original, matrix-informed lesson-design draft with a weighted,
non-repeating combination of teaching approach, visual treatment, and optional
sound suggestions:

```bash
python video_learning.py --matrix output/matrix_network.json \
  --question-id "<question row ID from the matrix report>"
python video_learning.py --concepts math:derivatives math:integrals
```

The planner can incorporate human-rated observations about local videos; it
does not analyze raw video/audio or imitate any creator. See
[`docs/video_learning.md`](docs/video_learning.md) for the observation format,
source limits, and review requirements.

For separate local profiling of reference-video editing/audio metadata and
matrix-informed batch guidance, run:

```bash
python -m production_knowledge index --videos 3b1b
python -m production_knowledge advise \
  --manifest data/video_batches/batch_001.json \
  --matrix output/matrix_network.json
python -m content_engine batch-plan \
  --manifest data/video_batches/batch_001.json \
  --matrix output/matrix_network.json \
  --output output/video_batch_plan.json
```

This stores derived measurements, original production principles, human
ratings, and batch advice in `output/production_knowledge.sqlite`. It does not
transcribe videos or copy a creator's distinctive style. See
[`docs/production_knowledge.md`](docs/production_knowledge.md).

## Render the first batch in Google Colab

Open [`notebooks/render_in_colab.ipynb`](notebooks/render_in_colab.ipynb)
in Google Colab and run its cells from top to bottom. No Drive mount is needed:
the notebook saves the kinematics preview and optional 20-video batch under
`/content/saemphysics` in the temporary Colab runtime. Watch the preview before
setting `RENDER_FULL_BATCH = True`. Run the notebook's download cell and save
the files before ending or deleting the runtime; upload them to Drive manually
if desired. The batch renders are silent visual drafts, not final narrated or
release-approved videos.

## Create an episode

1. Copy the episode brief and review templates into a descriptively named
   folder, such as `episodes/electrostatics_001/`.
2. Get teacher approval for the central question and learning objective.
3. Record definitions, assumptions, derivation, checks, and traceable sources;
   get the physics approved before scripting.
4. Write narration alongside the storyboard and scene cards. Make each scene
   answer one question.
5. Implement one scene, render a low-quality preview, and review physics,
   timing, layout, and mobile legibility.
6. Record narration, edit, correct captions, and inspect the final export.
   Publish only after the release checklist is approved.
7. Commit source, decisions, and small licensed assets. Store large renders
   and private raw recordings outside normal Git history.

## Using reference books and other sources

The `book/` folder is a source library, not a license to reproduce a book's
text, figures, or lecture. Record the title, author, edition, location, URL,
and applicable license or permission with each episode. Learn from ideas and
verify claims independently; write original explanations, examples, and
visuals. See `docs/sources.md` before using a source in a published video.
