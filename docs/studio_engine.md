# SaemPhysics Studio coordinator

The `studio_engine` package is the repository's central processing interface.
Its role is to validate one portable request, invoke registered existing
engines, connect task results when requested, and write an auditable run
manifest. It does not duplicate the physics, exam, content, matrix, or video
engines.

## Computation design basis

The local Feynman computation volume was consulted before designing this
coordinator. The implementation applies several general computational ideas:

- Represent the request as explicit, mechanical instructions (version, action,
  inputs, dependencies) rather than implicit conversational state.
- Keep each task's operation and output inspectable; specialized engines stay
  independently testable.
- Validate boundaries and record machine-readable results so malformed input
  and failed steps are observable rather than silently producing success.
- Treat uncertainty and errors as part of the data contract: a seeded forecast
  is reproducible, but not certainty; task outcomes distinguish failure and
  dependency blocking.
- Keep outputs portable and preserve provenance/review boundaries instead of
  implying that computation itself verifies academic or editorial quality.

These are original architecture decisions, not quotations or a reproduction
of the book.

## Usage

```bash
python -m studio_engine actions
python -m studio_engine validate --request config/studio_request.example.json
python -m studio_engine run --request config/studio_request.example.json
python -m studio_engine run --request request.json --output-dir /content/studio-run
```

The output override is useful in Colab and other environments where the
repository checkout and generated artifacts use different paths. The default
output is `output/studio/<run_id>/`. The request's default output directory
must be repository-relative. A run writes:

- `run.json`: versioned run status, request digest, revision where available,
  task counts, timestamps, and result-file references.
- `<task-id>.json`: JSON result for every successful task.

Tasks execute in the order written. A dependency must appear earlier. Use
`depends_on` for an explicit dependency or a JSON reference such as
`{"$ref":"matrix#/network"}`; the coordinator infers that dependency. JSON
pointer components support `~0` and `~1`. Failed tasks are recorded, tasks that
depend on them are marked `blocked`, and independent tasks still run. The
overall result is `succeeded`, `partial`, or `failed`; the CLI returns a
non-zero status unless every task succeeds.

Requests have `schema_version: 1`, optional stable `run_id`, optional
repository-relative `output_dir`, and 1-50 task objects. Each task has a unique
`id`, a supported `action`, optional `params`, and optional `depends_on`.
Action-specific inputs follow.

## Registered actions and parameters

Paths in task parameters are repository-relative unless noted. Defaults below
are applied by the coordinator.

| Action | Parameters |
|---|---|
| `content.initialize` | `database` (default `output/content.sqlite`) |
| `content.summary` | `database` (default `output/content.sqlite`; must be initialized) |
| `content.solve` | `problem` (JSON problem file), `database` (default `output/content.sqlite`) |
| `content.compile_lesson` | `problem`, `database` (default `output/content.sqlite`) |
| `math.solve_linear` | `matrix`, `rhs` |
| `physics.constant_acceleration` | `initial_position_m`, `initial_velocity_m_per_s`, `acceleration_m_per_s2`, `time_s` |
| `exam.recommend` | `exam` (`jee-advanced` default), `as_of_year` (defaults to current year), `topics` (default `data/physics_topics.csv`), `data` (default `data/exam_question_metadata.csv`) |
| `exam.backtest` | Same selection parameters as `exam.recommend` |
| `exam.forecast` | `exam`, `target_year` (current year default), `question_count` (10), `simulations` (10000), `seed` (2026), `topics`, `data` |
| `exam.import_candidates` | No parameters. Writes pending candidate records to the tracked data catalogs; this is an explicit data-import operation, not a read-only forecast. |
| `matrix.build` | `exam_papers` (default `exam_papers`), `books` (default `book`) |
| `audio.analyze_reference` | `wav` (repository-local PCM WAV; read-only signal measurements) |
| `production.index_references` | `videos_dir` (repository-local reference folder), `database` (default `output/production_knowledge.sqlite`) |
| `production.record_review` | `video_title`, `concept_ids`, integer 1-5 ratings `editing`, `narration_pacing`, `narration_clarity`, `narration_sync`, `sound`, `visual_clarity`; optional `notes` (max 500 characters) and `database` |
| `video.request` | `brief` (required), `batch_id`, `episodes` (10), `formats` (`both`, `vertical`, or `horizontal`) |
| `video.lesson_plan` | `matrix` object or `matrix_path`; one of `concept_ids`, `question_id`, `book_section_id`; optional `observations` file, `history` path (default `output/video_learning_history.json`), and `seed` |
| `video.batch_plan` | `manifest`; optional `matrix` object to attach local production advice, and `production_database` (default `output/production_knowledge.sqlite`) |
| `video.render_batch` | `manifest`, `formats` (default vertical and horizontal), optional `video_ids`, `quality` (`preview` default; `high` requires `approved-for-storyboarding`), `fps` (15 preview, 30 high), `resume`, and `output_dir` (default run `renders/`) |

For arrays and algorithm-specific constraints, the engine that owns the action
validates its parameters and reports errors in the task record. Examples and
the machine-readable outer schema are in
[`config/studio_request.example.json`](../config/studio_request.example.json)
and [`schemas/studio_request.schema.json`](../schemas/studio_request.schema.json).

## Data, review, and capability limits

- `content.initialize` materializes the Git-tracked content catalogs into a
  disposable SQLite database. The catalogs remain canonical.
- Exam ranking and forecasting continue to consume only source-linked rows
  marked `verified`. Pending or keyword-suggested topic tags are not silently
  promoted.
- The matrix builder's matches are candidate links, not verified exam-question
  classifications. A video lesson plan remains design guidance.
- `audio.analyze_reference` reports technical metrics from PCM WAV files; it
  does not replace listening review or assess voice quality. `video.lesson_plan`
  can provide visual, narration, and sound-design guidance; there is no audio
  recording, speech synthesis, or sound mixing action.
- `production.index_references` analyzes videos locally into the separate
  production SQLite database; `production.record_review` records explicit
  human ratings. The batch planner can use that database when attaching
  production advice.
- `video.render_batch` uses the existing repository batch renderer and its
  fixed Manim scene. It creates silent visual drafts, not arbitrary generated
  lessons, finished audio/video, captions, or published output.
- High-quality rendering is gated on the existing storyboard-approval status.
  Preview rendering is still a draft and must receive physics, rights, visual,
  audio, accessibility, and teacher review as relevant.
- `content.solve` and `content.compile_lesson` require an initialized database
  and retain the existing typed problem schema and physics checks.

GitHub Actions, Colab, Codespaces, and local Python can all invoke this CLI
against the same request file. Generated databases and run outputs are local
artifacts; store canonical inputs and reviewed manifests in version control
according to the repository's data and rights policies.
