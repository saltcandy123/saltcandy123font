#!/bin/bash

set -eux

base_dir=$(dirname "$0")
font_file=$base_dir/dist/saltcandy123font.ttf
output_image=$base_dir/fontimage.png
fontimage \
    "$font_file" \
    --width 460 \
    --pixelsize 20 \
    --fontname \
    --text " " \
    --text "0123456789 ()[]{}<>/\\|\`~@#$%^&*_+-=;:'\",.!?" \
    --text "ABCDEFGHIJKLMLOPQRSTUVWXYZ abcdefghijklmlopqrstuvwxyz" \
    --text " " \
    --text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
    -o "$output_image"
convert \
    "$output_image" \
    -bordercolor white \
    -border 20x20 \
    -strip \
    "$output_image"
