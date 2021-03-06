#!/usr/bin/env python3

import argparse
import pathlib
import re
import xml.dom.minidom

import fontforge

BASE_DIR = pathlib.Path(__file__).parent


def build_saltcandy123font(*, tag):
    font = fontforge.font()
    font.familyname = "saltcandy123font"
    font.fullname = "saltcandy123font-Regular"
    font.fontname = font.fullname
    font.copyright = "Copyright (C) saltcandy123"
    font.weight = "Regular"
    font.os2_weight = 400
    if tag:
        font.version = tag

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag")
    args = parser.parse_args()

    dist_dir = BASE_DIR.joinpath("font-dist")
    dist_dir.mkdir(exist_ok=True)

    font_map = {
        "saltcandy123font": build_saltcandy123font(tag=args.tag),
    }
    for font_name in font_map:
        font = font_map[font_name]
        for ext in ["ttf", "woff", "woff2"]:
            font.generate(str(dist_dir.joinpath(f"{font_name}.{ext}")))


if __name__ == "__main__":
    main()
