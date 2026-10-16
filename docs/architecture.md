# Studio architecture and approval workflow

The studio is a pipeline of small, reviewable artifacts. Its first goal is a
correct 30-60 second scene; reusable components and automation come only after
the manual workflow is understood.

## Layers and handoffs

| Layer | Artifact | Required check | Approver |
|---|---|---|---|
| Editorial | Episode brief: learner, central question, misconception, outcome | One focused objective for a named audience | Teacher |
| Physics | Review: definitions, assumptions, derivation, units, signs, limits, independent check | Equations and domain of validity are explicit | Teacher |
| Scene design | Script, storyboard, scene cards | Each visual has a teaching purpose and matches the approved physics | Teacher |
| Animation | Manim scenes and low-quality renders | Coordinate system, scale, labels, timing and render are inspected | Teacher |
| Post-production | Narration, edit, audio mix and corrected captions | Speech is intelligible and synchronized; mobile layout is legible | Teacher |
| Release | Export, metadata, source record and archive | Full export plays; source and decisions can reproduce it | Teacher |

Data flows from the brief to the physics review, script, storyboard, scenes,
preview, narration/edit, quality review, and publication package. If an
upstream claim or assumption changes, recheck every downstream artifact that
depends on it. A model's agreement is not scientific evidence or approval.

## Project structure

```text
config/
  brand.py
data/
  exam_question_metadata.csv
  physics_topics.csv
knowledge/
  concepts.csv
  links.csv
math_engine/
  linear_algebra.py
physics_engine/
  kinematics.py
animation_engine/
  vector_scene.py
docs/
  architecture.md
  channel_brief.md
  sources.md
episodes/
  vectors_001/
    brief.md
    physics_review.md
    script.md
    storyboard.md
    scenes.py
library/
  components/
  physics/
templates/
  episode_brief.md
  physics_review.md
  scene_card.md
  release_checklist.md
```

Add abstractions only when a visual or physics model has been reused enough to
show which inputs genuinely need to vary. Keep screen coordinates separate
from physical quantities; label schematic diagrams as schematic, and do not
imply quantitative scale unless the code preserves it.

## Concept-to-animation path

1. Record a source-linked exam question as metadata, with a human-verified
   topic tag. Keep protected question text and figures out of the public
   metadata ledger unless reuse rights are explicit.
2. Resolve its `topic_id` to a physics concept in `knowledge/concepts.csv`.
   `knowledge/links.csv` records mathematical tools and prerequisite concepts.
   Keep syllabus references versioned and source-checked; a topic catalog alone
   is not proof of alignment to a particular year's official syllabus.
3. Formulate a typed model with explicit assumptions, units, coordinate
   conventions, and domain of validity. Use deterministic math/physics
   primitives for supported cases; reject invalid or unsupported inputs.
4. Independently check derivations, dimensions, limiting cases, and numerical
   residuals. A small residual is a numerical diagnostic, not proof that the
   model or answer is physically correct.
5. Generate an animation specification from model outputs. Map model
   coordinates into screen coordinates separately, label schematic scales,
   and test invariants before rendering.
6. Render a preview and require teacher review of the physics, visual
   encoding, narration, and final export. Never auto-approve a generated scene.

The first numerical implementation supports vectors, small dense linear
systems, and constant-acceleration motion, plus a 2D vector decomposition
scene-spec archetype. It does not solve arbitrary word problems, infer every
model from natural language, or guarantee error-free output. Expand one
well-defined domain at a time, with analytical test cases and independent
checks before adding a new solver or animation template.

## Editorial and visual originality

Aim for original lessons that use clear visual reasoning, intuition, careful
derivations, meaningful motion, and accessible sound. These are broad
educational qualities, not a request to copy any particular creator's
distinctive scripts, artwork, narration, or visual identity. Physics, content
rights, and publication remain human approval gates.

## Reproducibility and assets

- Pin Python package versions and record the Python, Manim, FFmpeg, and render
  settings used for a published episode.
- Keep source, scripts, configuration, small licensed assets, tests, and
  decisions in Git.
- Exclude caches, generated media, large exports, and private raw recordings.
  Use a deliberate asset store or Git LFS only when needed.
- Name episodes and scenes descriptively; use Git tags for approved releases.
- Keep a failure log with the symptom, cause, fix, and prevention.

## Human approval gates

1. **Editorial:** objective and central question approved.
2. **Physics:** model, derivation, assumptions, and checks approved.
3. **Design:** narration and visual encoding approved.
4. **Preview:** rendered animation reviewed at normal speed.
5. **Release:** audio, captions, export, and publication package approved.

Record approval and reviewer/date in the episode artifacts. An unchecked gate
is pending; AI must not mark it approved.
