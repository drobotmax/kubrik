#!/usr/bin/env python3
"""Programmatic character counting and optional auto-fix for creatives.md."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


FIELD_RE = re.compile(r"^(\s*-\s+\*\*)([^*]+)(:\*\*\s*)(.*)$")
COUNT_RE = re.compile(r"\s+\((\d+)\s+chars\)\s*$")
VARIANT_RE = re.compile(r"^###\s+(.*)$")

PLATFORM_RULES = {
    "VK Feed": {
        "Primary text": 125,
        "Headline": 40,
        "Description": 30,
    },
    "VK Stories": {},
    "Yandex Search": {
        "Заголовок 1": 56,
        "Заголовок 2": 30,
        "Текст": 81,
        "Текст (исправлено)": 81,
        "Display URL": 20,
        "Сайтлинки": 30,
    },
    "Yandex RSYA": {
        "Заголовок": 56,
        "Текст": 81,
    },
    "Google Search": {
        "Headline 1": 30,
        "Headline 2": 30,
        "Headline 3": 30,
        "Description 1": 90,
        "Description 2": 90,
        "Display URL path": 15,
    },
    "Google Display": {
        "Short headline": 30,
        "Long headline": 90,
        "Description": 90,
    },
    "Instagram Reels": {
        "Caption": 2200,
    },
}

PLATFORM_PREFIXES = [
    ("VK Feed", "VK Feed"),
    ("VK Stories", "VK Stories"),
    ("Yandex Search", "Яндекс Поиск"),
    ("Yandex RSYA", "Яндекс РСЯ"),
    ("Google Search", "Google Search"),
    ("Google Display", "Google Display"),
    ("Instagram Reels", "Instagram Reels"),
]

SAFE_REPLACEMENTS = [
    ("подземный паркинг", "паркинг"),
    ("Онлайн-показ", "Показ онлайн"),
    ("онлайн-показ", "показ онлайн"),
    ("Покажем квартиру онлайн", "Покажем онлайн"),
    ("покажем квартиру онлайн", "покажем онлайн"),
    ("Запишитесь сейчас!", "Запишитесь!"),
    ("запишитесь сейчас!", "запишитесь!"),
    ("прямо во дворе", "во дворе"),
    ("прямо у дома", "у дома"),
    ("Центральный район", "Центр"),
    ("центральный район", "центр"),
    ("Комфорт+ класс", "Комфорт+"),
    ("качественных объектов", "жилья"),
    ("качественного предложения", "предложения"),
]

TRAILING_SNIPPETS = [
    " Запишитесь на показ!",
    " Запишитесь!",
    " Узнайте цены!",
    " Узнайте цены",
    " Узнайте больше",
    " Звоните!",
    " Запросите расчёт!",
    " Запросите расчёт",
    " Онлайн-показ за 15 минут",
    " Онлайн-показ за 15 мин",
    " Показ онлайн",
]


@dataclass
class Finding:
    variant: str
    platform: str
    label: str
    actual: int
    limit: int | None
    claimed: int | None
    changed: bool
    message: str


@dataclass
class VariantContext:
    title: str
    platform: str
    findings: list[Finding] = field(default_factory=list)


def count_chars(text: str) -> int:
    return len(text)


def strip_claimed_count(value: str) -> tuple[str, int | None]:
    match = COUNT_RE.search(value)
    if not match:
        return value.rstrip(), None
    return value[: match.start()].rstrip(), int(match.group(1))


def detect_platform(heading: str) -> str | None:
    for platform, prefix in PLATFORM_PREFIXES:
        if heading.startswith(prefix):
            return platform
    return None


def limit_for(platform: str | None, label: str) -> int | None:
    if not platform:
        return None
    return PLATFORM_RULES.get(platform, {}).get(label)


def update_count_suffix(label: str, value: str, actual: int) -> str:
    if label in {
        "CTA",
        "Visual brief",
        "Hook/Angle",
        "Сегмент ЦА",
        "Примечание",
        "Display URL",
        "Display URL path",
        "Сайтлинки",
    }:
        return value
    return f"{value} ({actual} chars)"


def trim_display_url(value: str, limit: int) -> tuple[str, bool]:
    raw = value.strip()
    if not raw:
        return raw, False
    prefix = "/" if raw.startswith("/") else ""
    segments = [segment.strip() for segment in raw.strip("/").split("/") if segment.strip()]
    changed = False
    trimmed: list[str] = []
    for segment in segments:
        if len(segment) > limit:
            trimmed.append(segment[:limit].rstrip("-_"))
            changed = True
        else:
            trimmed.append(segment)
    return prefix + "/".join(trimmed), changed


def trim_pipe_list(value: str, limit: int) -> tuple[str, bool]:
    parts = [part.strip() for part in value.split("|")]
    changed = False
    trimmed: list[str] = []
    for part in parts:
        text, _claimed = strip_claimed_count(part)
        if len(text) > limit:
            trimmed.append(shrink_text(text, limit))
            changed = True
        else:
            trimmed.append(text)
    return " | ".join(trimmed), changed


def shrink_text(text: str, limit: int) -> str:
    current = normalize_whitespace(text)
    if len(current) <= limit:
        return current

    for old, new in SAFE_REPLACEMENTS:
        if old in current and len(current) > limit:
            current = normalize_whitespace(current.replace(old, new))

    for snippet in TRAILING_SNIPPETS:
        if current.endswith(snippet) and len(current) > limit:
            current = normalize_whitespace(current[: -len(snippet)].rstrip(" .,!"))

    while len(current) > limit and "." in current:
        head, _sep, _tail = current.rpartition(".")
        if not head.strip():
            break
        candidate = head.strip()
        if len(candidate) < len(current):
            current = candidate
            continue
        break

    if len(current) <= limit:
        return current

    words = current.split()
    while words and len(" ".join(words)) > limit:
        words.pop()
    current = " ".join(words).rstrip(" -,:;.!?")

    if len(current) <= limit and current:
        return current
    return text


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def measured_length(label: str, value: str) -> int:
    if label == "Display URL":
        return max((len(part) for part in value.strip("/").split("/") if part), default=0)
    if label == "Display URL path":
        return max((len(part.strip()) for part in value.split("/") if part.strip()), default=0)
    if label == "Сайтлинки":
        items = []
        for part in value.split("|"):
            text, _claimed = strip_claimed_count(part.strip())
            if text:
                items.append(len(text))
        return max(items, default=0)
    return count_chars(value)


def process_line(
    line: str,
    variant: VariantContext | None,
    mode: str,
    overflow_policy: str,
) -> tuple[str, VariantContext | None]:
    variant_match = VARIANT_RE.match(line)
    if variant_match:
        heading = variant_match.group(1).strip()
        return line, VariantContext(title=heading, platform=detect_platform(heading) or "")

    if variant is None:
        return line, variant

    field_match = FIELD_RE.match(line)
    if not field_match:
        return line, variant

    prefix, label, separator, raw_value = field_match.groups()
    value, claimed = strip_claimed_count(raw_value)
    actual = measured_length(label, value)
    limit = limit_for(variant.platform, label)
    changed = claimed is not None and claimed != actual
    message = "count synced"

    if mode == "fix" and limit is not None:
        if label == "Display URL path":
            segments = [segment.strip() for segment in value.split("/") if segment.strip()]
            if any(len(segment) > limit for segment in segments):
                new_value = " / ".join(shrink_text(segment, limit) for segment in segments)
                changed = changed or new_value != value
                value = new_value
                actual = measured_length(label, value)
                message = "overflow trimmed"
        elif label == "Display URL":
            new_value, trimmed = trim_display_url(value, limit)
            if trimmed:
                changed = True
                value = new_value
                actual = measured_length(label, value)
                message = "overflow trimmed"
        elif label == "Сайтлинки":
            new_value, trimmed = trim_pipe_list(value, limit)
            if trimmed:
                changed = True
                value = new_value
                actual = measured_length(label, value)
                message = "overflow trimmed"
        elif overflow_policy == "trim" and actual > limit:
            new_value = shrink_text(value, limit)
            if len(new_value) <= limit and new_value != value:
                value = new_value
                actual = measured_length(label, value)
                changed = True
                message = "overflow trimmed"

    overflow = limit is not None and actual > limit
    if overflow and message == "count synced":
        message = "overflow detected"
    elif changed and message == "count synced":
        message = "count corrected"

    variant.findings.append(
        Finding(
            variant=variant.title,
            platform=variant.platform or "Unknown",
            label=label,
            actual=actual,
            limit=limit,
            claimed=claimed,
            changed=changed,
            message=message,
        )
    )

    new_value = update_count_suffix(label, value, actual)
    return f"{prefix}{label}{separator}{new_value}", variant


def render_report(path: Path, variants: Iterable[VariantContext]) -> str:
    findings = [finding for variant in variants for finding in variant.findings]
    checked = [finding for finding in findings if finding.limit is not None]
    overflows = [finding for finding in checked if finding.actual > finding.limit]
    corrected = [finding for finding in findings if finding.changed]

    lines = [
        f"# Character Guard Report: {path.name}",
        "",
        f"- Checked fields with hard limits: {len(checked)}",
        f"- Corrected count annotations: {len(corrected)}",
        f"- Remaining overflows: {len(overflows)}",
        "",
    ]

    if overflows:
        lines.append("## Remaining overflows")
        lines.append("")
        for finding in overflows:
            lines.append(
                f"- {finding.variant} - {finding.label}: {finding.actual}/{finding.limit}"
            )
        lines.append("")

    if corrected:
        lines.append("## Updated fields")
        lines.append("")
        for finding in corrected[:40]:
            claimed = "n/a" if finding.claimed is None else str(finding.claimed)
            limit = "-" if finding.limit is None else str(finding.limit)
            lines.append(
                f"- {finding.variant} - {finding.label}: claimed {claimed}, actual {finding.actual}, limit {limit} ({finding.message})"
            )
        if len(corrected) > 40:
            lines.append(f"- ... and {len(corrected) - 40} more")
        lines.append("")

    if not overflows and not corrected:
        lines.append("All counted fields are already aligned with their annotations and limits.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to creatives.md")
    parser.add_argument("--mode", choices=["check", "fix"], default="check")
    parser.add_argument(
        "--overflow-policy",
        choices=["report", "trim"],
        default="report",
        help="How to handle over-limit fields in fix mode",
    )
    parser.add_argument("--output", type=Path, help="Write updated markdown to a new file")
    parser.add_argument("--in-place", action="store_true", help="Rewrite input file")
    parser.add_argument("--report", type=Path, help="Write markdown report to a file")
    args = parser.parse_args()

    if args.output and args.in_place:
        parser.error("--output and --in-place are mutually exclusive")

    original = args.input.read_text(encoding="utf-8")
    lines = original.splitlines()
    rewritten: list[str] = []
    variants: list[VariantContext] = []
    current: VariantContext | None = None

    for line in lines:
        new_line, current = process_line(
            line=line,
            variant=current,
            mode=args.mode,
            overflow_policy=args.overflow_policy,
        )
        if current and VARIANT_RE.match(line) and (not variants or variants[-1] is not current):
            variants.append(current)
        rewritten.append(new_line)

    report = render_report(args.input, variants)

    destination = args.output
    if args.in_place:
        destination = args.input
    if destination:
        destination.write_text("\n".join(rewritten) + "\n", encoding="utf-8")

    if args.report:
        args.report.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
