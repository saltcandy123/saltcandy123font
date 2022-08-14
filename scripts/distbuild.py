#!/usr/bin/env python3

"""Build distribution files under dist directory"""

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import zipfile

import fontbuild

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
    license_path = BASE_DIR.joinpath("OFL.txt")

    dist_dir = BASE_DIR.joinpath("dist")
    dist_dir.mkdir(exist_ok=True)

    font_paths = [
        dist_dir.joinpath(f"saltcandy123font-Regular.{ext}") for ext in ["ttf", "woff"]
    ]
    font = fontbuild.build_saltcandy123font(version=version.get_font_version())
    for path in font_paths:
        fontbuild.generate_file(font=font, path=path)

    with zipfile.ZipFile(dist_dir.joinpath("saltcandy123font.zip"), "w") as zipf:
        zipf.write(license_path, license_path.name)
        for path in font_paths:
            zipf.write(path, path.name)

    npm_package_dir = dist_dir.joinpath("npm-package")
    npm_package_dir.mkdir(exist_ok=True)

    for path in font_paths:
        shutil.copy(path, npm_package_dir)
    shutil.copy(license_path, npm_package_dir)
    with open(npm_package_dir.joinpath("README.md"), "w") as f:
        f.write(build_npm_readme_content())
    with open(npm_package_dir.joinpath("package.json"), "w") as f:
        f.write(build_package_json_content(version=version))

    for path in font_paths:
        os.remove(path)


def build_npm_readme_content() -> str:
    with open(BASE_DIR.joinpath("README-npm.md")) as f:
        readme_content = f.read()
    # If the commit has a tag, update all the image URLs in README to refer to the tag
    try:
        command = ["git", "describe", "--tags", "--exact-match"]
        output = subprocess.check_output(command, stderr=subprocess.DEVNULL)
        git_tag = output.decode().strip() or None
    except subprocess.CalledProcessError:
        git_tag = None
    if git_tag:
        base_url = "https://raw.githubusercontent.com/saltcandy123/saltcandy123font"
        main_base_url = f"{base_url}/main/"
        tagged_base_url = f"{base_url}/{git_tag}/"
        readme_content = readme_content.replace(main_base_url, tagged_base_url)
    return readme_content


def build_package_json_content(*, version: Version) -> str:
    metadata = {
        "name": "@saltcandy123/saltcandy123font",
        "version": version.get_package_version(),
        "description": "A handwritten font",
        "repository": "https://github.com/saltcandy123/saltcandy123font",
        "author": "saltcandy123",
        "license": "OFL-1.1",
    }
    return json.dumps(metadata, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "version",
        metavar="VERSION",
        type=Version,
        help='build distribution files as VERSION (e.g. "0.1.2")',
    )
    args = parser.parse_args()
    build_files(args.version)


if __name__ == "__main__":
    main()
