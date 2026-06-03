import urllib.request
import json
import re
import sys

url = "https://forms.gle/oMPXA87UMnhVQy1AA"

try:
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
    
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')

    # Look for FB_PUBLIC_LOAD_DATA_
    match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);\s*var', content, re.DOTALL)
    if not match:
         match = re.search(r'var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);', content, re.DOTALL)

    if match:
        json_data = match.group(1)
        data = json.loads(json_data)
        
        # Fields are in data[1][1]
        fields = data[1][1]
        
        print("--- Form Structure ---")
        for f in fields:
            # f[1] = title
            # f[3] = type
            # f[4] = details (includes entry id)
            
            title = f[1]
            f_type = f[3]
            
            entry_id = "N/A"
            if len(f) > 4 and f[4] and len(f[4]) > 0 and len(f[4][0]) > 0:
                entry_id = f[4][0][0]
            
            print(f"Title: {title} | Type: {f_type} | Entry: {entry_id}")
            
            # Print choices if multiple choice (Type 2, 3, 4)
            if f_type in [2, 3, 4]:
                if len(f) > 4 and f[4] and len(f[4]) > 0 and len(f[4][0]) > 1:
                     choices = f[4][0][1]
                     # choices is a list of [choice_value, ...]
                     choice_values = [c[0] for c in choices if c and len(c) > 0]
                     print(f"  Choices: {choice_values}")

    else:
        print("FB_PUBLIC_LOAD_DATA_ not found")

except Exception as e:
    print(f"Error: {e}")
