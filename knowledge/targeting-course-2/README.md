# Targeting Course 2

Second targeting course (separate from Weberg course in targeting-course/).

- **Source:** YouTube playlist `PLkOvrhXD_9PuhlIfuG0qw8dThhyWxARWO`
- **Videos:** ~51 lessons
- **Google Doc:** `1ozs8HUozmr4kAh36sn0AgTwTsBBhMA2hRwUfP_ZYN-g`
- **Status:** URLs collected, awaiting subtitle download and transcription

## Pipeline

1. Download auto-subs: `yt-dlp --write-auto-sub --sub-lang ru --skip-download -o "subs/%(playlist_index)s - %(title)s.%(ext)s" "PLkOvrhXD_9PuhlIfuG0qw8dThhyWxARWO"`
2. Whisper transcription for videos without good subs
3. Run `python build-knowledge-base.py` to build unified knowledge file
