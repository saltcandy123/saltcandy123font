#!/usr/bin/env python3

"""Remove unnecessary XML elements from glyph SVG files"""

import argparse
import pathlib
import xml.dom.minidom


def create_line_node(
    doc: xml.dom.minidom.Document, x1: int, y1: int, x2: int, y2: int
) -> xml.dom.minidom.Node:
    node = doc.createElement("line")
    node.setAttribute("x1", str(x1))
    node.setAttribute("y1", str(y1))
    node.setAttribute("x2", str(x2))
    node.setAttribute("y2", str(y2))
    node.setAttribute("stroke", "#99f")
    node.setAttribute("stroke-width", "5")
    node.setAttribute("class", "template")
    return node


def clean_dom(doc: xml.dom.minidom.Document, *, with_template: bool) -> None:
    svg = doc.firstChild
    namespaces = set()
    for key in set(svg.attributes.keys()) - {"xmlns", "width", "height"}:
        svg.removeAttribute(key)
        if key.startswith("xmlns:"):
            namespaces.add(key.split(":")[1])
    for child in list(svg.childNodes):
        if child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            if child.prefix in namespaces:
                svg.removeChild(child)
            elif child.tagName in ("metadata", "defs"):
                svg.removeChild(child)
            elif child.getAttribute("class") == "template":
                svg.removeChild(child)
            elif child.tagName == "path":
                for key in set(child.attributes.keys()) - {"d"}:
                    child.removeAttribute(key)
            else:
                raise RuntimeError(f"Unexpected tag: {child.tagName}")
        else:
            svg.removeChild(child)
    if with_template:
        first_element = svg.firstChild
        width = int(svg.getAttribute("width"))
        height = int(svg.getAttribute("height"))
        for y in range(0, height + 1, 400):
            svg.insertBefore(create_line_node(doc, 0, y, width, y), first_element)
        svg.insertBefore(
            create_line_node(doc, width // 2, 0, width // 2, height), first_element
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "dirname",
        type=pathlib.Path,
        help="path to directory that glyph SVG files are in",
    )
    parser.add_argument(
        "--with-template", action="store_true", help="draw template lines on each SVG"
    )
    args = parser.parse_args()
    glyphs_dir = args.dirname

    for svg_path in glyphs_dir.glob("**/*.svg"):
        with open(svg_path) as f:
            svg_content = f.read()
        with xml.dom.minidom.parseString(svg_content) as dom:
            clean_dom(dom, with_template=args.with_template)
            with open(svg_path, "w") as f:
                dom.writexml(f, newl="\n")


if __name__ == "__main__":
    main()
