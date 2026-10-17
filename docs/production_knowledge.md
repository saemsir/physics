# Local production-knowledge advisor

`production_knowledge` is a separate, local SQLite-backed analysis and advice
engine. It profiles technical properties of the videos in `3b1b/`, maintains
original production principles and human review ratings, then adds
concept-specific editing, narration, sound, visual, and verification advice to
a selected lesson batch. The database defaults to the ignored file
`output/production_knowledge.sqlite`; neither video frames nor extracted
dialogue are stored.

This is an inspectable advisory system, not a neural network trained to clone
a creator. It uses general teaching principles and technical measurements,
not anyone's scripts, voice, signature pacing, music, sound effects, layouts,
or scene sequence. Use reference videos only when you have the right to
analyze them.

## Set up the local corpus

Install the project requirements, including the bundled FFmpeg decoder:

```bash
python -m pip install -r requirements.txt
```

Index local video metadata:

```bash
python -m production_knowledge index --videos 3b1b
python -m production_knowledge summary
```

Indexing groups filename shards such as `topic_0_429.mp4` and
`topic_428_795.mp4` by their common title. It measures duration, frame size,
frame rate, codec, candidate scene-change timestamps, audio stream presence,
approximate mean/peak audio level, and detected silence. Unchanged files are
skipped on later runs. Failed files are recorded and reported with a non-zero
exit status while successful profiles remain available. Media paths and these
derived measurements stay in the local database; transcripts, frames, voice
identities, and source audio are not retained. Scene-change candidates are
not a measure of editing quality, and audio levels cannot identify speech,
music, or effects.

Concept tags inferred from video filenames are tentative keyword matches only.
Review them before interpreting a reference-video comparison. The engine does
not claim to analyze visual meaning, emotional delivery, narration wording,
musical composition, or an individual voice.

## Advise a matrix-selected batch

Build the current matrix report, then pass it with the selected batch manifest:

```bash
python matrix_pipeline.py --output output/matrix_network.json
python -m production_knowledge advise \
  --manifest data/video_batches/batch_001.json \
  --matrix output/matrix_network.json
```

Or make production advice part of the normal validated batch-plan operation;
when `--matrix` is supplied, the command automatically attaches and persists
the advice:

```bash
python -m content_engine batch-plan \
  --manifest data/video_batches/batch_001.json \
  --matrix output/matrix_network.json \
  --output output/video_batch_plan.json
```

The advisor maps each episode's concept or `topic_id` through the matrix. To
connect a specific indexed question or book section instead, set
`matrix_question_id` or `matrix_book_section_id` on that episode. The output
contains suggestions for both vertical and horizontal deliverables and is
persisted in the SQLite database as well as written to
`output/production_batch_advice.json`.

Every suggestion includes its rationale, matched concepts, evidence category,
and any local reference measurements. The rules prioritize an explicit
question and model, readable reasoning, visuals that encode the math,
purposeful transitions, clear spoken mathematics, speech intelligibility,
meaningful or absent sound effects, and an independent solution check. They
are starting points, not fixed timing instructions or publication approval.

## Learning from human review

Record ratings for each reference lesson after watching it yourself:

```bash
python -m production_knowledge review \
  --video-title "a locally reviewed video title" \
  --concepts math:derivatives math:graphs \
  --editing 4 --narration-pacing 5 --narration-clarity 5 \
  --narration-sync 4 --sound 3 --visual-clarity 5 \
  --notes "The graph stays readable while the derivative is explained."
```

Ratings are integers from 1 (poor fit) to 5 (strong fit). Review narration
pacing, clarity, and synchronization separately. The advisor uses stored
concept-overlapping ratings to adjust the relative priority of relevant
guidance areas. Notes are limited to 500 characters; enter your own review,
not copied narration or dialogue. Database review history is local and can be
removed by deleting the database file if desired.

## Limits and originality

The engine does not verify exam provenance, solve questions, judge physics,
generate narration or sound, edit footage, or render a video. A matrix match
is not proof that a problem is an authentic JEE PYQ or that its answer is
correct. Ask a subject expert and teacher to verify sources, rights, equations,
assumptions, narration, storyboard, and preview. Make original SaemPhysics
scripts, diagrams, edits, and audio; do not imitate Grant Sanderson's or
another creator's distinctive presentation.
