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
        # FIXED: Using the correct, valid model name
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest", 
            contents=f"{system_instruction}\n\nUser brief: {prompt}"
        )
        raw_text = response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        sys.exit(1)

    # Clean markdown formatting if present
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
    output_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Successfully wrote generated request to {output_path}")

if __name__ == "__main__":
    main()
