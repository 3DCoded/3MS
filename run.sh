#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

uv run python step_helper.py # Generate step markdown
wget https://raw.githubusercontent.com/3DCoded/3MS/refs/heads/main/install.sh -O docs/install.sh # Download/update install script

uv run zensical "$@"