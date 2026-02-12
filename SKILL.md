---
name: pokee-deep-research
description: Conduct deep research using Pokee AI's Deep Research API. Generates comprehensive, structured research reports with outlines and detailed writeups. Use when the user needs thorough research, competitive analysis, market research, academic research, or any topic requiring detailed investigation. Takes 7-25 minutes per query and produces publication-quality reports.
---

# Pokee Deep Research

## 3-Step Quick Start

**1. Install:**
```bash
mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
git clone https://github.com/Niraven/pokee-deep-research-skill.git pokee-deep-research
cd pokee-deep-research
```

**2. Setup (get free token at https://pokee.ai):**
```bash
python3 scripts/setup.py
```

**3. Research:**
```bash
./scripts/pokee-research.sh "Your research question"
```

## Output

Results saved to `~/.openclaw/workspace/research-output/`:
- `*_outline.md` — Structured outline
- `*_writeup.md` — Full report (50-70 KB)
- `*_response.json` — Raw API data

## Requirements

- Python 3.7+
- `pip3 install requests` (if not installed)
- Pokee API token (free at https://pokee.ai)

## Troubleshooting

**"No API token"** → Run `python3 scripts/setup.py`

**"requests not found"** → `pip3 install requests`
