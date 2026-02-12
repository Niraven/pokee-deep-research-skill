#!/usr/bin/env python3
"""Setup wizard for Pokee Deep Research skill."""
import os
import sys

def main():
    print("🔧 Pokee Deep Research - Setup")
    print("=" * 40)
    
    token = input("\nEnter your Pokee API token: ").strip()
    if not token:
        print("❌ Token required")
        sys.exit(1)
    
    # Save to workspace .credentials
    cred_dir = os.path.expanduser("~/.openclaw/workspace/.credentials")
    os.makedirs(cred_dir, exist_ok=True)
    
    cred_file = os.path.join(cred_dir, "pokee-deep-research.txt")
    with open(cred_file, "w") as f:
        f.write(token)
    os.chmod(cred_file, 0o600)
    
    print(f"✓ Token saved to {cred_file}")
    print("\n🎉 Setup complete! You can now run:")
    print("  ./scripts/pokee-research.sh 'Your research question'")

if __name__ == "__main__":
    main()
