# saltcandy123font

@saltcandy123 による手書きフォントです。

This is a simple handwritten font created by @saltcandy123.

- Download the `ttf` file and the `woff` from [the release page](https://github.com/saltcandy123/saltcandy123font/releases).
- An npm package ([@saltcandy123/saltcandy123font](https://www.npmjs.com/package/@saltcandy123/saltcandy123font)) is also available.

![Font image](./fontimage.png)

## Source code

- **`glyphs/uXXXX.svg`** defines the shape of each character. For example, [`u0073.svg`](glyphs/u0073.svg) is the image of "s" (U+0073).
- **[`scripts/build_font.py`](scripts/build_font.py)** builds a font from the glyph SVG files. This Python script requires [FontForge](https://fontforge.org/) and [its Python library](https://fontforge.org/docs/scripting/python.html).
- **[`scripts/clean_glyphs.py`](scripts/clean_glyphs.py)** cleans SVG files by removing extra data from SVG.
- **[`scripts/build-dist.sh`](scripts/build-dist.sh)** builds distribution files under `dist` directory.
