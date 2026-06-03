#!/bin/bash
cd /opt/devsecops || exit 1
CONTAINER=$(sudo docker compose ps -q crowdsec)
sudo docker exec "$CONTAINER" cscli bouncers delete traefik-bouncer 2>/dev/null || true
KEY=$(sudo docker exec "$CONTAINER" cscli bouncers add traefik-bouncer)
sed -i "s|CROWDSEC_BOUNCER_API_KEY=.*|CROWDSEC_BOUNCER_API_KEY=$KEY|" docker-compose.yml
sudo docker compose up -d
sudo docker exec "$CONTAINER" cscli decisions delete --all
