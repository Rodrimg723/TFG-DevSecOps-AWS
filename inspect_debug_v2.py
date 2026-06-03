import urllib.request
import json
import re

url = "https://forms.gle/oMPXA87UMnhVQy1AA"

print(f"Fetching {url}...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8')

# 1. Look for FBZX
# <input type="hidden" name="fbzx" value="12345">
match_fbzx = re.search(r'name="fbzx"\s+value="([^"]+)"', content)
if match_fbzx:
    print(f"FBZX: {match_fbzx.group(1)}")
else:
    print("FBZX not found in HTML inputs. Searching script variables...")
    # Sometimes it's in FB_PUBLIC_LOAD_DATA_
    
# 2. Parse Fields for Required
match_data = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);\s*var', content, re.DOTALL)
if not match_data:
    match_data = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);', content, re.DOTALL)

if match_data:
    data = json.loads(match_data.group(1))
    fields = data[1][1]
    
    print("--- FIELDS ---")
    for f in fields:
        # f[4][0][2] is usually 1 for required?
        # Let's inspect f[4][0]
        # f[4] = [[entry_id, choices, required, ...]]
        
        entry_id = "N/A"
        is_required = False
        
        if len(f) > 4 and f[4] and len(f[4][0]) > 0:
            entry_id = f[4][0][0]
            if len(f[4][0]) > 2:
                is_required = (f[4][0][2] == 1)
        
        print(f"ID: {entry_id} | Required: {is_required} | Title: {f[1][:30]}...")

