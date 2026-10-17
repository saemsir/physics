# First mixed video and Physics practice batch

The first batch draft is in
[`data/video_batches/batch_002.json`](../data/video_batches/batch_002.json):
five concept episodes and five problem-solving episodes, with 9:16 and 16:9
deliverables declared. Every episode is still `proposed` and the manifest is
`draft-owner-review`; review the physics, question wording, references, visual
hooks, and answers before changing those statuses.

The separate original 10-question Physics practice set is
[`data/practice_papers/jee_advanced_2027_physics_set_01.json`](../data/practice_papers/jee_advanced_2027_physics_set_01.json).
Its `forecast_basis` is part of the paper contract: there are no verified
source-linked JEE Advanced question records in the predictor, so its topic
baseline is prior-only. The paper is not a reliable prediction of actual
questions or the official exam pattern. Questions are original practice
questions; the forecast engine samples topics, not questions.

## Input and planning

1. **Edit the JSON manifest directly.** Each episode has a type, topic, prompt,
   worked answer, misconception check, and visual hook. Keep both kinds of
   episodes in the batch and preserve the output contract: ten episodes means
   ten vertical plus ten horizontal deliverables.
2. **Use the unified coordinator.** Its request file runs matrix indexing,
   creates the reviewable batch plan with local production advice, and produces
   the seeded 2027 Physics topic baseline:

   ```bash
   python -m studio_engine validate --request config/studio_request.batch_002.json
   python -m studio_engine run --request config/studio_request.batch_002.json
   ```

   Results and the run manifest are written to
   `output/studio/jee-advanced-2027-first-batch-complete/`.
3. **Render the printable papers** (candidate paper and separate worked
   solutions) either as part of the unified Studio request above, or directly:

   ```bash
   python tools/render_practice_paper.py
   ```

   The Studio run writes both PDFs under its `paper_pdfs` result directory;
   the direct command writes under `output/practice_papers/`. Edit the
   canonical JSON paper, then rerun either route to refresh the PDFs.

## Video rendering with narration in Codespaces or local Python

The render worker needs the project Python dependencies plus Manim's system
tools. Google Cloud Text-to-Speech also needs a Google Cloud project with the
Text-to-Speech API enabled, billing configured, and credentials authorized to
use that API. TTS usage may incur charges. The default voice is Google's
`en-US-Neural2-J`; choose another supported voice with `--voice-name`. This
uses a Google-supplied voice, not a cloned person's voice. Keep credentials
outside the repository.

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev \
  texlive-latex-extra texlive-fonts-recommended dvisvgm
python -m pip install -r requirements.txt
```

Render one vertical preview first, inspect it at normal speed, then render
the complete batch:

```bash
python tools/render_video_batch.py \
  --manifest data/video_batches/batch_002.json \
  --video-ids b002-e01-collision-spring-vertical \
  --formats vertical --quality preview \
  --narration google --voice-name en-US-Neural2-J \
  --output-dir output/batch_002-preview --resume

python tools/render_video_batch.py \
  --manifest data/video_batches/batch_002.json \
  --formats vertical horizontal --quality preview \
  --narration google --voice-name en-US-Neural2-J \
  --output-dir output/batch_002-preview --resume
```

For better timing and delivery, add a teacher-reviewed `narration` object to
each episode in the manifest:

```json
"narration": {
  "vertical": "The concise, spoken one-minute script.",
  "horizontal": "The complete, paced three-minute lesson script."
}
```

At a conversational pace, aim for roughly 110-130 words for a one-minute
vertical script and 320-380 words for a three-minute horizontal lesson.
Treat those as starting estimates; review the spoken timing and the report's
`narration_coverage` for each render.

Without those optional scripts, the renderer speaks the episode's title, visual
hook, question, solution, misconception, and answer to create an audio draft.
The report includes each voice track's duration and coverage; extend the
format-specific script if it leaves too much quiet time. Narration longer than
the video contract is rejected rather than cut off. Audio is cached by script
and voice within the output directory. The output includes spoken narration;
music, sound effects, reviewed captions, and publishing still require separate
production and human review.

After the owner approves the storyboards, mark the batch and all episodes
`approved-for-storyboarding`, then choose `--quality high`.

## Other environments

- **GitHub Actions:** create a repository secret named
  `GOOGLE_TTS_SERVICE_ACCOUNT_JSON` containing the service-account JSON, then
  run **Actions → Render approved video batch**. Select `batch_002.json`,
  formats, quality, and narration voice. The credentials are written to a
  temporary runner file and are not included in artifacts. Download the
  uploaded artifact when the workflow completes.
- **Google Colab:** clone the repository into a notebook, install the same
  system and Python dependencies, then authenticate using Google Cloud
  Application Default Credentials. For example, store the service-account JSON
  in Colab Secrets as `GOOGLE_TTS_SERVICE_ACCOUNT_JSON`, write it to a
  temporary file (never print it), and set `GOOGLE_APPLICATION_CREDENTIALS` to
  that path. Run the same Python command. Save or download `output/` artifacts
  explicitly; Colab's local filesystem is temporary.

Colab setup cells for the prepared 20-video batch:

```python
from google.colab import userdata
from pathlib import Path
import os
import subprocess
import sys

subprocess.run(["git", "clone", "https://github.com/saemsir/physics.git", "/content/physics"], check=True)
os.chdir("/content/physics")
subprocess.run(["apt-get", "update", "-qq"], check=True)
subprocess.run([
    "apt-get", "install", "-y", "ffmpeg", "libcairo2-dev",
    "libpango1.0-dev", "texlive-latex-extra",
    "texlive-fonts-recommended", "dvisvgm",
], check=True)
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

credential_file = Path("/content/google-tts-service-account.json")
credential_file.write_text(userdata.get("GOOGLE_TTS_SERVICE_ACCOUNT_JSON"), encoding="utf-8")
credential_file.chmod(0o600)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(credential_file)

subprocess.run([
    sys.executable, "tools/render_video_batch.py",
    "--manifest", "data/video_batches/batch_002.json",
    "--formats", "vertical", "horizontal",
    "--quality", "preview",
    "--narration", "google",
    "--voice-name", "en-US-Neural2-J",
    "--output-dir", "output/batch_002",
    "--resume",
], check=True)
```

Add the service-account JSON to Colab's **Secrets** panel as
`GOOGLE_TTS_SERVICE_ACCOUNT_JSON` and grant the notebook access. The notebook
will render twenty separate narrated videos; it does not combine the episodes
into one compilation.
- **Assistant/manual intake:** describe the topic spread, concept/problem
  counts, formats, and target exam in plain language. The saved JSON manifest
  remains the reviewable source of truth; a natural-language brief does not
  approve physics or storyboards.

## Creative direction and review

Use the high-level teaching goals of intuition-first visuals, conversational
first-principles reasoning, and explicit mathematical structure, but make the
Saem Physics narration and execution original. Do not copy any creator's recognizable
composition, drawings, scripts, narration, or signature pacing, and do not
reproduce textbook prose, figures, or exam questions. Keep the color palette
semantic, animate the physical quantities, show assumptions and units, and
hold a diagram long enough for learners to inspect it. Each episode remains a
draft until the teacher checks the physics, source references, and visual
interpretation.
