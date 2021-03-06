# saltcandy123font

@saltcandy123 による手書きフォントです。

This is a simple handwritten font created by @saltcandy123.

* Download font from <https://github.com/saltcandy123/saltcandy123font/releases>
* Try out demo on <https://saltcandy123.github.io/saltcandy123font/>

![Sample image](https://saltcandy123.github.io/saltcandy123font/sample.png)

## How it works

All the glyph data is stored as SVG files in [`/glyphs`](./glyphs) directory.
Each SVG file is named after the corresponding 4-digit hex Unicode.
For instance, the filename for "A" glyph should be [`u0041.svg`](./glyphs/u0041.svg) because the Unicode of "A" is 41 in hex.
See also [Unicode Character Code Charts](https://unicode.org/charts/).

A Python script [`/build_fonts.py`](./build_fonts.py) converts the SVG files to fonts in `/font-dist` directory.
It requires [FontForge](https://fontforge.org/) and [its Python library](https://fontforge.org/docs/scripting/python.html).

[`/webapp`](./webapp) is the source code directory for <https://saltcandy123.github.io/saltcandy123font/>.
`yarn && yarn build` builds static pages in `/webapp-dist` directory.
`yarn build` requires `/font-dist` directory with font files.

Releasing is handled by GitHub Actions.
By pushing a tag to this repository, GitHub Actions will automatically [create a new release](./.github/workflows/release.yml) and [update GitHub Pages](./.github/workflows/github-pages.yml).
