#!/bin/bash
# Double-click in Finder to open a capture window.
cd "$(dirname "$0")"
./bin/capture
echo
read -p "Done. Press Enter to close..."
