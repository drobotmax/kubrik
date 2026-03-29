#!/usr/bin/env python3
"""
Build a unified knowledge base from SRT subtitles and Whisper transcripts.
Outputs a single markdown file organized by lesson number.
Adapted for targeting-course-2 playlist.
"""

import os
import re
import glob

COURSE_DIR = os.path.dirname(os.path.abspath(__file__))
SUBS_DIR = os.path.join(COURSE_DIR, "subs")
TRANSCRIPTS_DIR = os.path.join(COURSE_DIR, "transcripts")
OUTPUT_FILE = os.path.join(COURSE_DIR, "targeting-course-2-knowledge.md")


def clean_srt(text):
    """Remove SRT formatting: timestamps, sequence numbers, duplicate lines."""
    text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[.,]\d{3}', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    deduped = []
    for line in lines:
        if not deduped or line != deduped[-1]:
            deduped.append(line)
    return ' '.join(deduped)


def extract_lesson_number(filename):
    """Extract lesson/order number from filename for sorting."""
    # Try playlist index at the start: "01 - ...", "02 - ..."
    m = re.match(r'^(\d+)\s*-\s*', filename)
    if m:
        return (int(m.group(1)), 0)
    # Try patterns like /1, /2
    m = re.search(r'[/\u29F8](\d+)(?:[/\u29F8](\d+))?', filename)
    if m:
        main = int(m.group(1))
        sub = int(m.group(2)) if m.group(2) else 0
        return (main, sub)
    m = re.search(r'[Уу]рок\s*(\d+)', filename)
    if m:
        return (int(m.group(1)), 0)
    return (999, 0)


def extract_title(filename):
    """Extract clean title from filename."""
    title = re.sub(r'\s*\[[\w-]+\]', '', filename)
    title = re.sub(r'\.(ru\.srt|ru\.vtt|srt|vtt|txt)$', '', title)
    title = title.replace('\u29F8', '/').replace('\uFF1A', ':').replace('\uFF1F', '?').replace('\uFF5C', '|')
    # Remove leading playlist index
    title = re.sub(r'^\d+\s*-\s*', '', title)
    return title.strip()


def main():
    entries = []

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

    entries.sort(key=lambda e: e['order'])

    max_numbered = max(
        (e['order'][0] for e in entries if e['order'][0] < 999), default=0
    )
    bonus_counter = max_numbered + 1
    for entry in entries:
        if entry['order'][0] == 999:
            entry['order'] = (bonus_counter, 0)
            bonus_counter += 1

    lines = [
        "# Targeting Course 2 - Knowledge Base",
        "",
        "Source: YouTube playlist PLkOvrhXD_9PuhlIfuG0qw8dThhyWxARWO",
        f"Lessons: {len(entries)}",
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

        lines.append(f"## Lesson {num_str}: {entry['title']}")
        lines.append(f"*Source: {entry['source']}*")
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
