# Saem Physics video production: operating guide and architecture

## The short answer: where to work

Use each service for a different job:

| Place | Use it for | Do not use it for |
| --- | --- | --- |
| GitHub | Permanent source, reviewed episode data, code, and version history | Storing generated MP4s or treating CI as a video renderer |
| Codespaces | Editing episode JSON, code, captions, and review changes; running fast validation | Long, high-resolution Manim renders |
| GitHub Actions | Automatically running tests, checking the batch contract, and catching broken changes | Rendering the 20-video batch; the current workflow does not render |
| Google Colab | Running the Manim notebook, previews, and batch renders on a temporary compute runtime | The permanent source of truth or a guaranteed always-on render service |
| Google Drive | Persisting rendered MP4s, reports, and approved production audio outside Git | Public source storage unless sharing permissions are intentionally configured |
| Local audio workstation | Recording and editing narration privately using the voice profile | Automatically generating a voice from the profile |

**Recommended now:** prepare and review the content in Codespaces/GitHub, then
open [`notebooks/render_in_colab.ipynb`](../notebooks/render_in_colab.ipynb)
in Colab to render. Save renders to a private Drive folder. Use GitHub Actions
as the validation gate, not as the renderer.

## How to provide input for a video batch today

There is not yet a web form, conversational intake app, or automatic
question-to-video pipeline. The current input is a reviewed JSON manifest:
[`data/video_batches/batch_001.json`](../data/video_batches/batch_001.json).

1. In Codespaces, create a new batch JSON by following the existing manifest's
   shape. Keep one episode per idea and provide its ID, type (`problem` or
   `concept`), title, topic, question, answer, solution, visual hook,
   misconception, source reference, and review status. For a problem supported
   by the computation engine, also provide a typed `problem_spec`, units,
   assumptions, input values, and expected outputs.
2. Use original wording and visuals. A book section or exam-paper locator is
   provenance, not permission to reproduce a copyrighted question, paragraph,
   or figure. Keep unverified material marked as unverified.
3. Set the batch review state to `draft-owner-review` while editing. Ask for
   editorial and physics review; only mark it
   `approved-for-storyboarding` after approving the storyboards. That status
   does not mean exam verification or release approval.
4. Validate before committing:

   ```bash
   python -m content_engine batch-plan \
     --manifest data/video_batches/batch_001.json \
     --output /tmp/batch_plan.json
   ```

   The current batch contract expects exactly 10 episodes and expands them to
   10 vertical 9:16, 60-second deliverables and 10 horizontal 16:9,
   180-second deliverables. It checks selected problem calculations and
   formula audits, but human review is still required.
5. Commit and push the reviewed source to GitHub. GitHub Actions runs tests,
   database/lesson checks, and batch validation. Fix any failure before
   rendering. For a reproducible render, use the reviewed commit SHA in the
   notebook's `REVISION` cell instead of `main`.
6. In Google Colab, open the notebook from GitHub, set `BATCH_MANIFEST` to
   your committed batch JSON path, run setup and validation, mount Drive, and
   render the two preview videos first. The notebook previews the first
   episode in both formats and names the Drive folder from the manifest's
   batch ID. Watch both aspect ratios. If approved, run the vertical and
   horizontal high-quality cells separately. Keep `--resume` enabled if
   Colab disconnects.
7. For batch 001, use the timed script in
   [`episodes/batch_001/narration.json`](../episodes/batch_001/narration.json).
   The Colab preview cell shows its timed beat cues alongside the vertical and
   horizontal silent previews for the first episode. Read along and check
   whether the wording fits each visual beat. Timing aligns to beat boundaries,
   not frame-level gestures. The lines are not automatically recorded or mixed
   into the video yet.
8. Review all exports, then add/verify narration and captions and complete
   physics, editorial, accessibility, and release approval. The current
   Manim output is a silent visual draft with text branding; it is not a
   publish-ready video.

For a local or Codespaces preview, after installing the repository's renderer
dependencies, the same batch renderer can be run without Colab:

```bash
python tools/render_video_batch.py \
  --quality preview \
  --video-ids b001-e01-projectile-components-vertical \
               b001-e01-projectile-components-horizontal \
  --output-dir /tmp/batch_preview
```

This can be convenient for a small test, but it requires Manim, FFmpeg, and
`ffprobe`; a local machine may not have enough resources for all 20
high-quality videos.

## Running the narration profile well

[`config/audio_profile.json`](../config/audio_profile.json) and
[`docs/audio_profile.md`](audio_profile.md) define a production guide: delivery
style, pacing, recording setup, optional processing, and mix targets. They do
**not** clone a voice, create narration, or get applied by the current
notebook/renderer. The analyzed sample was used for technical measurements
only; EQ and sound-quality judgments still need private listening review.

Recommended workflow:

1. Write and approve a narration script for each episode before recording.
   Use the profile's pace as a starting point, but let equations and pauses
   determine timing. A 60-second script is usually around 110–145 spoken
   words; a three-minute script around 345–420 words before allowing extra
   space for equation pauses. Rehearse with the actual visual timing.
2. Record in a local audio workstation (for example Audacity or Reaper) in a
   quiet, treated space. Follow the profile's 48 kHz mono PCM recording
   recommendation and -12 to -6 dBFS peak target; leave headroom and avoid
   aggressive denoising. The profile is a starting point, not a preset to
   apply blindly.
3. Listen for room noise, plosives, sibilance, reverberation, and intelligible
   scientific terms. Apply only the processing that the recording needs.
   Check the final mix on headphones, phone speakers, and in mono; synchronize
   and proofread captions against the actual spoken track.
4. Keep raw takes private. If using Colab for later audio muxing, upload only
   the approved narration file to a private runtime/Drive location, restrict
   Drive sharing, and do not put audio in a public repo or CI artifacts.
   Delete temporary runtime copies when finished.
5. Archive only the approved final audio and required release assets in a
   controlled location. Track non-sensitive metadata (script version,
   profile version, speaker approval, audio filename/checksum, and review
   state) in the batch manifest when that workflow is implemented.

**Voice-sample privacy:** `saem_voice_sample.wav` is currently tracked in the
Git repository. If the repository is public, it is accessible to visitors.
The ignore rule does not untrack it, and deleting it in a later commit would
not erase it from Git history. Do not use that file as a Colab input merely
because it is present in the checkout. Decide separately whether it should be
removed from the repository and whether history remediation is needed.

## Architecture today

```text
Owner / educator
   |
   +-- authors and reviews episode manifest
   |      data/video_batches/*.json
   |      source/concept links + typed problem specs
   |
   v
GitHub repository (versioned source of truth)
   |
   +--> GitHub Actions: tests, schema/engine checks, batch validation
   |                    (no video or voice rendering)
   |
   +--> Codespaces: authoring, code changes, local validation/preview
   |
   +--> Colab notebook: pin checkout revision -> install renderer ->
                        validate -> Manim render -> verify MP4/report
                             |
                             v
                       private Google Drive
                       preview + final visual drafts
                             |
                 human review / narration / captions
                             |
                             v
                        release platform
```

The content engine validates the manifest and expands it into render briefs.
The physics/animation engines provide tested computation and scene
representations for supported cases. Manim currently uses the batch manifest
to produce diagrams, on-screen explanations, and text-only branding. The
batch renderer checks output dimensions, frame rate, duration, and file
checksum. It does not yet compose a script-driven voice track, create
captions, or make the visual scene unique and fully data-driven for every
episode. Those are explicit future capabilities, not current guarantees.

## Production specifications

| Area | Current specification/status |
| --- | --- |
| Batch size | 10 content episodes, each expanded to two formats (20 exports) |
| Vertical | 9:16, 1080x1920, 60 seconds |
| Horizontal | 16:9, 1920x1080, 180 seconds |
| Audience | Ages 14–21; define symbols and state assumptions |
| Brand | `Saem Physics` and `NEET JEE MIT`; text-only until an approved logo asset is supplied |
| Content input | Versioned JSON manifest; no input form yet |
| Narration scripts | 20 original draft scripts in `episodes/batch_001/narration.json`, six timed cues per vertical video and seven per horizontal video |
| Calculation checks | Existing typed constant-acceleration path plus selected formula audits; only supported models execute |
| Visuals | Original Manim visual drafts; human legibility and scientific review required |
| Voice | Spoken-math profile and timed scripts are available; current rendered MP4s are silent and no audio is composed |
| Captions | Not currently generated; must be authored/synchronized and reviewed |
| Output validation | MP4 dimensions, FPS, duration, non-empty file, SHA-256 report |
| Rendering | Colab notebook and Drive export; Colab runtime is temporary and may disconnect |
| Release | Human physics, editorial, audio, caption, rights, and final playback approval |

Use the aspect-ratio-specific composition as a design constraint: vertical
videos need large text, a safe center column, and fewer simultaneous elements;
horizontal videos can carry a wider diagram and more explicit derivation.
Verify equations and captions at phone size. The renderer's technical MP4
checks do not establish scientific correctness or readability.

## Future upgrades, in recommended order

### 1. Easier, safer content intake

- Add a validated episode template and a small CLI command to scaffold a new
  batch, assign IDs, and check required fields before review.
- Add a simple web form only after the JSON schema and approval process are
  stable. The form should export the same versioned manifest, not become a
  second source of truth.
- Record source locator, rights state, question verification, solver result,
  reviewer, and revision history as separate fields. Never infer approval
  from successful computation.

### 2. Script and storyboard as explicit data

- Add per-format narration scripts, timed beats, on-screen text, accessibility
  notes, and scene parameters to a renderer-neutral lesson format.
- Validate script duration against each 60/180-second timeline, text length
  against safe areas, and every displayed number against the engine result.
- Support separate vertical and horizontal edits instead of simply scaling
  one composition.

### 3. Reliable audio and caption production

- Add an optional local/private audio workflow with explicit user-selected
  files; never upload the raw sample automatically.
- Support voice takes, approved processing settings, voice-over alignment,
  loudness/true-peak checks, and subtitle export (for example WebVTT/SRT).
- Keep audio provenance and consent/release state separate from public content
  metadata. Do not add automatic voice cloning without a distinct, informed
  consent and privacy decision.

### 4. Render pipeline improvements

- Add a single manifest-driven command that builds previews and production
  outputs, stores a machine-readable run manifest, and resumes safely by
  content revision and renderer version.
- Pin and report Manim, FFmpeg, fonts, Python dependencies, frame rate,
  resolution, and quality settings. Record the exact Git commit and input
  checksums with every output.
- Add automated visual QA for missing frames, blank exports, clipping, safe
  margins, and audio/caption duration; retain human sign-off for correctness
  and aesthetics.
- Keep generated media outside Git. Use private, access-controlled storage
  for review and a separately approved destination for release masters.

### 5. Scale the knowledge network

- Continue adding sources and concepts only with provenance and rights review.
- Add model-specific solvers with units, domain constraints, analytical
  reference tests, and failure tests before using them in lessons.
- Move from generated local SQLite to a managed database only when multiple
  concurrent editors or automated services need shared writes; keep Git
  migrations and reviewed content records as the auditable change history.

### 6. Optional orchestration

When a batch is consistently reproducible, add a GitHub Actions `workflow_dispatch`
job that builds previews or queues a render on an appropriate worker. Do not
use a normal GitHub-hosted job as a substitute for a long, GPU/resource-heavy
Colab render without checking runtime limits, storage, secrets, and cost.
Rendering should consume a reviewed commit and write artifacts to controlled
external storage, never commit MP4 files back to the source repository.

## Current acceptance gates

Before a batch is considered ready to publish:

- [ ] The batch validator and the full relevant test suite pass.
- [ ] Every source, rights state, question, solution, units, and assumption is
  reviewed; unsupported material is excluded or clearly flagged.
- [ ] The physics reviewer approves each derivation and displayed result.
- [ ] Preview videos pass layout and timing review in both aspect ratios.
- [ ] Final exports match the declared resolution, FPS, and duration.
- [ ] Narration is approved, intelligible, and correctly mixed; captions match
  the audio and equations.
- [ ] Logo and music are original or properly licensed.
- [ ] All 20 outputs receive a final human playback and release decision.
