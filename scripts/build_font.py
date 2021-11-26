#!/usr/bin/env python3

"""Build saltcandy123font from SVG files"""

import argparse
import pathlib
import re
import typing
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
    font.encoding = "UnicodeBmp"
    font.hasvmetrics = 1  # required to enable vwidth settings

    # Add lookup subtable for vertical writing
    font.addLookup(
        "gsub_vert",
        "gsub_single",
        (),
        (
            (
                "vert",
                (("DFLT", ("dflt",)),),
            ),
        ),
    )
    font.addLookupSubtable("gsub_vert", "vert")

    glyphs_dir = pathlib.Path(__file__).parent.parent.joinpath("glyphs")
    all_svg_paths = list(glyphs_dir.glob("**/*.svg"))

    # Import basic glyph outlines (e.g. u3041.svg)
    for svg_path in all_svg_paths:
        match = re.search("^u([0-9a-f]{4}).svg$", svg_path.name)
        if not match:
            continue
        code = int(match.group(1), 16)
        glyph = font.createChar(code)
        glyph.importOutlines(str(svg_path))
        glyph.width, glyph.vwidth = read_svg_size(svg_path)

    # Import additional glyph outlines for subtable (e.g. u3041-vert.svg)
    for svg_path in all_svg_paths:
        match = re.search("^u([0-9a-f]{4})-([a-z]+).svg$", svg_path.name)
        if not match:
            continue
        code = int(match.group(1), 16)
        subtable_name = match.group(2)
        glyph_name = f"u{code:04x}-{subtable_name}"
        glyph = font.createChar(-1, glyph_name)
        glyph.importOutlines(str(svg_path))
        glyph.width, glyph.vwidth = read_svg_size(svg_path)
        font[code].addPosSub(subtable_name, glyph_name)

    return font


def read_svg_size(path_to_svg: pathlib.Path) -> typing.Tuple[int, int]:
    with xml.dom.minidom.parse(str(path_to_svg)) as doc:
        width = int(doc.childNodes[0].getAttribute("width"))
        height = int(doc.childNodes[0].getAttribute("height"))
        return width, height


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
