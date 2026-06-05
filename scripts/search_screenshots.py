#!/usr/bin/env python3
"""Rank screenshot evidence entries for Nihaisha course notes."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_FILES = [
    ROOT / "references" / "screenshot-evidence.md",
    ROOT / "references" / "jingui-screenshot-evidence.md",
    ROOT / "references" / "zhongjing-xinfa-screenshot-evidence.md",
    ROOT / "references" / "clinical-cases-screenshot-evidence.md",
    ROOT / "references" / "bagang-screenshot-evidence.md",
    ROOT / "references" / "fuyang-screenshot-evidence.md",
    ROOT / "references" / "yijinjing-screenshot-evidence.md",
    ROOT / "references" / "huangdi-screenshot-evidence.md",
    ROOT / "references" / "bencao-screenshot-evidence.md",
    ROOT / "references" / "acupuncture-screenshot-evidence.md",
    ROOT / "references" / "tianji-screenshot-evidence.md",
]


def parse_entries(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    lesson = ""
    current: dict[str, str] | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            lesson = line.removeprefix("## ").strip()
        elif line.startswith("- `"):
            match = re.match(r"- `([^`]+)` \[([^\]]+)\] (.*)", line)
            if match:
                current = {
                    "lesson": lesson,
                    "time": match.group(1),
                    "category": match.group(2),
                    "desc": match.group(3),
                    "path": "",
                }
                entries.append(current)
        elif current and line.strip().startswith("- 截图路径："):
            current["path"] = line.split("截图路径：", 1)[1].strip()
    return entries


def score_entry(entry: dict[str, str], terms: list[str]) -> int:
    hay = f"{entry['lesson']} {entry['time']} {entry['category']} {entry['desc']} {entry['path']}"
    score = 0
    for term in terms:
        if not term:
            continue
        if term in entry["desc"]:
            score += 10
        if term in entry["category"]:
            score += 4
        if term in entry["lesson"] or term in entry["path"]:
            score += 3
        if term in hay:
            score += 1
    if all(term in hay for term in terms if term):
        score += 20
    if resolve_path(entry["path"]).exists():
        score += 2
    return score


def resolve_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return ROOT / candidate


def path_status(path: str) -> str:
    if path.startswith("未上传"):
        return "not-uploaded"
    return "exists" if resolve_path(path).exists() else "missing"


def main() -> int:
    parser = argparse.ArgumentParser(description="Search ranked screenshot evidence.")
    parser.add_argument("terms", nargs="+", help="Search terms, e.g. 小柴胡汤 加减")
    parser.add_argument("-n", "--limit", type=int, default=8)
    args = parser.parse_args()

    entries = []
    for evidence in EVIDENCE_FILES:
        if evidence.exists():
            entries.extend(parse_entries(evidence.read_text(encoding="utf-8")))
    ranked = []
    for entry in entries:
        score = score_entry(entry, args.terms)
        if score > 0:
            ranked.append((score, entry))
    ranked.sort(key=lambda item: (-item[0], item[1]["lesson"], item[1]["time"]))

    for score, entry in ranked[: args.limit]:
        print(f"- {entry['lesson']} {entry['time']} [{entry['category']}] score={score} path={path_status(entry['path'])}")
        print(f"  {entry['desc']}")
        print(f"  截图路径：{entry['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
