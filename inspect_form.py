import urllib.request
import re

url = "https://forms.gle/oMPXA87UMnhVQy1AA"

try:
    print(f"Fetching {url}...")
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
    
    # Pattern to find entry IDs
    # Often found in FB_PUBLIC_LOAD_DATA_
    
    print("Searching for entry IDs...")
    
    # Just printing all occurrences of entry. followed by numbers
    entries = set(re.findall(r'entry\.\d+', content))
    
    print("Found entries:", entries)
    
    # Also look for the form action URL. 
    # Mapped from the form or constructed. 
    # Usually `https://docs.google.com/forms/u/0/d/e/{form_id}/formResponse`
    
    action_match = re.search(r'action="https://docs\.google\.com/forms/[^"]+"', content)
    if action_match:
        print("Form Action:", action_match.group(0))
    else:
        # Search for the form ID to construct the URL
        # "https://docs.google.com/forms/d/e/1FAIpQLSf..."
        # It's usually in the `FB_PUBLIC_LOAD_DATA_` variable or meta tags
        pass

    # Save to file for manual inspection if needed
    with urllib.request.urlopen(url) as response:
         full_content = response.read().decode('utf-8')
         with open("form_source.html", "w", encoding="utf-8") as f:
            f.write(full_content)
        
except Exception as e:
    print(f"Error: {e}")
