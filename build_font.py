#!/usr/bin/env python3

"""Build saltcandy123font from SVG files"""

import argparse
import json
import pathlib
import re
import xml.dom.minidom

import fontforge

BASE_DIR = pathlib.Path(__file__).parent


def build_saltcandy123font(*, version: str) -> fontforge.font:
    font = fontforge.font()
    font.fontname = "saltcandy123font"
    font.fullname = font.fontname
    font.familyname = font.fontname
    font.copyright = "Copyright (C) saltcandy123"
    font.weight = "Regular"
    font.os2_weight = 400
    font.version = version

    for svg_path in BASE_DIR.joinpath("glyphs").iterdir():
        match = re.search("^u([0-9a-f]{4}).svg$", svg_path.name)
        if not match:
            continue
        code = int(match.group(1), 16)
        glyph = font.createChar(code)
        glyph.importOutlines(str(svg_path))
        with xml.dom.minidom.parse(str(svg_path)) as doc:
            glyph.width = int(doc.childNodes[0].getAttribute("width"))

    return font


def generate_npm_package_metadata(*, version=str) -> dict:
    return {
        "name": "@saltcandy123/saltcandy123font",
        "version": version,
        "description": "A simple handwritten font created by @saltcandy123",
        "repository": "https://github.com/saltcandy123/saltcandy123font",
        "author": "saltcandy123",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("font_version", help="font version (e.g. 0.1.2)")
    args = parser.parse_args()

    dist_dir = BASE_DIR.joinpath("dist")
    dist_dir.mkdir(exist_ok=True)

    font = build_saltcandy123font(version=args.font_version)

    for ext in ["ttf", "woff"]:
        font.generate(str(dist_dir.joinpath(f"saltcandy123font.{ext}")))

    package_metadata = generate_npm_package_metadata(version=args.font_version)
    with open(dist_dir.joinpath("package.json"), "w") as f:
        json.dump(package_metadata, f, indent=2)

    with open(dist_dir.joinpath("README.md"), "w") as f:
        with open(BASE_DIR.joinpath("README-npm.md")) as f_src:
            f.write(f_src.read())


if __name__ == "__main__":
    main()
