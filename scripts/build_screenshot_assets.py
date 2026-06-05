#!/usr/bin/env python3
"""Build compressed screenshot assets from evidence indexes."""

from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
ASSET_ROOT = ROOT / "assets" / "screenshots"

MODULES = {
    "screenshot-evidence.md": "shanghanlun",
    "jingui-screenshot-evidence.md": "jingui",
    "zhongjing-xinfa-screenshot-evidence.md": "zhongjing-xinfa",
    "clinical-cases-screenshot-evidence.md": "clinical-cases",
    "bagang-screenshot-evidence.md": "bagang",
    "fuyang-screenshot-evidence.md": "fuyang",
    "yijinjing-screenshot-evidence.md": "yijinjing",
    "huangdi-screenshot-evidence.md": "huangdi",
    "bencao-screenshot-evidence.md": "bencao",
    "acupuncture-screenshot-evidence.md": "acupuncture",
    "tianji-screenshot-evidence.md": "tianji",
}

def entry_lines(text: str) -> list[str]:
    return text.splitlines()


def compress_image(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as image:
        image = image.convert("RGB")
        image.thumbnail((1280, 1280))
        image.save(dst, "WEBP", quality=70, method=6)


def build_module(evidence: Path, module: str) -> tuple[int, int]:
    lines = entry_lines(evidence.read_text(encoding="utf-8"))
    output: list[str] = []
    image_index = 0
    written = 0

    for line in lines:
        if "截图路径：" not in line:
            output.append(line)
            continue

        src_text = line.split("截图路径：", 1)[1].strip()
        src = Path(src_text)
        image_index += 1
        if not src.is_absolute():
            output.append(line)
            continue
        dst_rel = Path("assets") / "screenshots" / module / f"{image_index:04d}.webp"
        dst = ROOT / dst_rel
        if not src.exists():
            raise FileNotFoundError(src)

        compress_image(src, dst)
        output.append(f"  - 截图路径：{dst_rel.as_posix()}")
        written += 1

    evidence.write_text("\n".join(output) + "\n", encoding="utf-8")
    return image_index, written


def main() -> int:
    total_seen = 0
    total_written = 0

    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    for evidence_name, module in MODULES.items():
        evidence = REFERENCES / evidence_name
        if not evidence.exists():
            continue
        seen, written = build_module(evidence, module)
        total_seen += seen
        total_written += written
        print(f"{evidence_name}: {written}/{seen}")

    print(f"compressed assets: {total_written}/{total_seen}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
