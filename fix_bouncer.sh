#!/bin/bash
ssh -o StrictHostKeyChecking=no -i ~/.ssh/labsuser.pem ubuntu@3.81.229.167 << 'EOF'
cd /opt/devsecops
CONTAINER=$(docker compose ps -q crowdsec)
KEY=$(docker exec $CONTAINER cscli bouncers add traefik-bouncer)
echo "Generated key: $KEY"
sed -i "s/my-secret-key/$KEY/" docker-compose.yml
docker compose up -d
EOF
