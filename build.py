#!/usr/bin/env python3
import os

path = "/Users/feifei/.openclaw/workspace/ai-diff-checker/index.html"
parts = []

# Will be populated by append calls
# Run: python3 build.py to assemble
if os.path.exists(path + '.parts'):
    with open(path + '.parts', 'r') as f:
        content = f.read()
    with open(path, 'w') as f:
        f.write(content)
    print(f"Written {len(content)} bytes to {path}")
