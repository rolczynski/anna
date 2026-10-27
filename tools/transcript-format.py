#!/usr/bin/env python3
"""Print a whisper JSON transcript as "[mm:ss] text" lines, minutes from the recording's start.

Usage: python3 agent/tools/transcript-format.py FILE.json [OFFSET_SECONDS]
The JSON is what mlx_whisper writes with --output-format json. Read-only, prints to stdout. The
optional offset is added to every timestamp, for audio transcribed in pieces.
"""
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)

offset = int(sys.argv[2]) if len(sys.argv) > 2 else 0

for segment in data["segments"]:
    start = int(segment["start"]) + offset
    text = segment["text"].strip()
    if text:
        print(f"[{start // 60:02d}:{start % 60:02d}] {text}")
