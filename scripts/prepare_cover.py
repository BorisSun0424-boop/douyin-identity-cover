#!/usr/bin/env python3
"""Normalize a cover to 1080x1920 and export a centered 1080x1440 crop.

Uses Pillow when available. On macOS it falls back to the built-in `sips`
command. The script does not judge visual safety; inspect both outputs.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MASTER = (1080, 1920)
PREVIEW = (1080, 1440)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Source PNG or JPEG")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--slug", default="douyin-cover")
    return parser.parse_args()


def crop_box(width: int, height: int, ratio: float) -> tuple[int, int, int, int]:
    current = width / height
    if current > ratio:
        crop_width = round(height * ratio)
        left = (width - crop_width) // 2
        return left, 0, left + crop_width, height
    crop_height = round(width / ratio)
    top = (height - crop_height) // 2
    return 0, top, width, top + crop_height


def prepare_with_pillow(source: Path, master: Path, preview: Path) -> None:
    from PIL import Image

    with Image.open(source) as image:
        image = image.convert("RGB")
        image = image.crop(crop_box(*image.size, MASTER[0] / MASTER[1]))
        image = image.resize(MASTER, Image.Resampling.LANCZOS)
        image.save(master, format="PNG", optimize=True)
        top = (MASTER[1] - PREVIEW[1]) // 2
        image.crop((0, top, PREVIEW[0], top + PREVIEW[1])).save(
            preview, format="PNG", optimize=True
        )


def sips_dimensions(source: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(source)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    values: dict[str, int] = {}
    for line in result.splitlines():
        if ":" in line:
            key, value = line.strip().split(":", 1)
            if value.strip().isdigit():
                values[key] = int(value.strip())
    return values["pixelWidth"], values["pixelHeight"]


def prepare_with_sips(source: Path, master: Path, preview: Path) -> None:
    width, height = sips_dimensions(source)
    left, top, right, bottom = crop_box(width, height, MASTER[0] / MASTER[1])
    crop_width, crop_height = right - left, bottom - top
    with tempfile.TemporaryDirectory(prefix="douyin-cover-") as temp_dir:
        cropped = Path(temp_dir) / "cropped.png"
        subprocess.run(
            [
                "sips",
                "-c",
                str(crop_height),
                str(crop_width),
                str(source),
                "--out",
                str(cropped),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            [
                "sips",
                "-z",
                str(MASTER[1]),
                str(MASTER[0]),
                str(cropped),
                "--out",
                str(master),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
    shutil.copy2(master, preview)
    subprocess.run(
        ["sips", "-c", str(PREVIEW[1]), str(PREVIEW[0]), str(preview)],
        check=True,
        stdout=subprocess.DEVNULL,
    )


def main() -> int:
    args = parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Source image not found: {source}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    master = args.output_dir / f"{args.slug}-9x16.png"
    preview = args.output_dir / f"{args.slug}-3x4-preview.png"

    try:
        import PIL  # noqa: F401
    except ImportError:
        if shutil.which("sips") is None:
            raise SystemExit(
                "Install Pillow (`python3 -m pip install Pillow`) or run on macOS with sips."
            )
        prepare_with_sips(source, master, preview)
        backend = "sips"
    else:
        prepare_with_pillow(source, master, preview)
        backend = "Pillow"

    print(f"backend={backend}")
    print(f"master={master}")
    print(f"preview={preview}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
