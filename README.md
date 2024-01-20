# saltcandy123font

saltcandy123font は @saltcandy123 による手書きフォントです。

saltcandy123font is a font based on the handwriting of @saltcandy123.

![A font image of saltcandy123font.](./fontimage.png)

Visit [the demo page](https://saltcandy123.github.io/saltcandy123font/) to try the font with your texts.

## Installation

Download `saltcandy123font.zip` from
[the release page on GitHub](https://github.com/saltcandy123/saltcandy123font/releases/latest), uncompress the zip file and install the font file to your system.

Alternatively, if you use the font in a Node.js project, run `npm install @saltcandy123/saltcandy123font` ([npm package](https://www.npmjs.com/package/@saltcandy123/saltcandy123font)).

## Supported characters

- (U+0000 - U+007F) Basic Latin (ASCII)
- (U+3000 - U+303F) CJK Symbols and Punctuation
- (U+3040 - U+309F) Hiragana
- (U+30A0 - U+30FF) Katakana
- (U+4E00 - U+9FFF) CJK Unified Ideographs (漢字)
  - Supporting only a small set of characters
- (U+FF00 - U+FFEF) Halfwidth and Fullwidth Forms
  - Excluding halfwidth Hangul variants and halfwidth symbol variants (U+FFA0 - U+FFDC, U+FFE8 - U+FFEE)

## Development

### Source code

- **`glyphs/xxxx/uXXXX.svg`** defines the shape of each character. For example, [`u0073.svg`](glyphs/basic-latin/u0073.svg) is the image of "s" (U+0073). A character may have another image (`uXXXX-vert.svg`) for vertical writing ("vert" feature). The SVG files are in the `glyphs` directory or subdirectories named after Unicode blocks.
- **[`scripts/fontbuild.py`](scripts/fontbuild.py)** builds a font from the glyph SVG files.
- **[`scripts/glyphclean.py`](scripts/glyphclean.py)** cleans SVG files by removing extra data from SVG.
- **[`scripts/distbuild.py`](scripts/distbuild.py)** builds distribution packages under the `dist` directory.
- **[`scripts/fontimagegen.sh`](scripts/fontimagegen.sh)** produces a font thumbnail image for README.
- **`.github/workflows/*.yml`** defines workflows for GitHub Actions.
  - **[`.github/workflows/release.yml`](.github/workflows/release.yml)** creates a release with a zip file when a git tag is pushed, and publishes the npm package.
  - **[`.github/workflows/verification.yml`](.github/workflows/verification.yml)** builds a font and tests it using a font quality assurance tool [Font Bakery](https://github.com/fonttools/fontbakery).
  - **[`.github/workflows/font-image.yml`](.github/workflows/font-image.yml)** updates [`fontimage.png`](fontimage.png) on a git branch using a built font.

Note that the scripts require Python 3.11 and [FontForge](https://fontforge.org/) 2023-01-01.

### How to add a glyph

```bash
## Create a directory under "glyphs"
mkdir -p glyphs/draft

## Create an empty SVG file
cat <<EOF >glyphs/draft/u5b57.svg
<?xml version="1.0" ?>
<svg xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 1000 1000"></svg>
EOF

## Add template lines
python scripts/glyphclean.py glyphs/draft --with-template

## Draw outlines on your SVG editor (e.g. inkscape)
inkscape glyphs/draft/u5b57.svg

## Erase template lines
python scripts/glyphclean.py glyphs/draft

## Build a font file
python scripts/fontbuild.py -o font.ttf
```

The glyphs for this font were drawn with Inkscape using "Calligraphy Tool" with the settings as follows:

- Marker
- Width: 75px
- Thinning: 0
- Mass: 2
- Angle: 90
- Fixation: 0
- Caps: 1.00
- Tremor: 0
- Wiggle: 0
