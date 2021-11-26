#!/usr/bin/env python3

"""Build saltcandy123font from SVG files"""

import argparse
import pathlib
import re
import xml.dom.minidom

import fontforge


def build_saltcandy123font(*, version: str) -> fontforge.font:
    font = fontforge.font()
    font.fontname = "saltcandy123font"
    font.fullname = font.fontname
    font.familyname = font.fontname
    font.copyright = "Copyright (C) saltcandy123"
    font.weight = "Regular"
    font.os2_weight = 400
    font.version = version

    glyphs_dir = pathlib.Path(__file__).parent.parent.joinpath("glyphs")
    all_svg_paths = list(glyphs_dir.glob("**/*.svg"))

    for svg_path in all_svg_paths:
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        metavar="FILE",
        default="saltcandy123font.ttf",
        type=pathlib.Path,
        help="write a font to FILE",
    )
    parser.add_argument(
        "-t",
        metavar="FONT_VERSION",
        default="(None)",
        help="build a font as FONT_VERSION",
    )
    args = parser.parse_args()
    outfile_path = args.o
    font_version = args.t

    font = build_saltcandy123font(version=font_version)
    font.generate(str(outfile_path))


if __name__ == "__main__":
    main()
