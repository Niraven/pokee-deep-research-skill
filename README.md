# 🦞 Pokee Deep Research

> When you need **answers worth waiting for**

Some questions deserve more than a quick search. Pokee Deep Research takes 7-25 minutes to deliver structured, comprehensive reports — the kind you'd expect from an analyst, not an algorithm.

---

## Why This Exists

| Quick Search | Deep Research |
|--------------|---------------|
| 10 blue links | Executive summary + detailed analysis |
| Surface facts | Strategic insights |
| You connect the dots | Pokee connects them for you |

**Use this when:** preparing for a meeting, evaluating competitors, understanding a market, or any time "I googled it" isn't enough.

---

## 3 Steps to Start

### 1. Install (copy-paste)
```bash
mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
git clone https://github.com/Niraven/pokee-deep-research-skill.git pokee-deep-research
cd pokee-deep-research
```

### 2. Configure (copy-paste)
```bash
python3 scripts/setup.py
```
**Need a token?** Get one free at [pokee.ai](https://pokee.ai) — takes 30 seconds.

### 3. Research (copy-paste)
```bash
./scripts/pokee-research.sh "What you're actually trying to learn"
```

**Examples that work well:**
- "EV charging infrastructure: who owns what in 2025"
- "Remote work productivity studies: what actually holds up"
- "AI coding tools landscape: enterprise vs indie"

---

## What You Get Back

After 7-25 minutes, check `~/.openclaw/workspace/research-output/`:

| File | What's Inside |
|------|---------------|
| `*_outline.md` | The skeleton — scan this first |
| `*_writeup.md` | The meat — 50-70 KB of analysis |
| `*_response.json` | Raw data — for follow-up questions |

**The writeup includes:** executive summary, key players, comparative analysis, recommendations, and sources.

---

## About Pokee

[Pokee](https://pokee.ai) is an AI execution agent — you describe what you need in plain English, it figures out the rest. The Deep Research API is their academic-grade engine: slower because it's thorough, structured because it's useful.

**Pricing:** ~$0.50-2.00 per query. You use your own account — no pooled credits, no surprises.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "No API token" | Re-run `python3 scripts/setup.py` |
| "requests not found" | `pip3 install requests` |
| Command not found | Make sure you're in the `pokee-deep-research` folder |

---

Built for [OpenClaw](https://openclaw.ai) · Powered by [Pokee](https://pokee.ai)
