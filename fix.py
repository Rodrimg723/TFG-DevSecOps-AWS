import subprocess
import re

try:
    container = subprocess.check_output("sudo docker compose ps -q crowdsec", shell=True, text=True).strip()
    subprocess.call(f"sudo docker exec {container} cscli bouncers delete traefik-bouncer", shell=True)
    key = subprocess.check_output(f"sudo docker exec {container} cscli bouncers add traefik-bouncer", shell=True, text=True).strip()
    
    with open("docker-compose.yml", "r") as f:
        content = f.read()

    new_content = re.sub(r'CROWDSEC_BOUNCER_API_KEY=.*', f'CROWDSEC_BOUNCER_API_KEY={key}', content)
    
    with open("docker-compose.yml", "w") as f:
        f.write(new_content)
        
    subprocess.call("sudo docker compose up -d", shell=True)
    print("FIXED")
except Exception as e:
    print(f"Error: {e}")
