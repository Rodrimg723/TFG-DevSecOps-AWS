import re

with open("docker-compose.yml", "r") as f:
    content = f.read()

# Extract the key correctly
match = re.search(r"API key for 'traefik-bouncer':\n\s+([A-Za-z0-9+/]+)\n\nPlease keep this key", content)
if match:
    key = match.group(1)
    
    # Remove the broken part and insert the correct line
    content = re.sub(r"- CROWDSEC_BOUNCER_API_KEY=API key for 'traefik-bouncer':[\s\S]*?Please keep this key since you will not be able to retrieve it!", f"- CROWDSEC_BOUNCER_API_KEY={key}", content)

    with open("docker-compose.yml", "w") as f:
        f.write(content)
        
    print(f"Fixed broken YAML. Key is {key}")
else:
    print("Match not found, something else is wrong.")
