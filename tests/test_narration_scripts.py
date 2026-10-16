from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

from content_engine.batch import load_batch, validate_batch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "episodes" / "batch_001" / "narration.json"
WORD_PATTERN = re.compile(r"\b[\w]+(?:['’][\w]+)*\b")


class NarrationScriptTests(unittest.TestCase):
    def test_all_scripts_match_animation_beats_and_timecodes(self) -> None:
        script = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
        batch = load_batch(ROOT / "data" / "video_batches" / "batch_001.json")
        plan = validate_batch(batch, ROOT)

        self.assertEqual(script["batch_id"], batch["batch_id"])
        self.assertEqual(
            {episode["episode_id"] for episode in script["episodes"]},
            {episode["id"] for episode in batch["episodes"]},
        )
        self.assertEqual(len(script["episodes"]), 10)

        for episode in script["episodes"]:
            for format_name in ("vertical", "horizontal"):
                video_id = f"{episode['episode_id']}-{format_name}"
                render_brief = next(item for item in plan if item["video_id"] == video_id)
                cues = episode[format_name]
                beats = render_brief["story_beats"]
                self.assertEqual(
                    [cue["beat"] for cue in cues],
                    [beat["name"] for beat in beats],
                    video_id,
                )

                cursor = 0
                total_words = 0
                timecodes = script["timecodes_seconds"][format_name]
                for cue, beat in zip(cues, beats):
                    start, end = timecodes[cue["beat"]]
                    self.assertEqual(start, cursor, video_id)
                    self.assertEqual(end - start, beat["duration_seconds"], video_id)
                    self.assertIsInstance(cue["text"], str)
                    self.assertTrue(cue["text"].strip(), video_id)
                    word_count = len(WORD_PATTERN.findall(cue["text"]))
                    total_words += word_count
                    self.assertLessEqual(
                        word_count / (end - start),
                        2.5,
                        f"{video_id} {cue['beat']} exceeds 150 words per minute",
                    )
                    cursor = end

                self.assertEqual(cursor, render_brief["duration_seconds"], video_id)
                if format_name == "vertical":
                    self.assertGreaterEqual(total_words, 90, video_id)
                    self.assertLessEqual(total_words, 145, video_id)
                else:
                    self.assertGreaterEqual(total_words, 300, video_id)
                    self.assertLessEqual(total_words, 420, video_id)


if __name__ == "__main__":
    unittest.main()
