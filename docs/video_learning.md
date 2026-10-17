# Matrix-informed video lesson planner

`video_learning.py` turns a selected concept set, JEE question candidate, or
book-section row from the local concept matrices into an original lesson-design
draft. It samples among inspectable teaching approaches, visual treatments,
and optional sound palettes. A local history file prevents reuse of the same
approach/visual/audio combination for the same concept set. Set `--seed` for a
repeatable draw; without a seed the planner uses fresh system randomness.

## Run it

Build a concept-matrix report for the local reference library and exam papers:

```bash
python matrix_pipeline.py --output output/matrix_network.json
```

Generate a plan for an analyzed question:

```bash
python video_learning.py --matrix output/matrix_network.json \
  --question-id "<question row ID from the matrix report>"
```

Or select a book section from the report's `book_concept_matrix` row labels,
or provide concept IDs directly:

```bash
python video_learning.py --matrix output/matrix_network.json \
  --book-section-id "<book-section row ID from the matrix report>"
python video_learning.py --concepts math:derivatives math:integrals
```

If `--matrix` is omitted, the planner builds the report in memory from the
repository's `book/` and `exam_papers/` directories. It writes a JSON lesson
plan under `output/` by default and stores uniqueness history in
`output/video_style_history.json`. Both locations can be changed with
`--output` and `--history`.

## Learning from reviewed videos

The current `videos/` folder has no source video or audio examples for
automatic analysis. The planner does not claim to learn audiovisual style
from the book text or raw media. Instead, it can incorporate human-reviewed
observations in this JSON format:

```json
[
  {
    "video_id": "local-video-001",
    "concept_ids": ["math:derivatives", "math:graphs"],
    "style_id": "geometric_calculus",
    "visual_treatment": "coordinate_plot",
    "audio_palette": "quiet_precision",
    "rating": 5
  }
]
```

`style_id`, `visual_treatment`, and `audio_palette` must use the planner's
original labels in `video_learning.py`; ratings are integers from 1 to 5. The
file accepts only video IDs, concept IDs, those three labels, and a rating—not
scripts, transcripts, extracted frames, audio, or other source content. Supply
it with `--observations reviewed_video_notes.json`. Ratings update small,
concept-overlap Beta-prior preferences for teaching, visual, and audio
choices; this is transparent preference adaptation, not model training or a
claim of calibrated quality.
Only use observations you have the rights and permission to review.

## Source, originality, and review limits

The matrix pipeline identifies candidate concepts from source text; its
keyword matches are not verified interpretations, solutions, or exam
predictions. A video question row is not automatically a verified JEE PYQ.
Confirm its source, rights, exact question, answer, and tags before scripting.
The Strang and Feynman materials inform topic selection and broad habits such
as explicit assumptions, derivation, intuitive explanation, and independent
checks. The planner does not reproduce their wording or illustrations.

The output is a draft, not a finished narration, sound mix, storyboard, or
render. Sound cues are optional design suggestions; no audio is generated.
Use original wording, visuals, and sound. Do not imitate a specific creator's
distinctive voice, script, artwork, or signature presentation. A subject
expert and teacher must review every claim, derivation, source, and preview.
Sampling probabilities describe only the planner's remaining weighted
options; they do not predict learning, correctness, or exam appearance.

For persistent review ratings, technical reference-video measurements, and
advice attached to every matrix-backed batch plan, use the separate
[`production_knowledge` workflow](./production_knowledge.md).
