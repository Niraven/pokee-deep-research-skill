# Long-Term Memory

## Critical System Information

### Google Workspace Auth (3 Accounts)
| Priority | Account | Status | Token Location |
|----------|---------|--------|----------------|
| **#1** | **niniconag@gmail.com** | ✅ PRIMARY | `token:default:niniconag@gmail.com` |
| #2 | ninoanthonyconag@gmail.com | ✅ Active | `token:default:ninoanthonyconag@gmail.com` |
| #3 | niamamorwork@gmail.com | ✅ Active | `token:default:niamamorwork@gmail.com` |

**Token Backup:** `~/.openclaw/workspace/.credentials/gog-tokens-backup/`
**Protocol:** `.credentials/GOOGLE_AUTH_PROTOCOL.md`
**Client ID:** `665678854624-eeucp4vbner08j86698b9c7b9i1739et.apps.googleusercontent.com`

### Skill System Architecture

**Total Skills:** 141 enabled (all active) — upgraded from 55 on Feb 20, 2026
**Ghost Skills Fixed:** 86 → 0 (batch fixed Feb 20, 2026)
**Workflow Documentation:** SKILL_WORKFLOW_MATRIX.md (10 master workflows defined)

**Key Skill Categories:**

**Anthropic Official (SkillKit):**
- algorithmic-art, brand-guidelines, slack-gif-creator, theme-factory
- mcp-builder, skill-creator, webapp-testing, doc-coauthoring

**Productivity & Knowledge:**
- 1password, bitwarden, obsidian, notion, trello
- todoist, qmd, news-aggregator

**Media & Creation:**
- remotion-video-toolkit, algorithmic-art, slack-gif-creator, theme-factory
- docx, pdf, xlsx, doc-coauthoring

**Infrastructure & DevOps:**
- tmux, homeassistant, sonoscli, docker-essentials
- github, vercel-deploy-claimable, api-designer

**Research & Intelligence:**
- pokee-deep-research, perplexity-deep-search
- web-search, reddit-insights, arxiv-watcher
- scout skills

**Orchestration:**
- orchestrator, workflow-registry, workflow-runner.sh

### Agent Roles

| Agent | Specialty | Key Skills |
|-------|-----------|------------|
| **Scribe** | Content creation | doc-coauthoring, theme-factory, brand-guidelines, seo-optimizer |
| **Builder** | Development | mcp-builder, webapp-testing, algorithmic-art, remotion |
| **Scout** | Research | pokee, perplexity, reddit-insights, web-search |
| **Keeper** | System operations | cron-mastery, backup, homeassistant, sonoscli |
| **Hunter** | Career | job-auto-apply, linkedin-automation |

### Credentials Inventory
**Location:** `~/.openclaw/workspace/.credentials/`

| Service | File | Status |
|---------|------|--------|
| GitHub | github.txt | ✅ Active |
| Pokee Deep Research | pokee-deep-research.txt | ✅ Active |
| Manus AI | manus.txt | ✅ Active |

### Pokee Deep Research Skill

**GitHub Repository:** https://github.com/Niraven/pokee-deep-research-skill

**Architecture:**
- **SKILL.md** — Interface definition for OpenClaw agent
- **pokee_research.py** — Core Python script with subprocess curl
- **setup.py** — Credential management wizard
- **API Endpoint:** `https://deepresearch.pokee.ai/deep-research`
- **Output:** 3 files (outline.md, writeup.md, response.json) → `research-output/`

**Why subprocess curl?** Handles 30+ min timeouts better than Python requests

**Technical Implementation:**
```python
# Multi-path credential discovery
CREDENTIAL_PATHS = [
    Path.home() / ".openclaw/workspace/.credentials/pokee-deep-research.txt",
    # Fallback paths for different install locations
]

# API call with 30-min timeout
curl_cmd = [
    "curl", "--silent", "--location",
    "--header", "Content-Type: application/json",
    "--header", f"Authorization: Bearer {token}",
    "--data", json.dumps({"query": query}),
    "--max-time", "1800",  # 30 min
    "https://deepresearch.pokee.ai/deep-research"
]
```

---

### Pokee Deep Research — Live Stream Tutorial (Upcoming)

**Date:** Thursday (TBD with Kiri)  
**Format:** Technical tutorial — BUILDING the skill from scratch  
**Duration:** 45-60 minutes  
**Co-host:** Kiri from Pokee AI  
**Audience:** Developers, OpenClaw users who want to build skills

**Full Script:** `POKEE_LIVE_STREAM_SCRIPT.md` (detailed 60-min structure)

**Stream Structure:**
| Time | Section | Content |
|------|---------|---------|
| 0:00-3:00 | Opening | Problem: Surface-level AI vs. real research |
| 3:00-8:00 | Architecture | What is an OpenClaw skill? How Pokee API works |
| 8:00-15:00 | Live Coding | Build `pokee_research.py` — credentials, curl, parsing |
| 15:00-22:00 | SKILL.md | Creating the interface for LLM to use |
| 22:00-30:00 | Demo | Install, setup, run live research |
| 30:00-40:00 | Output Analysis | Outline, writeup, JSON — what's in each |
| 40:00-50:00 | Extensions | Cron jobs, chaining, error handling |
| 50:00-55:00 | Open Source | MIT license, PokeeResearch-7B model |
| 55:00-60:00 | Q&A | Audience questions, live research request |

**Key Technical Points to Cover:**
1. **Skill anatomy** — SKILL.md + executable + credentials
2. **Why subprocess curl** — Timeout handling for 25+ min requests
3. **Credential discovery** — Multiple fallback paths
4. **Response parsing** — Extract outline, writeup, JSON from API
5. **Integration** — Files land in workspace, no copy-paste

**Positioning Pokee:**
- SOTA 7B model (beats larger models on GAIA, BrowseComp)
- 75% cheaper than OpenAI/Gemini/Perplexity
- Open source (skill + model both MIT licensed)
- Multi-turn research vs. one-shot summarization

**Pre-Stream Checklist:**
- [ ] Test skill on clean machine
- [ ] Prepare API token + backup
- [ ] Have 2-3 research topics ready
- [ ] Screen share test (terminal + browser)
- [ ] Kiri tech check (10 min before)

**Demo Research Topics (ready to use):**
1. "State of MCP server ecosystem 2025" (meta!)
2. "Competitive analysis of AI presentation tools"
3. "EV charging infrastructure: who owns what in 2025"

**Quick Demo Flow (if short on time):**
1. **Introduction (30 sec)** — "Let me show you the Pokee Deep Research skill in action"
2. **Show It's Available (1 min)** — Read SKILL.md, confirm API key configured
3. **Pick a Topic (30 sec)** — User provides complex research question (e.g., "competitive analysis of vector databases for AI apps", "state of MCP server ecosystem")
4. **Run It (7-25 min)** — Execute skill, show real-time progress: outline → research loops → synthesis → final report
5. **Review Output (3-5 min)** — Show structured outline, full 50-70KB report, JSON for automation, workspace file locations
6. **Q&A / Wrap** — Handle questions

**Key Talking Points:**
- Solves the 3-4 hour research vs shallow summary tradeoff
- Multi-step structured research process (not just summarization)
- **Outputs: 3 files** — structured outline, full write-up (~50-70KB), AND raw JSON for automation
- Raw JSON is critical for piping into other workflows, Notion sync, custom tooling
- Runs 7-25 minutes for real depth
- Files land directly in OpenClaw workspace (`research-output/`)

### User Preferences
- **Role:** Chief architect, AI expert
- **Expectation:** Proactive self-improvement, zero mistakes
- **Timezone:** Europe/Berlin

### Active Projects
1. **Skill System Expansion** - 86 ghost skills fixed, 141 total active (Feb 20, 2026)
2. **Orchestration Framework** - workflow-registry + runner
3. **Self-Evolution System** - Proactive mode activated with task queue + learning capture
4. **Master Workflows Defined** (SKILL_WORKFLOW_MATRIX.md)
   - WF-001: Full-Stack Application Deployment
   - WF-002: Autonomous Research & Publication
   - WF-003: Security Hardening Sprint
   - WF-004: Multi-Agent Content Studio
   - WF-005: Skill Development Factory
   - WF-006: Job Hunt Automation
   - WF-007: Smart Home DevOps
   - WF-008: Financial Intelligence
   - WF-009: Knowledge Management
   - WF-010: API Integration Factory

---

## Self-Evolution System (Active Feb 20, 2026)

### Infrastructure
| Component | File | Purpose |
|-----------|------|---------|
| **Task Queue** | `tasks/QUEUE.md` | Ready/In Progress/Blocked/Done kanban |
| **Heartbeat** | `HEARTBEAT.md` | Daily work rotation, DO WORK not just checks |
| **Learnings** | `skills/self-improving-agent/.learnings/` | Capture corrections, errors, discoveries |
| **Consolidation** | `MEMORY.md` | Promote high-value learnings weekly |

### Daily Rotation
- **Monday:** System health + backups
- **Tuesday:** Intelligence gathering (arxiv, reddit, perplexity)
- **Wednesday:** Skill improvements
- **Thursday:** Security audit (tinman)
- **Friday:** Weekly review + learning consolidation
- **Saturday:** Light — system status only
- **Sunday:** Planning + priority queue

### Key Learnings (Feb 20, 2026)

**1. Ghost Skills Discovery**
86 skill directories had only `.clawdhub/` metadata, no SKILL.md files. Root cause: Failed ClawHub bulk install on Feb 13, 2026. Fix: Batch-created SKILL.md files for all 86.

**2. Self-Evolution Requires Infrastructure**
Being proactive requires more than intent — needs task queue (what to do), learning logs (what was learned), and heartbeat integration (when to do it).

**3. Batch Operations > Perfection**
Creating 77 functional SKILL.md files with sensible defaults is better than hand-crafting 9 perfect ones and leaving 77 broken. Iterate on quality later.

**4. Skill Priority Matrix**
When fixing 86 skills, prioritize by leverage:
1. Meta-skills (self-improving-agent)
2. Automation (cron, backup)
3. Intelligence (arxiv, reddit, perplexity)
4. Infrastructure (database, security)
5. Everything else (batch when needed)
