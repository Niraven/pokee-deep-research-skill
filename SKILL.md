---
name: pokee-deep-research
description: Conduct deep research using Pokee AI's Deep Research API. Generates comprehensive, structured research reports with outlines and detailed writeups. Use when the user needs thorough research, competitive analysis, market research, academic research, or any topic requiring detailed investigation. Takes 7-25 minutes per query and produces publication-quality reports.
author: Niraven
version: 1.0.0
keywords:
  - ai
  - research
  - deep-research
  - pokee
  - analysis
  - competitive-intelligence
  - market-research
  - academic-research
---

# Pokee Deep Research

Conduct deep research using Pokee AI's Deep Research API. Generates comprehensive, structured research reports with outlines and detailed writeups.

## Quick Start

```bash
# Setup (one-time)
python3 scripts/setup.py

# Run research
./scripts/pokee-research.sh "Your research question"
```

## Setup

1. **Get a Pokee API token** from https://pokee.ai
2. **Run the setup wizard**:
   ```bash
   python3 scripts/setup.py
   ```
3. **Enter your token** when prompted

The token is stored securely at `~/.openclaw/workspace/.credentials/pokee-deep-research.txt` with 600 permissions.

## Usage

### Basic Usage

```bash
# From skill directory
./scripts/pokee-research.sh "Compare Tesla vs BYD EV strategies"

# Using absolute path (for automation)
~/.openclaw/skills/pokee-deep-research/scripts/pokee-research.sh "Your query"
```

### Output

Results are saved to `~/.openclaw/workspace/research-output/`:
- `{query}_{timestamp}_outline.md` - Research outline
- `{query}_{timestamp}_writeup.md` - Full research report
- `{query}_{timestamp}_response.json` - Raw API response

## How It Works

1. Sends your query to Pokee AI's Deep Research API
2. The API conducts comprehensive research (7-25 minutes)
3. Results are parsed and saved as markdown files
4. A preview of the writeup is displayed

## Requirements

- Python 3.7+
- `requests` library (`pip install requests`)
- Pokee API token

## Troubleshooting

**"No API token found"**
→ Run `python3 scripts/setup.py` and enter your token

**API errors**
→ Check your token is valid at https://pokee.ai

**Module not found**
→ Install requests: `pip3 install requests`
