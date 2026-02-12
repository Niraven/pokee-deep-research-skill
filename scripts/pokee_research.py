#!/usr/bin/env python3
"""Pokee Deep Research - Core research functionality."""
import os
import sys
import json
import requests
import re
from pathlib import Path
from datetime import datetime

# Try multiple credential locations
CREDENTIAL_PATHS = [
    Path.home() / ".openclaw" / "workspace" / ".credentials" / "pokee-deep-research.txt",
    Path.home() / ".openclaw" / "skills" / "pokee-deep-research" / ".credentials" / "pokee-deep-research.txt",
    Path(".credentials") / "pokee-deep-research.txt",
]

OUTPUT_DIR = Path.home() / ".openclaw" / "workspace" / "research-output"
API_URL = "https://deepresearch.pokee.ai/deep-research"

def get_api_token():
    """Find API token from credential files."""
    for path in CREDENTIAL_PATHS:
        if path.exists():
            token = path.read_text().strip()
            if token:
                return token
    return None

def sanitize_filename(query):
    """Create safe filename from query."""
    clean = re.sub(r'[^\w\s-]', '', query.lower())
    clean = re.sub(r'[-\s]+', '-', clean)
    return clean[:50]

def save_results(query, data):
    """Save research results to output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    basename = sanitize_filename(query)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Save JSON response
    json_file = OUTPUT_DIR / f"{basename}_{timestamp}_response.json"
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)
    
    # Extract and save outline from output_data
    if "output_data" in data and "formatted_outline" in data["output_data"]:
        outline_file = OUTPUT_DIR / f"{basename}_{timestamp}_outline.md"
        outline_file.write_text(data["output_data"]["formatted_outline"])
    elif "outline" in data:
        outline_file = OUTPUT_DIR / f"{basename}_{timestamp}_outline.md"
        outline_file.write_text(data["outline"])
    
    # Extract and save writeup from output_data
    if "output_data" in data and "formatted_writeup" in data["output_data"]:
        writeup_file = OUTPUT_DIR / f"{basename}_{timestamp}_writeup.md"
        writeup_file.write_text(data["output_data"]["formatted_writeup"])
    elif "writeup" in data:
        writeup_file = OUTPUT_DIR / f"{basename}_{timestamp}_writeup.md"
        writeup_file.write_text(data["writeup"])
    
    return OUTPUT_DIR

def conduct_research(query):
    """Call Pokee Deep Research API."""
    token = get_api_token()
    if not token:
        print("❌ Error: No API token found")
        print("Run: python3 scripts/setup.py")
        return None
    
    print(f"🔬 Researching: {query}")
    print("This may take 7-25 minutes...")
    print("(Do not interrupt - research is running on Pokee's servers)")
    print("")
    
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"query": query}
    
    try:
        # Note: Timeout is 1500 seconds (25 minutes) to match Pokee's documented timing
        response = requests.post(API_URL, json=payload, headers=headers, timeout=1500)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out")
        print("The Deep Research API takes 7-25 minutes depending on query complexity.")
        print("This is normal - please try again with a simpler query or wait longer.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: pokee_research.py 'Your research question'")
        sys.exit(1)
    
    query = sys.argv[1]
    data = conduct_research(query)
    
    if data:
        output_dir = save_results(query, data)
        print(f"\n✅ Research complete!")
        print(f"📁 Results saved to: {output_dir}")
        
        # Show preview from output_data if available
        if "output_data" in data and "formatted_writeup" in data["output_data"]:
            preview = data["output_data"]["formatted_writeup"][:500] + "..."
            print(f"\n📝 Preview:\n{preview}")
        elif "writeup" in data:
            preview = data["writeup"][:500] + "..."
            print(f"\n📝 Preview:\n{preview}")

if __name__ == "__main__":
    main()
