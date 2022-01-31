#!/usr/bin/env python3

"""Remove unnecessary XML elements from glyph SVG files"""

import argparse
import pathlib
import re
import unicodedata
import xml.dom.minidom


def clean_dom(doc: xml.dom.minidom.Document) -> None:
    svg = doc.documentElement
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


def add_template(doc: xml.dom.minidom.Document, char_code: int) -> None:
    svg = doc.documentElement
    nodes = list()
    width = int(svg.getAttribute("width"))
    height = int(svg.getAttribute("height"))

    for top in range(-1000, height + 1, 1000):
        for delta in [0, 400, 800, 1000]:
            y = top + delta
            if y <= height:
                nodes.append(create_line(doc, x1=-1000, y1=y, x2=width, y2=y))

    for x in [-1000, -500, 0, width // 2, width]:
        nodes.append(create_line(doc, x1=x, y1=-1000, x2=x, y2=height))

    nodes.append(create_line(doc, x1=0, y1=0, x2=width, y2=0, width=10))
    nodes.append(create_line(doc, x1=width, y1=0, x2=width, y2=height, width=10))
    nodes.append(create_line(doc, x1=width, y1=height, x2=0, y2=height, width=10))
    nodes.append(create_line(doc, x1=0, y1=height, x2=0, y2=0, width=10))

    text = f"{chr(char_code)} (U+{char_code:04X}, {unicodedata.name(chr(char_code))})"
    nodes.append(create_text(doc, text=text, x=0, y=height - 25, size=50))

    first_element = svg.firstChild
    for node in nodes:
        svg.insertBefore(node, first_element)


def create_line(
    doc: xml.dom.minidom.Document, *, x1: int, y1: int, x2: int, y2: int, width: int = 2
) -> xml.dom.minidom.Node:
    node = doc.createElement("line")
    node.setAttribute("x1", str(x1))
    node.setAttribute("y1", str(y1))
    node.setAttribute("x2", str(x2))
    node.setAttribute("y2", str(y2))
    node.setAttribute("stroke", "#99f")
    node.setAttribute("stroke-width", str(width))
    node.setAttribute("class", "template")
    return node


def create_text(
    doc: xml.dom.minidom.Document, *, text: str, x: int, y: int, size: int
) -> xml.dom.minidom.Node:
    node = doc.createElement("text")
    node.setAttribute("x", str(x))
    node.setAttribute("y", str(y))
    node.setAttribute("font-size", str(size))
    node.setAttribute("fill", "#f99")
    node.setAttribute("class", "template")
    node.appendChild(doc.createTextNode(text))
    return node


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
        match = re.search("^u([0-9a-f]+)(-([a-z]+))?.svg$", svg_path.name)
        if match is None:
            continue
        char_code = int(match.group(1), 16)
        with open(svg_path) as f:
            svg_content = f.read()
        with xml.dom.minidom.parseString(svg_content) as dom:
            clean_dom(dom)
            if args.with_template:
                add_template(dom, char_code)
            with open(svg_path, "w") as f:
                dom.writexml(f, newl="\n")


if __name__ == "__main__":
    main()
