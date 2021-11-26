#!/bin/bash

if [ "${#}" -ne 1 ]; then
    echo "Usage: bash ${0} FONT_VERSION"
    exit 1
fi
FONT_VERSION=${1}

set -eux

BASE_DIR="$(dirname "$(dirname "${0}")")"
DIST_DIR="${BASE_DIR}/dist"
mkdir -p "${DIST_DIR}"

python3 "${BASE_DIR}/scripts/build_font.py" -t "${FONT_VERSION}" -o "${DIST_DIR}/saltcandy123font.ttf"
python3 "${BASE_DIR}/scripts/build_font.py" -t "${FONT_VERSION}" -o "${DIST_DIR}/saltcandy123font.woff"

NPM_PACKAGE_DIR="${DIST_DIR}/npm-package"
mkdir -p "${NPM_PACKAGE_DIR}"
cp "${DIST_DIR}/saltcandy123font.ttf" "${DIST_DIR}/saltcandy123font.woff" "${NPM_PACKAGE_DIR}/"
cp "${BASE_DIR}/README-npm.md" "${NPM_PACKAGE_DIR}/README.md"
bash "${BASE_DIR}/scripts/generate-fontimage.sh" "${DIST_DIR}/saltcandy123font.ttf" "${NPM_PACKAGE_DIR}/fontimage.png"
cat <<EOF | python -m json.tool >"${NPM_PACKAGE_DIR}/package.json"
{
    "name": "@saltcandy123/saltcandy123font",
    "version": "${FONT_VERSION}",
    "description": "A handwritten font",
    "repository": "https://github.com/saltcandy123/saltcandy123font",
    "author": "saltcandy123"
}
EOF
