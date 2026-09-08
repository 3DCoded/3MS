#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

uv run python step_helper.py
exec uv run zensical "$@"