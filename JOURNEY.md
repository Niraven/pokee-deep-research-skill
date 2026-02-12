# Pokee Deep Research Skill - Development Journey

## 🎉 SUCCESS! The Skill is LIVE and WORKING!

**Repository:** https://github.com/Niraven/pokee-deep-research-skill  
**Status:** ✅ Production Ready  
**Date:** 2026-02-12

---

## The Journey (What We Went Through)

### Phase 1: Initial Discovery (Day 1)
- Discovered Pokee's Deep Research API
- Found the open source repository
- Identified the API endpoint
- First attempts with wrong endpoint (`api.pokee.ai/v1/deep-research`)

### Phase 2: The Struggle (Day 1-2, ~20+ hours of debugging)
- ❌ Used Python `requests` library (timed out on server)
- ❌ Thought the API was broken
- ❌ Multiple token generations
- ❌ Extensive diagnostics and false conclusions
- ❌ Believed the API was non-responsive

### Phase 3: The Breakthrough (Day 2, Hour ~20)
- ✅ User tested on Mac with official Pokee bash script
- ✅ Script WORKED in 7 minutes
- ✅ Discovered: `curl` works, `requests` doesn't (on this server)
- ✅ Realized the issue was **my environment**, not the API

### Phase 4: The Fix (Day 2, Hour ~22)
- ✅ Replaced Python `requests` with `subprocess.run(curl...)`
- ✅ Matched exact curl command from working bash script
- ✅ Added proper error handling
- ✅ Tested successfully

### Phase 5: Verification (Day 2, Hour ~23)
**Test 1:** Meditation research
- Query: "What are 3 benefits of meditation"
- Time: **3 minutes 26 seconds**
- Status: ✅ SUCCESS
- Files: outline.md (6.4KB), response.json (32KB), writeup.md (24KB)

**Test 2:** Prompt engineering research  
- Query: "Best ways to prompt engineer for all use cases 2025"
- Time: **5 minutes 56 seconds**
- Status: ✅ SUCCESS
- Files: outline.md (14KB), response.json (132KB), writeup.md (112KB)

**Test 3:** AI coding assistants (ongoing as of documentation)
- Query: "Best AI coding assistants comparison 2025"
- Status: ⏳ IN PROGRESS

---

## Total Timeline

- **Start:** February 11, 2026
- **Breakthrough:** February 12, 2026 (~20 hours later)
- **Working Skill:** February 12, 2026 (~23 hours later)
- **Total Duration:** ~2 days
- **Actual Fix Time:** ~1 hour (once we knew the problem)
- **Learning Curve:** Priceless

---

## Key Technical Decisions

### Why Curl Instead of Requests?
```python
# ❌ DIDN'T WORK (times out)
import requests
requests.post(url, json=data, headers=headers, timeout=1500)

# ✅ WORKS (completes successfully)
import subprocess
subprocess.run([
    "curl", "--silent", "--location",
    "--header", "Content-Type: application/json",
    "--header", f"Authorization: Bearer {token}",
    "--data", json.dumps({"query": query}),
    "--max-time", "1800",
    "https://deepresearch.pokee.ai/deep-research"
], capture_output=True, timeout=1860)
```

**Reason:** Unknown network/firewall issue with Python's requests library on this server. Curl handles the connection differently and succeeds.

---

## How It Works Now

```
User Query
    ↓
./scripts/pokee-research.sh
    ↓
python3 scripts/pokee_research.py
    ↓
curl --location \
  --header "Authorization: Bearer TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"query": "..."}' \
  --max-time 1800 \
  https://deepresearch.pokee.ai/deep-research
    ↓
Pokee API (7-25 min research)
    ↓
Response JSON
    ↓
Parse and save files:
  - {timestamp}_outline.md
  - {timestamp}_writeup.md
  - {timestamp}_response.json
```

---

## Installation (For Yi Wan or Others)

```bash
# 1. Clone repo
mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
git clone https://github.com/Niraven/pokee-deep-research-skill.git pokee-deep-research
cd pokee-deep-research

# 2. Setup token (if not already configured)
python3 scripts/setup.py
# Enter your Pokee API token when prompted

# 3. Run research
./scripts/pokee-research.sh "Your research question here"

# 4. Wait 7-25 minutes

# 5. Check results
ls ~/.openclaw/workspace/research-output/
```

---

## Output Files

For each research query, the skill creates:

| File | Content | Size (example) |
|------|---------|----------------|
| `{timestamp}_outline.md` | Structured research outline | 6-14 KB |
| `{timestamp}_writeup.md` | Full research report | 24-112 KB |
| `{timestamp}_response.json` | Raw API response with sources | 32-132 KB |

---

## API Details

- **Endpoint:** `https://deepresearch.pokee.ai/deep-research`
- **Method:** POST
- **Auth:** Bearer Token
- **Timeout:** 30 minutes (1800 seconds)
- **Response Time:** 3-25 minutes depending on query complexity
- **Token Location:** `~/.openclaw/workspace/.credentials/pokee-deep-research.txt`

---

## Lessons Learned

1. **Don't assume the API is broken** - Test with the simplest possible client first
2. **User's environment ≠ Your environment** - What works on Mac may not work on server
3. **Use standard tools when possible** - Curl is more reliable than requests in some cases
4. **Document the journey** - Future you will thank present you
5. **Test twice, commit once** - Verified with multiple queries
6. **Persistence pays off** - Almost 2 days of debugging for a 1-hour fix

---

## Final Status

- ✅ Code: Working
- ✅ Tests: Passed (2/2, 3rd pending)
- ✅ Documentation: Complete
- ✅ Repo: Updated
- ✅ Skill: Ready for production

**Total time from "not working" to "production ready":** ~2 days  
**Actual fix time:** ~1 hour (once we knew the problem)  
**Learning curve:** Priceless

---

## Celebrations 🎉

- We didn't give up (for 2 days!)
- We listened to the user
- We tested properly
- We documented everything
- The skill is now genuinely useful

**Result:** A working OpenClaw skill that conducts deep research in 3-25 minutes!

**Special thanks to the user for not giving up and testing on their Mac!** 🙏
