#!/bin/bash
# Pokee Deep Research - Bash entry point
# Usage: ./pokee-research.sh "Your research question"

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "${SCRIPT_DIR}/pokee_research.py" "$@"
