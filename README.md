# 🔍 Pokee Deep Research

> **Deep research that actually goes deep — iterative investigation, real citations, answers you can verify.**

Powered by [Pokee AI](https://pokee.ai)'s SOTA Deep Research Agent. Up to 75% cheaper than OpenAI, Gemini, and Perplexity. No API key management, no hidden costs.

---

## ✨ What Makes This Different

| | Web Search | ChatGPT/Perplexity | **Pokee Deep Research** |
|---|:---:|:---:|:---:|
| **Speed** | ⚡ Instant | 🚀 30-60 sec | ⏱️ 7-25 min |
| **Method** | Links | Single query | **Multi-turn investigation** |
| **Depth** | Surface | Medium | **Deep — explores, not summarizes** |
| **Structure** | Raw links | Paragraphs | **Outline + Full Report** |
| **Citations** | ❌ | Partial | **✅ Rich, verifiable sources** |
| **Best For** | Quick facts | Fast answers | **Strategic decisions, due diligence** |

Other AI tools give you plausible summaries. Pokee performs **iterative web searches and content analysis** — reading sources, following leads, building a comprehensive picture you can actually trust.

**Use this when:** preparing for a meeting, evaluating competitors, understanding a market, or any time "I googled it" isn't enough.

---

## 🚀 Quick Start

### 1. Install

```bash
mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
git clone https://github.com/Niraven/pokee-deep-research-skill.git pokee-deep-research
cd pokee-deep-research
```

### 2. Configure

```bash
python3 scripts/setup.py
```

**Need a token?** Get one free at [pokee.ai](https://pokee.ai) — takes 30 seconds.

### 3. Research

```bash
./scripts/pokee-research.sh "competitive analysis of AI presentation tools"
```

**Examples that work well:**
- "EV charging infrastructure: who owns what in 2025"
- "Remote work productivity studies: what actually holds up"
- "AI coding tools landscape: enterprise vs indie"

---

## 📊 What You Get

Every research query produces publication-quality output:

| File | What's Inside |
|------|---------------|
| `*_outline.md` | Structured hierarchy of findings (research roadmap) |
| `*_writeup.md` | Detailed report with **rich citations** (50-70 KB) |
| `*_response.json` | Raw API data for programmatic use |

**What sets Pokee reports apart:**
- **Investigated, not summarized** — Multi-turn research that follows leads
- **Cited, not asserted** — Every key claim has a source you can check
- **Structured, not scattered** — Executive summary → detailed findings → sources

---

## 🧠 About Pokee AI

**Pokee AI** runs the **state-of-the-art 7B DeepResearch Agent** — open-source, benchmark-proven, and engineered for thoroughness.

### Why Pokee?

- **SOTA Performance:** Achieves superior results on HLE, GAIA, BrowseComp, and other complex reasoning benchmarks
- **Iterative Research:** Performs multi-turn web searches and content analysis — not one-shot summaries
- **Citation-Rich:** Every claim backed by sources you can verify
- **Transparent:** Open-source model you can audit, API you can trust
- **75% Cheaper:** Up to 75% less than OpenAI, Gemini, and Perplexity with no hidden costs

### The Open Source + API Combo

| | **PokeeResearch-7B (Open Source)** | **Pokee Deep Research API** |
|---|---|---|
| **Model** | 7B parameter agent | Same SOTA agent |
| **Setup** | Self-hosted (Docker, GPUs) | Zero setup |
| **Infrastructure** | You manage | We manage |
| **Best For** | Researchers, tinkerers | Teams, builders, busy professionals |

This skill uses the **API** — same benchmark-proven quality, zero infrastructure headaches.

---

## 💰 Pricing

- **Input:** $0.30 per 1M tokens (~60 credits)
- **Output:** $2.00 per 1M tokens (~400 credits)
- **Typical query:** 500-2,000 credits ($0.50-2.00)

Each user uses their own Pokee account — no shared costs, no surprises.

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---------|-----|
| "No API token" | Re-run `python3 scripts/setup.py` |
| "requests not found" | `pip3 install requests` |
| Command not found | Make sure you're in the `pokee-deep-research` folder |

---

## 🔗 Links

- **Pokee AI:** https://pokee.ai
- **Deep Research API Preview:** https://pokee.ai/deepresearch-preview
- **PokeeResearch-7B (Open Source):** https://github.com/Pokee-AI/PokeeResearchOSS
- **OpenClaw:** https://openclaw.ai

---

Built for [OpenClaw](https://openclaw.ai) · Powered by [Pokee AI](https://pokee.ai)
