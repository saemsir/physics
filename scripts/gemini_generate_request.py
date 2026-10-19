#!/usr/bin/env python3
"""
Generate a studio_request.json using Gemini based on a plain-language brief.
This is an isolated script and does not modify any core engines.
"""

import json
import os
import sys
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("Error: google-generativeai module not found. Please install it.", file=sys.stderr)
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

    genai.configure(api_key=api_key)

    # Using flash model for faster, structured generation
    model = genai.GenerativeModel("gemini-2.0-flash")

    system_instruction = (
        "You are an assistant that generates a valid studio_request.json for the SaemPhysics repository. "
        "The JSON must strictly follow this schema: schema_version (1), optional run_id, optional output_dir, "
        "and a 'tasks' array (1-50 tasks). Each task requires a unique 'id', a supported 'action', optional 'params', "
        "and optional 'depends_on'. Supported actions include: content.initialize, content.summary, content.solve, "
        "content.compile_lesson, math.solve_linear, physics.constant_acceleration, exam.recommend, exam.backtest, "
        "matrix.build, video.lesson_plan, exam.forecast. Return ONLY the raw JSON, no markdown fences or extra text."
    )

    print(f"Generating request for prompt: {prompt}")

    try:
        response = model.generate_content(
            f"{system_instruction}\n\nUser brief: {prompt}"
        )
        raw_text = response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

    # Clean up Markdown formatting if present
    if raw_text.startswith("```json"):
        raw_text = raw_text[7:]
    if raw_text.startswith("```"):
        raw_text = raw_text[3:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3]
    raw_text = raw_text.strip()

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        print(f"Gemini did not return valid JSON: {exc}\nRaw response:\n{raw_text}", file=sys.stderr)
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Successfully wrote generated request to {output_path}")

if __name__ == "__main__":
    main()
