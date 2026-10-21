# SaemPhysics Task Cookbook

This document is a practical guide to every actionable task in the SaemPhysics repository. 
It is organized by **Goal**. For each task, it defines the **Input** you must provide, the **Command** to run, and the **Output** you will receive.

---

## 🎬 1. Render a Video Batch (The Core Pipeline)
**Goal:** Generate high-quality, calculation-backed Manim animations (silent drafts) for a batch of physics topics.
*   **Input:** A validated JSON manifest in `data/video_batches/` (e.g., `batch_001.json`) with `"status": "approved-for-storyboarding"`.
*   **Command (GitHub Actions):**
    1. Go to **Actions** -> **Render approved video batch** -> **Run workflow**.
    2. Manifest path: `data/video_batches/batch_001.json`
    3. Quality: `preview` (for testing) or `high` (for final).
    4. Narration: `false` (for silent drafts).
*   **Command (Local Terminal):**
```bash
    python tools/render_video_batch.py \
      --manifest data/video_batches/batch_001.json \
      --output-dir output/batch_001_render \
      --quality preview \
      --narration off
```
*   **Output:** Silent MP4 files (vertical 9:16 and horizontal 16:9) in the `output/` directory or GitHub Actions Artifacts.

## 🤖 2. AI-Assisted Lesson Planning (Gemini Studio)
**Goal:** Use AI to generate a structured studio request from a plain-English prompt.
*   **Input:** A simple text prompt (e.g., "Create a JEE kinematics batch about reading motion graphs").
*   **Command (GitHub Actions):**
    1. Go to **Actions** -> **Gemini studio automation** -> **Run workflow**.
    2. Paste your prompt in the input box.
*   **Command (Local Terminal):**
```bash
    python -m content_engine studio \
      --brief "Create a JEE kinematics batch about reading motion graphs" \
      --episodes 6 --formats both
```
*   **Output:** A structured JSON file saved in `requests/` or `config/generated_request.json`. This is a *plan*, not a video. You must review it and convert it into a `batch_*.json` manifest.

##  3. Exam Forecasting & Topic Ranking
**Goal:** Analyze historical exam data to predict high-yield topics for JEE/NEET and generate practice test blueprints.
*   **Input:** Populated `data/exam_question_metadata.csv` (requires manual verification of rows to `review_status: verified`).
*   **Command (Topic Ranking):**
```bash
    python -m exam_engine recommend --exam jee-advanced --as-of-year 2026 \
      --output output/jee-advanced-video-ideas.md
```
*   **Command (Mock Test Blueprint):**
```bash
    python -m exam_engine predict-test --exam jee-advanced --as-of-year 2026 \
      --questions 10 --simulations 10000 --seed 2026 \
      --output output/jee-advanced-physics-blueprint.json
```
*   **Output:** Markdown files with topic recommendations or JSON files with statistically probable test structures in `output/`.

## 📚 4. Process Books and Exam Papers (The Matrix Pipeline)
**Goal:** Convert PDF/DOCX books and papers into Markdown, then map them to your physics concept graph.
*   **Input:** PDF or DOCX files placed in the `book/` or `exam_papers/` directories.
*   **Command (Convert to Markdown):**
```bash
    python convert_pdfs.py
```
*   **Command (Build Concept Matrix):**
```bash
    python matrix_pipeline.py
```
*   **Output:** Text-based `.md` files in the same folders, and a comprehensive `output/matrix_network.json` linking sources to physics/math concepts.

## 🧮 5. Solve Physics & Math Problems (Calculation Engine)
**Goal:** Run deterministic solvers to get exact numbers and check residuals before animating.
*   **Input:** CLI arguments defining the problem (vectors, matrices, kinematics).
*   **Command (Kinematics):**
```bash
    python -m physics_engine constant-acceleration \
      --position-m '[0,0]' --velocity-m-per-s '[3,2]' \
      --acceleration-m-per-s2 '[0,-9.8]' --time-s 1
```
*   **Command (Linear Algebra):**
```bash
    python -m math_engine solve-linear --matrix '[[2,1],[1,3]]' --rhs '[5,7]'
```
*   **Output:** JSON printed to the terminal containing the calculated outputs, assumptions, and residual checks.

## 🎙️ 6. Analyze and Clone Voice (Audio Pipeline)
**Goal:** Check the technical quality of your voice sample and generate offline AI-cloned narration.
*   **Input:** A PCM WAV file named `saem_voice_sample.wav` in the root directory.
*   **Command (Analyze Quality):**
```bash
    python tools/analyze_voice_sample.py saem_voice_sample.wav
```
*   **Command (Render with Local Voice):**
```bash
    python tools/render_video_batch.py \
      --manifest data/video_batches/batch_001.json \
      --output-dir output/batch_001_voiced \
      --narration local
```
*   **Output:** A JSON report of your audio quality (RMS, clipping, DC offset) OR fully voiced MP4 videos using your cloned voice.

## 🗄️ 7. Build the Content Network (Database)
**Goal:** Initialize the local SQLite database that links sources, papers, questions, and concepts.
*   **Input:** CSV files in `data/` (`sources.csv`, `papers.csv`, `questions.csv`) and `knowledge/` (`concepts.csv`, `links.csv`).
*   **Command:**
```bash
    python -m content_engine init
    python -m content_engine papers
```
*   **Output:** A local `saemphysics.sqlite` database file used by the recommendation and mapping engines.

---

## ⚠️ The Golden Rule of this Repository
**AI drafts, Engines calculate, Humans approve.**
Never run a render or publish a video without manually verifying the `status` in your JSON files and checking the physics derivations. The pipeline is designed to fail safely if a human approval gate is missing.
