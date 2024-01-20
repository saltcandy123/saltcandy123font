#!/usr/bin/env python3

"""Build distribution packages (zip file, npm pakcage) under dist directory"""

import argparse
import json
import logging
import os
import pathlib
import re
import shutil
import subprocess
import zipfile

import fontbuild

LOGGER = logging.getLogger(__name__)

BASE_DIR = pathlib.Path(__file__).parent.parent


class Version:
    major: int
    minor: int
    patch: int

    def __init__(self, version_str: str) -> None:
        m = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)$", version_str)
        if m is None:
            raise argparse.ArgumentTypeError(f"Invalid version string: {version_str:r}")
        major = int(m.group(1))
        minor = int(m.group(2))
        patch = int(m.group(3))
        if minor > 99:
            raise argparse.ArgumentTypeError(f"Invalid minor version: {minor}")
        if patch > 9:
            raise argparse.ArgumentTypeError(f"Invalid patch version {patch}")
        self.major = major
        self.minor = minor
        self.patch = patch

    def get_package_version(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def get_font_version(self) -> str:
        return f"{self.major}.{self.minor:02}{self.patch}"


def build_files(version: Version) -> None:
    LOGGER.info("Started building files")

    license_path = BASE_DIR.joinpath("OFL.txt")

    dist_dir = BASE_DIR.joinpath("dist")
    dist_dir.mkdir(exist_ok=True)

    font = fontbuild.build_saltcandy123font(version=version.get_font_version())
    LOGGER.info(f"Built a font object as version {font.version}")

    extensions = ["ttf", "woff"]
    font_paths = [
        dist_dir.joinpath(f"saltcandy123font-Regular.{ext}") for ext in extensions
    ]
    for path in font_paths:
        fontbuild.generate_file(font=font, path=path)
        LOGGER.info(f"Built a font file {path.name} (size: {get_file_size(path)})")

    zip_path = dist_dir.joinpath("saltcandy123font.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(license_path, license_path.name)
        for path in font_paths:
            zipf.write(path, path.name)
    LOGGER.info(f"Built a zip file {zip_path.name} (size: {get_file_size(zip_path)})")

    npm_package_dir = dist_dir.joinpath("npm-package")
    if npm_package_dir.exists():
        shutil.rmtree(npm_package_dir)
    npm_package_dir.mkdir()

    for path in font_paths:
        shutil.copy(path, npm_package_dir)
    shutil.copy(license_path, npm_package_dir)
    with open(npm_package_dir.joinpath("README.md"), "w") as f:
        f.write(build_npm_readme_content())
    with open(npm_package_dir.joinpath("package.json"), "w") as f:
        f.write(build_package_json_content(version=version.get_package_version()))
    LOGGER.info(f"Built an npm package as version {version.get_package_version()}")

    for path in font_paths:
        os.remove(path)


def get_file_size(path: pathlib.Path) -> str:
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} B"
    if size < 1024**2:
        return f"{size / 1024:.2f} KB"
    return f"{size / 1024**2:.2f} MB"


def build_npm_readme_content() -> str:
    git_tag = get_git_tag() or "main"
    image_url = f"https://raw.githubusercontent.com/saltcandy123/saltcandy123font/{git_tag}/fontimage.png"
    return re.sub(
        "\n\\s+\\|",
        "\n",
        f"""
        |# saltcandy123font
        |
        |saltcandy123font is a font based on the handwriting of @saltcandy123.
        |
        |![A font image of saltcandy123font.]({image_url})
        |
        |## Usage
        |
        |Install the package using this command:
        |
        |```bash
        |npm install @saltcandy123/saltcandy123font
        |```
        |
        |Then, import font files in your frontend code.
        |Example usage in CSS:
        |
        |```css
        |@font-face {{
        |  font-family: "saltcandy123font";
        |  src:
        |    url("~@saltcandy123/saltcandy123font/saltcandy123font-Regular.woff")
        |      format("woff"),
        |    url("~@saltcandy123/saltcandy123font/saltcandy123font-Regular.ttf")
        |      format("truetype");
        |  font-weight: 400;
        |  font-style: normal;
        |}}
        |```
        |""",
    ).lstrip("\n")


def get_git_tag() -> str | None:
    try:
        command = ["git", "describe", "--tags", "--exact-match"]
        output = subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return output.decode().strip() or None
    except subprocess.CalledProcessError:
        return None


def build_package_json_content(*, version: str) -> str:
    metadata = {
        "name": "@saltcandy123/saltcandy123font",
        "version": version,
        "description": "A font based on the handwriting of @saltcandy123",
        "repository": "https://github.com/saltcandy123/saltcandy123font",
        "author": "saltcandy123",
        "license": "OFL-1.1",
        "keywords": ["font", "typeface"],
    }
    return json.dumps(metadata, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "version",
        metavar="VERSION",
        type=Version,
        help='semantic version of the distribution package (e.g. "0.1.2")',
    )
    parser.add_argument(
        "--loglevel",
        metavar="LEVEL",
        choices=["DEBUG", "INFO", "WARN", "ERROR"],
        default="INFO",
        help="logging level (default: INFO)",
    )
    args = parser.parse_args()

    logging.basicConfig(
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
        level=getattr(logging, args.loglevel),
    )

    build_files(args.version)

    LOGGER.info("Done!")


if __name__ == "__main__":
    main()
