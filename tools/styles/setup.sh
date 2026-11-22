#!/bin/sh
# Recreate the working directories the style builders expect (paths are hardcoded).
set -e
mkdir -p /home/claude/work
rm -rf /home/claude/work/styles && cp -r "$(dirname "$0")" /home/claude/work/styles
mkdir -p /home/claude/lilac && cp -r /home/claude/work/styles/heirloom_source/* /home/claude/lilac/
pip install playwright pillow qrcode opencv-python-headless --break-system-packages -q || true
echo "ready: /home/claude/work/styles"
