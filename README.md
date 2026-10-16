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
docs/                    Architecture, channel brief, source policy
episodes/                Episode-specific brief, physics, script and scenes
templates/               Brief, review, storyboard and release templates
book/                    Reference material; check source permissions before reuse
data/                    Exam-question metadata schema and physics topic catalog
content_engine/          Versioned SQLite index, provenance links and lesson compiler
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

## Build exam-focused video briefs

The exam engine uses verified, source-linked question metadata to prioritize
physics topics and produce ten 16:9 three-minute and ten 9:16 one-minute
original video briefs:

```bash
python -m exam_engine recommend --exam jee-main
python -m exam_engine recommend --exam jee-advanced --as-of-year 2026 \
  --output output/jee-advanced-video-ideas.md
python -m exam_engine backtest --exam jee-main
python -m exam_engine map-topic --topic electrostatics
python -m math_engine solve-linear --matrix '[[2,1],[1,3]]' --rhs '[5,7]'
python -m physics_engine constant-acceleration --position-m '[0,0]' \
  --velocity-m-per-s '[3,2]' --acceleration-m-per-s2 '[0,-9.8]' --time-s 1
python -m unittest discover -s tests -v
```

Start with `data/README.md` before adding records. The metadata ledger is
intentionally empty until source provenance and topic tags have been verified;
it does not contain copied exam text. With no observations for a selected exam,
the command labels its output as a uniform curriculum baseline. With records,
it reports smoothed historical topic shares, not guaranteed or calibrated
predictions of upcoming questions. Every proposed explanation remains subject
to source-rights, physics, and teacher review. Run `backtest` to compare
rolling-origin topic rankings with a uniform baseline before using the results
to prioritize study or video production.

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

The indexed JEE papers are source placeholders, not verified question-bank
records. Add question metadata only after manually checking its exact paper
locator, rights, topic mapping, and answer. Open
`notebooks/render_in_colab.ipynb` in Google Colab to build the database and
render a lesson preview. See [docs/content_network.md](docs/content_network.md)
for the data contract, review gates, and collaboration workflow.

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
