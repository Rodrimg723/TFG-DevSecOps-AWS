#!/bin/bash
rsync -av /mnt/c/Users/rodri/.gemini/antigravity/scratch/terraform/ ~/terraform_run/
cd ~/terraform_run

rm -rf .terraform .terraform.lock.hcl
terraform init
terraform apply -auto-approve

cp terraform.tfstate /mnt/c/Users/rodri/.gemini/antigravity/scratch/terraform/terraform.tfstate
