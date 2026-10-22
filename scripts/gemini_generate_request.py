#!/usr/bin/env python3
"""
Generate a studio_request.json using Gemini based on a plain-language brief.
"""

import json
import os
import sys
from pathlib import Path

try:
    from google import genai
except ImportError:
    print("Error: google-genai module not found. Please install it.", file=sys.stderr)
    sys.exit(1)

def main():
    prompt = os.environ.get("GEMINI_PROMPT", "").strip()
    output_path = Path(os.environ.get("REQUEST_OUTPUT_PATH", "config/generated_request.json"))

    if not prompt:
        print("Error: GEMINI_PROMPT environment variable is empty.", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY secret is not set.", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    system_instruction = """You are an assistant that generates a valid studio_request.json for the SaemPhysics repository.

The JSON must strictly follow this schema:
- schema_version: 1 (required)
- run_id: string (optional, descriptive name for this run)
- output_dir: string (optional, default "output/studio")
- tasks: array of 1-50 task objects

Each task object requires:
- id: unique string identifier (e.g., "matrix_build", "lesson_plan")
- action: one of the supported actions below
- params: object with action-specific parameters (optional)
- depends_on: array of task ids that must complete first (optional)

Supported actions:
- content.initialize: Initialize content database
- content.summary: Summarize a concept
- content.solve: Solve a physics problem
- content.compile_lesson: Compile a lesson from solved problems
- math.solve_linear: Solve linear algebra system
- physics.constant_acceleration: Solve constant acceleration kinematics
- exam.recommend: Recommend high-yield topics for an exam
- exam.backtest: Backtest prediction accuracy
- exam.forecast: Forecast topic distribution for future exam
- matrix.build: Build concept-to-source matrix from books/papers
- video.lesson_plan: Generate video lesson plan from matrix

Example valid request:
{
  "schema_version": 1,
  "run_id": "jee-kinematics-planning",
  "output_dir": "output/studio",
  "tasks": [
    {
      "id": "matrix",
      "action": "matrix.build",
      "params": {
        "exam_papers": "exam_papers",
        "books": "book"
      }
    },
    {
      "id": "lesson",
      "action": "video.lesson_plan",
      "depends_on": ["matrix"],
      "params": {
        "matrix": {"$ref": "matrix#/network"},
        "concept_ids": ["physics:kinematics"],
        "seed": 2026,
        "history": "output/video_learning_history.json"
      }
    }
  ]
}

Return ONLY the raw JSON object. Do NOT include markdown code fences (```json or ```), explanations, or any text outside the JSON."""

    print(f"🤖 Generating studio request for prompt:")
    print(f"   {prompt}")
    print()

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",  # Stable, fast, free tier
            contents=f"{system_instruction}\n\nUser brief: {prompt}"
        )
        raw_text = response.text.strip()
        print(f"✅ Gemini response received ({len(raw_text)} characters)")
    except Exception as e:
        print(f"❌ Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

    # Clean markdown formatting if present
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    if raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
    raw_text = raw_text.strip()

    if not raw_text:
        print("❌ Gemini returned empty response", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(raw_text)
        print(f"✅ JSON parsed successfully")
        
        # Validate structure
        if not isinstance(data, dict):
            print("❌ Generated JSON must be an object", file=sys.stderr)
            sys.exit(1)
        if "tasks" not in data:
            print("❌ Generated JSON missing 'tasks' array", file=sys.stderr)
            sys.exit(1)
        if not isinstance(data["tasks"], list):
            print("❌ 'tasks' must be an array", file=sys.stderr)
            sys.exit(1)
        
        print(f"✅ Request contains {len(data['tasks'])} tasks")
        
    except json.JSONDecodeError as exc:
        print(f"❌ Gemini did not return valid JSON: {exc}", file=sys.stderr)
        print(f"Raw response:\n{raw_text}", file=sys.stderr)
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"✅ Saved generated request to {output_path}")
    print()
    print("Next steps:")
    print("  1. Review the generated request in your editor")
    print("  2. Run: python -m studio_engine validate --request config/generated_request.json")
    print("  3. Run: python -m studio_engine run --request config/generated_request.json")

if __name__ == "__main__":
    main()
