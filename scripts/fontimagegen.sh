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
    --width 560 \
    --pixelsize 40 \
    --fontname \
    --pixelsize 20 \
    --text "A font based on the handwriting of @saltcandy123" \
    --text "@saltcandy123 による手書きフォント" \
    --text " " \
    --text " " \
    --text "0123456789 ()[]{}<>/\\|\`~@#$%^&*_+-=;:'\",.!?" \
    --text "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz" \
    -o "${OUTPUT_FILE}"

convert \
    "${OUTPUT_FILE}" \
    -bordercolor white \
    -gravity center \
    -extent 560x240 \
    -border 40x40 \
    -strip \
    "${OUTPUT_FILE}"
