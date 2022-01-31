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
    font.encoding = "UnicodeBmp"
    font.hasvmetrics = 1  # required to enable vwidth settings
    font.ascent = 800
    font.descent = 200
    font.em = 1000
    font.hhea_linegap = font.os2_typolinegap = 0

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

    # Import base glyphs (e.g. u3041.svg)
    for svg_path in all_svg_paths:
        match = re.search("^u([0-9a-f]+).svg$", svg_path.name)
        if not match:
            continue
        code = int(match.group(1), 16)
        glyph = font.createChar(code)
        glyph.importOutlines(str(svg_path))
        glyph.width, glyph.vwidth = read_svg_size(svg_path)

    # Import replacement glyphs (e.g. u3041-vert.svg)
    for svg_path in all_svg_paths:
        match = re.search("^u([0-9a-f]+)-([a-z]+).svg$", svg_path.name)
        if not match:
            continue
        code = int(match.group(1), 16)
        subtable_name = match.group(2)
        base_glyph = font[code]
        glyph_name = f"{base_glyph.glyphname}.{subtable_name}"
        glyph = font.createChar(-1, glyph_name)
        glyph.importOutlines(str(svg_path))
        glyph.width, glyph.vwidth = read_svg_size(svg_path)
        base_glyph.addPosSub(subtable_name, glyph_name)

    # Simplify all the glyphs
    font.selection.all()
    font.removeOverlap()
    font.simplify(1, ("removesingletonpoints",))

    # Workaround for a trailing space in version string
    # Wait for the next release of FontForge (2022?)
    # https://github.com/fontforge/fontforge/issues/4595
    font.sfnt_names = tuple(
        (lang, id_, val.strip()) for lang, id_, val in font.sfnt_names
    )

    return font


def read_svg_size(path_to_svg: pathlib.Path) -> tuple[int, int]:
    with xml.dom.minidom.parse(str(path_to_svg)) as doc:
        width = int(doc.childNodes[0].getAttribute("width"))
        height = int(doc.childNodes[0].getAttribute("height"))
        return width, height


def generate_font_file(*, version: str, file_path: pathlib.Path) -> None:
    font = build_saltcandy123font(version=version)
    font.generate(
        str(file_path),
        flags=(
            "opentype",
            "old-kern",
            "winkern",
            "dummy-dsig",
            "no-FFTM-table",
            "no-hints",
            "no-flex",
            "omit-instructions",
        ),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        metavar="FILE",
        default="saltcandy123font-Regular.ttf",
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
    generate_font_file(version=args.t, file_path=args.o)


if __name__ == "__main__":
    main()
