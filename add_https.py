import re

try:
    with open("docker-compose.yml", "r") as f:
        content = f.read()

    # Add Let's Encrypt config to Traefik
    traefik_repl = """      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
      - "--certificatesresolvers.myresolver.acme.email=rodrigo@asir.net"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./security/crowdsec:/var/log/traefik"
      - "letsencrypt:/letsencrypt\""""

    content = re.sub(r'      - "--entrypoints.web.address=:80"[\s\S]*?- "\./security/crowdsec:/var/log/traefik".*', traefik_repl, content)

    # Add Host rule to DVWA
    content = re.sub(r'traefik.http.routers.dvwa.rule=PathPrefix\(`/dvwa`\)', r'traefik.http.routers.dvwa.rule=Host(`34.230.92.122.nip.io`) && PathPrefix(`/dvwa`)', content)
    content = re.sub(r'traefik.http.routers.dvwa.entrypoints=web', r'traefik.http.routers.dvwa.entrypoints=websecure"\n      - "traefik.http.routers.dvwa.tls.certresolver=myresolver', content)

    # Add volume at the bottom
    if "letsencrypt:" not in content:
        content = content.replace("volumes:\n", "volumes:\n  letsencrypt:\n")

    with open("docker-compose.yml", "w") as f:
        f.write(content)

    import subprocess
    subprocess.call("sudo docker compose up -d", shell=True)
    print("HTTPS Added")
except Exception as e:
    print(f"Error: {e}")
