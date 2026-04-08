---
name: pokee-deep-research
description: >
  Conduct deep research using Pokee AI's Deep Research API. Generates comprehensive,
  structured research reports with outlines and detailed writeups on any topic.
  Use when the user needs thorough investigation, competitive analysis, market research,
  academic research, technology evaluation, due diligence, literature review, or any
  question requiring depth beyond a quick search. Takes 7-25 minutes per query and
  produces publication-quality reports.
---

# Pokee Deep Research

Deep research skill powered by Pokee AI's academic-grade research engine. Use for competitive intelligence, market analysis, technology evaluations, academic research, or any question where a quick search is insufficient.

## Setup

1. Install the skill:
   ```bash
   mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
   git clone https://github.com/Niraven/pokee-deep-research-skill.git pokee-deep-research
   cd pokee-deep-research
   ```
2. Configure your API token (free tier at https://pokee.ai):
   ```bash
   python3 scripts/setup.py
   ```
   Verify setup succeeded: the script should print a confirmation message. If it errors with a token issue, check that your token is valid at https://pokee.ai/dashboard.
3. Run a research query:
   ```bash
   ./scripts/pokee-research.sh "Your research question"
   ```

## Output

Results are saved to `~/.openclaw/workspace/research-output/`:

| File | Purpose |
|------|---------|
| `*_outline.md` | Structured overview of findings (read first) |
| `*_writeup.md` | Full report with analysis, typically 50-70 KB |
| `*_response.json` | Raw API response for programmatic use |

## Requirements

- Python 3.7+
- `pip3 install requests`
- Pokee API token (free tier available)

## Troubleshooting

- **Token error on setup**: Re-run `python3 scripts/setup.py` and paste a fresh token from https://pokee.ai/dashboard.
- **Script timeout**: Queries take 7-25 minutes by design. If the script exits unexpectedly, re-run with the same query as Pokee may cache partial progress.
- **Empty output directory**: Verify your token is configured by checking `~/.openclaw/skills/pokee-deep-research/` for a config file containing your API key.
