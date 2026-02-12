#!/usr/bin/env python3
"""Pokee Deep Research - Core research functionality."""
import os
import sys
import json
import subprocess
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

def save_results(query, response_text):
    """Save research results to output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    basename = sanitize_filename(query)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save raw JSON response
    json_file = OUTPUT_DIR / f"{basename}_{timestamp}_response.json"
    json_file.write_text(response_text)
    
    # Try to parse and extract fields
    try:
        data = json.loads(response_text)
        
        # Extract and save outline from output_data
        if "output_data" in data and "formatted_outline" in data["output_data"]:
            outline_file = OUTPUT_DIR / f"{basename}_{timestamp}_outline.md"
            outline_file.write_text(data["output_data"]["formatted_outline"])
            print(f"Saved outline to: {outline_file}")
        
        # Extract and save writeup from output_data
        if "output_data" in data and "formatted_writeup" in data["output_data"]:
            writeup_file = OUTPUT_DIR / f"{basename}_{timestamp}_writeup.md"
            writeup_file.write_text(data["output_data"]["formatted_writeup"])
            print(f"Saved writeup to: {writeup_file}")
        
        return True
    except json.JSONDecodeError:
        print("Warning: Response is not valid JSON")
        return False

def conduct_research(query):
    """Call Pokee Deep Research API using curl (works better than requests)."""
    token = get_api_token()
    if not token:
        print("❌ Error: No API token found")
        print("Run: python3 scripts/setup.py")
        return None
    
    print(f"🔬 Researching: {query}")
    print("This will take 7-25 minutes...")
    print("Started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("")
    
    # Use curl command exactly like the working bash script
    # This matches what worked on the user's Mac
    curl_cmd = [
        "curl", "--silent", "--location",
        "--header", "Content-Type: application/json",
        "--header", f"Authorization: Bearer {token}",
        "--data", json.dumps({"query": query}),
        "--max-time", "1800",  # 30 minutes max
        API_URL
    ]
    
    try:
        result = subprocess.run(
            curl_cmd,
            capture_output=True,
            text=True,
            timeout=1860  # 31 minutes
        )
        
        if result.returncode != 0:
            print(f"❌ Curl error: {result.stderr}")
            return None
        
        return result.stdout
        
    except subprocess.TimeoutExpired:
        print("❌ Request timed out after 31 minutes")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: pokee_research.py 'Your research question'")
        print("")
        print("Example:")
        print('  ./scripts/pokee-research.sh "Best AI tools for students"')
        sys.exit(1)
    
    query = sys.argv[1]
    response_text = conduct_research(query)
    
    if response_text:
        print("✅ Research complete!")
        print("Finished:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("")
        
        if save_results(query, response_text):
            print(f"")
            print(f"📁 Results saved to: {OUTPUT_DIR}")
            
            # Show preview
            try:
                data = json.loads(response_text)
                if "output_data" in data and "formatted_writeup" in data["output_data"]:
                    preview = data["output_data"]["formatted_writeup"][:300] + "..."
                    print(f"")
                    print(f"📝 Preview:")
                    print(preview)
            except:
                pass
        else:
            print("Response saved as raw JSON")
    else:
        print("")
        print("❌ Research failed or timed out")
        sys.exit(1)

if __name__ == "__main__":
    main()
