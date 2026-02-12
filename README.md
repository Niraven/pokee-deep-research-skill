# 🦞 Pokee Deep Research for OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue.svg)](https://openclaw.ai)
[![Pokee AI](https://img.shields.io/badge/Pokee-Deep%20Research-green.svg)](https://pokee.ai)

> Transform complex research questions into structured intelligence using Pokee AI's Deep Research API.

---

## ⚡ What Makes This Different

| | Web Search | Perplexity | **Pokee Deep Research** |
|---|---|---|---|
| **Speed** | ⚡ Instant | 🐢 30-60 sec | ⏱️ 7-25 min |
| **Depth** | Surface | Medium | **Deep** |
| **Structure** | Links | Paragraph | **Outline + Report** |
| **Citations** | ✓ | ✗ | ✗ |
| **Best For** | Quick facts | Fast answers | **Strategic analysis** |

Unlike quick searches that return 10 blue links, this skill delivers **academic-grade research** with structured outlines and detailed writeups.

---

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/Niraven/pokee-deep-research-skill.git
pokee-deep-research-skill
```

### 2. Configure

**Get your API token:**
1. Visit [pokee.ai](https://pokee.ai)
2. Sign up → Deep Research API → Generate Token

**Run setup wizard:**
```bash
python3 scripts/setup.py
```

Or manually:
```bash
echo "your-token-here" > ~/.openclaw/workspace/.credentials/pokee-deep-research.txt
chmod 600 ~/.openclaw/workspace/.credentials/pokee-deep-research.txt
```

### 3. Research

```bash
./scripts/pokee-research.sh "competitive analysis of AI presentation tools"
```

From Python:
```python
from scripts.pokee_research import quick_research

result = quick_research("market sizing for workflow automation 2025")
print(result)
```

---

## 🎁 What You Get

For every research query, you'll receive:

1. **`*_outline.md`** — Structured hierarchy of findings
2. **`*_writeup.md`** — Detailed report (50-70 KB)
3. **`*_response.json`** — Raw API data

**Example output structure:**
```markdown
## Executive Summary
## Market Overview
## Key Players
### Company A
### Company B
## Comparative Analysis
## Recommendations
## Sources
[1] Author, Title, Publication, Year
```

---

## 💰 Pricing

- **Input:** $0.30 per 1M tokens (~60 credits)
- **Output:** $2.00 per 1M tokens (~400 credits)
- **Typical query:** 500-2,000 credits ($0.50-2.00)

Each user uses their own Pokee account — no shared costs.

---

## 📦 What's Included

- ✅ **Python client** (`scripts/pokee_research.py`)
- ✅ **Bash client** (`scripts/pokee-research.sh`)
- ✅ **Setup wizard** (`scripts/setup.py`)
- ✅ **MIT License**

---

## 🔮 What is Pokee.ai?

**Pokee AI** is a next-generation AI execution agent platform:

- **Natural language instructions** — Tell it what to do in plain English
- **End-to-end execution** — Research, create, translate across apps
- **Iterative collaboration** — Work together until the plan is right
- **No complex setup** — No API keys, triggers, or "zaps"

The **Deep Research API** is their academic-grade engine — slow (7-25 min) but thorough.

---

## ⚙️ Requirements

- Pokee AI Deep Research API token ([get free](https://pokee.ai))
- Python 3.8+
- OpenClaw 2026.2.0+

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## 📜 License

MIT License — see [LICENSE](LICENSE)

---

## 🔗 Links

- **Pokee AI:** https://pokee.ai
- **OpenClaw Docs:** https://docs.openclaw.ai

---

**Created by:** Nino Amor  
**Version:** 1.0.0  
**Last Updated:** 2026-02-12
