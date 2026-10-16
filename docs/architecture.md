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

## First project structure

```text
config/
  brand.py
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
