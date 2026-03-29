#!/usr/bin/env python3
"""
Build a unified knowledge base from SRT subtitles and Whisper transcripts.
Outputs a single markdown file organized by lesson number.
"""

import os
import re
import glob

COURSE_DIR = os.path.dirname(os.path.abspath(__file__))
SUBS_DIR = os.path.join(COURSE_DIR, "subs")
TRANSCRIPTS_DIR = os.path.join(COURSE_DIR, "transcripts")
OUTPUT_FILE = os.path.join(COURSE_DIR, "targeting-course-knowledge.md")


def clean_srt(text):
    """Remove SRT formatting: timestamps, sequence numbers, duplicate lines."""
    # Remove sequence numbers (lines that are just digits)
    text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)
    # Remove timestamps
    text = re.sub(r'\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[.,]\d{3}', '', text)
    # Remove HTML-like tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove blank lines and collapse whitespace
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    # Remove duplicate consecutive lines (common in auto-subs)
    deduped = []
    for line in lines:
        if not deduped or line != deduped[-1]:
            deduped.append(line)
    return ' '.join(deduped)


def extract_lesson_number(filename):
    """Extract lesson/order number from filename for sorting."""
    # Try patterns like /1, /2, /4/1, /4/2, etc.
    m = re.search(r'[/⧸](\d+)(?:[/⧸](\d+))?', filename)
    if m:
        main = int(m.group(1))
        sub = int(m.group(2)) if m.group(2) else 0
        return (main, sub)
    # Try "Урок N"
    m = re.search(r'[Уу]рок\s*(\d+)', filename)
    if m:
        return (int(m.group(1)), 0)
    return (999, 0)


def extract_title(filename):
    """Extract clean title from filename."""
    # Remove video ID in brackets
    title = re.sub(r'\s*\[[\w-]+\]', '', filename)
    # Remove file extension
    title = re.sub(r'\.(ru\.srt|srt|txt)$', '', title)
    # Clean up special chars from yt-dlp
    title = title.replace('⧸', '/').replace('：', ':').replace('？', '?').replace('｜', '|')
    return title.strip()


def main():
    entries = []

    # Process SRT files
    for srt_file in glob.glob(os.path.join(SUBS_DIR, "*.srt")):
        basename = os.path.basename(srt_file)
        with open(srt_file, 'r', encoding='utf-8') as f:
            raw = f.read()
        text = clean_srt(raw)
        title = extract_title(basename)
        order = extract_lesson_number(basename)
        entries.append({
            'title': title,
            'order': order,
            'text': text,
            'source': 'auto-subtitles'
        })

    # Process Whisper transcripts
    for txt_file in glob.glob(os.path.join(TRANSCRIPTS_DIR, "*.txt")):
        basename = os.path.basename(txt_file)
        with open(txt_file, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        title = extract_title(basename)
        order = extract_lesson_number(basename)
        entries.append({
            'title': title,
            'order': order,
            'text': text,
            'source': 'whisper-transcription'
        })

    # Sort by lesson number
    entries.sort(key=lambda e: e['order'])

    # Renumber bonus videos (999) starting from next available number
    max_numbered = max(
        (e['order'][0] for e in entries if e['order'][0] < 999), default=0
    )
    bonus_counter = max_numbered + 1
    for entry in entries:
        if entry['order'][0] == 999:
            entry['order'] = (bonus_counter, 0)
            bonus_counter += 1

    # Build markdown
    lines = [
        "# Базовый курс по таргетированной рекламе",
        "",
        "Источник: YouTube-плейлист (Weberg)",
        f"Уроков: {len(entries)}",
        "",
        "---",
        "",
    ]

    for entry in entries:
        lesson_num = entry['order']
        if lesson_num[1] > 0:
            num_str = f"{lesson_num[0]}.{lesson_num[1]}"
        else:
            num_str = str(lesson_num[0])

        lines.append(f"## Урок {num_str}: {entry['title']}")
        lines.append(f"*Источник: {entry['source']}*")
        lines.append("")
        lines.append(entry['text'])
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Knowledge base written to: {OUTPUT_FILE}")
    print(f"Total entries: {len(entries)}")
    total_chars = sum(len(e['text']) for e in entries)
    print(f"Total characters: {total_chars:,}")


if __name__ == "__main__":
    main()
