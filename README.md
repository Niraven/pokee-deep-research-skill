# 🦞 Pokee Deep Research

**3 steps to deep research:**

## Step 1: Install (copy-paste this)
```bash
mkdir -p ~/.openclaw/skills
cd ~/.openclaw/skills
git clone https://github.com/Niraven/pokee-deep-research-skill.git pokee-deep-research
cd pokee-deep-research
```

## Step 2: Setup (copy-paste this)
```bash
python3 scripts/setup.py
```
**It will ask for your Pokee token.** Get one free at https://pokee.ai

## Step 3: Research (copy-paste this)
```bash
./scripts/pokee-research.sh "Compare Tesla vs BYD EV strategies"
```

---

## 📁 Where Results Go

Check `~/.openclaw/workspace/research-output/` after it finishes (takes 7-25 minutes).

You'll get:
- `*_outline.md` — Quick overview
- `*_writeup.md` — Full report
- `*_response.json` — Raw data

---

## ❓ Troubleshooting

| Problem | Fix |
|---------|-----|
| "No API token" | Run `python3 scripts/setup.py` again |
| "Command not found" | Make sure you're in the `pokee-deep-research` folder |
| "pip not found" | Install Python 3 first |

---

**Questions?** The skill is at: https://github.com/Niraven/pokee-deep-research-skill
