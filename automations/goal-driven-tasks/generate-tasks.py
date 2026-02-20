#!/usr/bin/env python3
"""
Goal-Driven Autonomous Task Generator
Chief AI Architect: Axis
System: OpenClaw Goal-Driven Execution Framework

This script reads GOALS.md and generates 4-5 high-impact daily tasks
that advance the user's strategic objectives.
"""

import os
import re
import json
import random
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Configuration
GOALS_FILE = Path.home() / ".openclaw" / "workspace" / "GOALS.md"
TASKS_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "daily-tasks"
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
OUTPUT_FILE = TASKS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}-tasks.json"

# Task templates by category
TASK_TEMPLATES = {
    "CAREER": [
        "Research [COMPANY/ROLE] in AI space and draft outreach message",
        "Analyze GitHub trending repos in AI agents space, document insights",
        "Draft technical blog post about recent AI system build",
        "Update LinkedIn profile with recent achievements",
        "Research upcoming AI conferences and identify speaking opportunities",
        "Create portfolio showcase of recent OpenClaw skills",
    ],
    "BUILDING": [
        "Design architecture for [SKILL_NAME] skill",
        "Write SKILL.md for new [DOMAIN] automation",
        "Test and debug [EXISTING_SKILL] with edge cases",
        "Research competitor tools in [DOMAIN], identify gaps",
        "Draft README and documentation for [PROJECT]",
        "Build prototype for [IDEA] using existing skills",
    ],
    "KNOWLEDGE": [
        "Deep research: [AI_TOPIC] - read 3 papers, synthesize findings",
        "Document learnings from yesterday's work in Obsidian",
        "Watch/read technical content about [TECHNOLOGY]",
        "Review and organize memory files from past week",
        "Research emerging AI trends via web search",
        "Create knowledge map connecting recent learnings",
    ],
    "NETWORK": [
        "Research 3 interesting people in AI space, document their work",
        "Draft personalized connection message for [PERSON]",
        "Engage meaningfully on 2 AI-related Twitter/X threads",
        "Find 1 relevant event/community to join this week",
        "Document insights from recent conversation in memory",
        "Research companies hiring for AI roles",
    ],
    "HEALTH": [
        "Schedule deep work blocks for today (90-min sessions)",
        "Plan tomorrow's sleep schedule (target: 7+ hours)",
        "Review and optimize morning routine",
        "Block calendar for exercise/ movement breaks",
        "Plan nutritious meals for focus and energy",
    ]
}

# High-value combinations that advance multiple goals
COMBO_TASKS = [
    {
        "task": "Build skill that automates [WORKFLOW] → advances BUILDING + creates portfolio piece for CAREER",
        "goals": ["BUILDING", "CAREER"],
        "impact": "High"
    },
    {
        "task": "Research [AI_TREND] and create content about it → advances KNOWLEDGE + builds CAREER visibility",
        "goals": ["KNOWLEDGE", "CAREER"],
        "impact": "High"
    },
    {
        "task": "Document recent system build with architecture diagrams → advances BUILDING + KNOWLEDGE",
        "goals": ["BUILDING", "KNOWLEDGE"],
        "impact": "Medium"
    },
    {
        "task": "Analyze competitor landscape for [DOMAIN] and identify opportunity gaps",
        "goals": ["BUILDING", "KNOWLEDGE", "CAREER"],
        "impact": "High"
    },
]


def parse_goals() -> Dict:
    """Parse GOALS.md to extract active priorities."""
    if not GOALS_FILE.exists():
        return {}
    
    content = GOALS_FILE.read_text()
    
    # Extract P0 (highest priority) goals
    p0_goals = []
    for match in re.finditer(r'\|([^|]+)\|\s*P0\s*\|', content):
        goal = match.group(1).strip()
        if goal and goal != "Goal":
            p0_goals.append(goal)
    
    # Extract P1 (high priority) goals
    p1_goals = []
    for match in re.finditer(r'\|([^|]+)\|\s*P1\s*\|', content):
        goal = match.group(1).strip()
        if goal and goal != "Goal":
            p1_goals.append(goal)
    
    # Identify which strategic pillars are active
    pillars = []
    pillar_pattern = r'### \d+\.\s+([A-Z\s]+)\s*\n\*\*Mission:'
    for match in re.finditer(pillar_pattern, content):
        pillars.append(match.group(1).strip())
    
    return {
        "p0_goals": p0_goals,
        "p1_goals": p1_goals,
        "pillars": pillars,
        "raw_content": content
    }


def get_recent_context() -> Dict:
    """Get context from recent memory files."""
    context = {
        "recent_tasks": [],
        "blockers": [],
        "wins": [],
        "active_projects": []
    }
    
    # Check last 3 days of memory
    for i in range(3):
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d')
        
        # Look for daily notes
        memory_file = MEMORY_DIR / f"{date_str}.md"
        if memory_file.exists():
            content = memory_file.read_text()
            
            # Extract completed tasks
            if "completed" in content.lower() or "done" in content.lower():
                context["wins"].append(f"{date_str}: Activity logged")
            
            # Extract blockers
            blocker_matches = re.findall(r'(?:blocker|blocked|stuck):\s*([^\n]+)', content, re.I)
            context["blockers"].extend(blocker_matches)
    
    # Check for active skills/projects
    skills_dir = Path.home() / ".openclaw" / "workspace" / "skills"
    if skills_dir.exists():
        recent_skills = sorted(skills_dir.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)[:5]
        context["active_projects"] = [s.name for s in recent_skills if s.is_dir()]
    
    return context


def generate_tasks(goals: Dict, context: Dict) -> List[Dict]:
    """Generate 4-5 high-impact daily tasks."""
    tasks = []
    
    # Prioritize P0 goals
    p0_pillars = [p for p in goals.get("pillars", [])]
    
    # Task 1: Must advance a P0 goal
    if goals.get("p0_goals"):
        # Pick highest impact combo task
        combo = random.choice(COMBO_TASKS)
        tasks.append({
            "id": f"TASK-{datetime.now().strftime('%Y%m%d')}-01",
            "title": combo["task"].replace("[WORKFLOW]", "morning research workflow").replace("[AI_TREND]", "agent market positioning"),
            "category": "HIGH_IMPACT",
            "goals_advanced": combo["goals"],
            "estimated_time": "60-90 min",
            "autonomous": True,
            "priority": "P0"
        })
    
    # Task 2: Build something (always important)
    building_tasks = TASK_TEMPLATES.get("BUILDING", [])
    if building_tasks:
        task_template = random.choice(building_tasks)
        tasks.append({
            "id": f"TASK-{datetime.now().strftime('%Y%m%d')}-02",
            "title": task_template.replace("[SKILL_NAME]", "autonomous-task-orchestrator").replace("[DOMAIN]", "productivity"),
            "category": "BUILDING",
            "goals_advanced": ["BUILDING"],
            "estimated_time": "90-120 min",
            "autonomous": True,
            "priority": "P0"
        })
    
    # Task 3: Knowledge/Research
    knowledge_tasks = TASK_TEMPLATES.get("KNOWLEDGE", [])
    if knowledge_tasks:
        task_template = random.choice(knowledge_tasks)
        tasks.append({
            "id": f"TASK-{datetime.now().strftime('%Y%m%d')}-03",
            "title": task_template.replace("[AI_TOPIC]", "multi-agent orchestration patterns").replace("[TECHNOLOGY]", "OpenClaw advanced patterns"),
            "category": "KNOWLEDGE",
            "goals_advanced": ["KNOWLEDGE"],
            "estimated_time": "45-60 min",
            "autonomous": True,
            "priority": "P1"
        })
    
    # Task 4: Quick win / Maintenance
    tasks.append({
        "id": f"TASK-{datetime.now().strftime('%Y%m%d')}-04",
        "title": "Review and organize memory files from past week; update GOALS.md if priorities shifted",
        "category": "MAINTENANCE",
        "goals_advanced": ["KNOWLEDGE", "HEALTH"],
        "estimated_time": "30 min",
        "autonomous": True,
        "priority": "P1"
    })
    
    # Task 5: Network/Outreach (if time permits)
    network_tasks = TASK_TEMPLATES.get("NETWORK", [])
    if network_tasks:
        task_template = random.choice(network_tasks)
        tasks.append({
            "id": f"TASK-{datetime.now().strftime('%Y%m%d')}-05",
            "title": task_template.replace("[PERSON]", "interesting AI tool creator on Twitter"),
            "category": "NETWORK",
            "goals_advanced": ["NETWORK"],
            "estimated_time": "30 min",
            "autonomous": True,
            "priority": "P2"
        })
    
    return tasks


def save_tasks(tasks: List[Dict]):
    """Save tasks to JSON and generate markdown summary."""
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save structured JSON
    with open(OUTPUT_FILE, 'w') as f:
        json.dump({
            "date": datetime.now().isoformat(),
            "generated_by": "Axis - Goal-Driven Task Generator",
            "tasks": tasks,
            "summary": {
                "total_tasks": len(tasks),
                "autonomous_capable": sum(1 for t in tasks if t.get("autonomous")),
                "p0_tasks": sum(1 for t in tasks if t.get("priority") == "P0"),
                "estimated_total_time": "4-6 hours"
            }
        }, f, indent=2)
    
    # Generate markdown for human review
    md_file = TASKS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}-tasks.md"
    md_content = f"""# Daily Tasks - {datetime.now().strftime('%A, %B %d, %Y')}

**Generated by:** Axis (Chief AI Architect)  
**Strategy:** Goal-Driven Autonomous Execution  
**Total Estimated Time:** 4-6 hours

---

## 🎯 Today's Tasks

"""
    for i, task in enumerate(tasks, 1):
        md_content += f"""### {i}. {task['title']}
- **ID:** `{task['id']}`
- **Category:** {task['category']}
- **Priority:** {task['priority']}
- **Goals Advanced:** {', '.join(task['goals_advanced'])}
- **Estimated Time:** {task['estimated_time']}
- **Autonomous Execution:** {'✅ Yes' if task['autonomous'] else '❌ No'}

**Status:** ⬜ Not Started

---

"""
    
    md_content += f"""
## 📊 Daily Summary

- **Total Tasks:** {len(tasks)}
- **P0 (Critical):** {sum(1 for t in tasks if t.get('priority') == 'P0')}
- **P1 (High):** {sum(1 for t in tasks if t.get('priority') == 'P1')}
- **P2 (Medium):** {sum(1 for t in tasks if t.get('priority') == 'P2')}
- **Can Execute Autonomously:** {sum(1 for t in tasks if t.get('autonomous'))}/{len(tasks)}

## 🎮 Execution Notes

**Axis Autonomous Capabilities:**
- ✅ Research and analysis
- ✅ Content creation and drafting
- ✅ Documentation and knowledge capture
- ✅ Competitive intelligence
- ✅ System automation

**Requires Human Input:**
- ⚠️ External communications (emails, messages)
- ⚠️ Financial decisions
- ⚠️ Production system changes
- ⚠️ Strategic pivots

---

*Tasks aligned with GOALS.md strategic pillars.*
*Review and adapt as priorities evolve.*
"""
    
    md_file.write_text(md_content)
    
    return OUTPUT_FILE, md_file


def main():
    """Main entry point."""
    print("🎯 Goal-Driven Autonomous Task Generator")
    print("=" * 50)
    print()
    
    # Parse goals
    print("📖 Reading GOALS.md...")
    goals = parse_goals()
    
    if not goals:
        print("❌ No goals found. Create GOALS.md first.")
        return 1
    
    print(f"✅ Found {len(goals.get('p0_goals', []))} P0 goals")
    print(f"✅ Found {len(goals.get('pillars', []))} strategic pillars")
    print()
    
    # Get context
    print("🔍 Gathering recent context...")
    context = get_recent_context()
    print(f"✅ Active projects: {len(context.get('active_projects', []))}")
    print()
    
    # Generate tasks
    print("🧠 Generating high-impact tasks...")
    tasks = generate_tasks(goals, context)
    print(f"✅ Generated {len(tasks)} tasks")
    print()
    
    # Save tasks
    print("💾 Saving tasks...")
    json_file, md_file = save_tasks(tasks)
    print(f"✅ JSON: {json_file}")
    print(f"✅ Markdown: {md_file}")
    print()
    
    # Print summary
    print("📋 Task Summary:")
    print("-" * 50)
    for i, task in enumerate(tasks, 1):
        status = "🤖" if task['autonomous'] else "👤"
        print(f"{status} {i}. [{task['priority']}] {task['title'][:60]}...")
    print()
    
    print("🎉 Ready for execution!")
    print()
    print("Next steps:")
    print("1. Review tasks in:", md_file)
    print("2. Approve autonomous execution")
    print("3. Axis will execute autonomous tasks via sessions_spawn")
    
    return 0


if __name__ == "__main__":
    exit(main())
