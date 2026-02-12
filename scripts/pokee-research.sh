#!/bin/bash
# Pokee Deep Research - Main entry point

QUERY="$1"
if [ -z "$QUERY" ]; then
    echo "Usage: pokee-research.sh 'Your research question'"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/pokee_research.py" "$QUERY"
