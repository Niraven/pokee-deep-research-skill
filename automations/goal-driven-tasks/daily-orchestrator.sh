#!/bin/bash
# Goal-Driven Autonomous Task System - Master Orchestrator
# Chief AI Architect: Axis
# 
# This script runs daily at 8:00 AM Manila time
# 1. Generates tasks from GOALS.md
# 2. Executes autonomous tasks
# 3. Reports status

set -e

echo "🎯 Goal-Driven Autonomous Task System"
echo "======================================"
echo "Date: $(date)"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Step 1: Generate tasks
echo "📋 Step 1: Generating daily tasks..."
python3 "${SCRIPT_DIR}/generate-tasks.py"
echo ""

# Step 2: Execute autonomous tasks
echo "⚡ Step 2: Executing autonomous tasks..."
python3 "${SCRIPT_DIR}/execute-tasks.py"
echo ""

# Step 3: Update morning digest with task status
echo "📊 Step 3: Updating status..."
TODAY=$(date +%Y-%m-%d)
TASKS_FILE="${HOME}/.openclaw/workspace/memory/daily-tasks/${TODAY}-tasks.md"

if [ -f "$TASKS_FILE" ]; then
    echo "✅ Today's tasks available at:"
    echo "   ${TASKS_FILE}"
    echo ""
    echo "📋 Task Preview:"
    head -50 "$TASKS_FILE"
else
    echo "⚠️  Tasks file not found"
fi

echo ""
echo "🎉 Daily task generation complete!"
echo ""
echo "Next: Review tasks and approve autonomous execution."
