import urllib.request
import json
import re

url = "https://forms.gle/oMPXA87UMnhVQy1AA"

print("Fetching...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        
    match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);', content, re.DOTALL)
    if not match:
        match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);\s*var', content, re.DOTALL)

    if match:
        data = json.loads(match.group(1))
        fields = data[1][1]
        
        print("--- RAW CHOICES ---")
        for f in fields:
            # f[4][0][0] is entry ID
            if len(f) > 4 and f[4] and len(f[4]) > 0 and len(f[4][0]) > 0:
                entry_id = f[4][0][0]
                
                # Check for choices
                if len(f[4][0]) > 1:
                    choices_raw = f[4][0][1]
                    choices = [c[0] for c in choices_raw]
                    print(f"ID: {entry_id} Type: {f[3]}")
                    print(f"Choices: {choices!r}") # repr() shows strings with \u escapes if any
                else:
                    print(f"ID: {entry_id} Type: {f[3]} (No choices)")
                    
    else:
        print("No JSON found")
        
except Exception as e:
    print(e)
