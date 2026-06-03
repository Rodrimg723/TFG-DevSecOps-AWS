#!/bin/bash
set -e

echo "Starting setup for DevSecOps TFG..."

# 1. Update and install dependencies
echo "[1/3] Installing dependencies (python3-venv, unzip, etc)..."
sudo apt-get update
sudo apt-get install -y software-properties-common python3-venv python3-pip unzip curl git

# 2. Install Ansible
echo "[2/3] Installing Ansible..."
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt-get install -y ansible

# 3. Install Terraform
echo "[3/3] Installing Terraform..."
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt-get update
sudo apt-get install -y terraform

echo "Setup complete!"
ansible --version | head -n 1
terraform --version
