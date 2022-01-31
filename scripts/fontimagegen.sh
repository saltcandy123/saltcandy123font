#!/bin/bash

if [ ${#} -ne 2 ]; then
    echo "Usage: bash ${0} FONT_FILE OUTPUT_FILE"
    exit 1
fi
FONT_FILE="${1}"
OUTPUT_FILE="${2}"

set -eux

fontimage \
    "${FONT_FILE}" \
    --width 460 \
    --pixelsize 20 \
    --fontname \
    --text " " \
    --text "0123456789 ()[]{}<>/\\|\`~@#$%^&*_+-=;:'\",.!?" \
    --text "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz" \
    --text " " \
    --text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
    -o "${OUTPUT_FILE}"

convert \
    "${OUTPUT_FILE}" \
    -bordercolor white \
    -border 20x20 \
    -strip \
    "${OUTPUT_FILE}"
