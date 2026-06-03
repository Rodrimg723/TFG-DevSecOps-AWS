#!/bin/bash
cd ~/terraform_run
terraform destroy -auto-approve
cp terraform.tfstate /mnt/c/Users/rodri/.gemini/antigravity/scratch/terraform/terraform.tfstate
