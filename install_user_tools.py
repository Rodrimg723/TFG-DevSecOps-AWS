import os
import urllib.request
import zipfile
import shutil
import subprocess
import sys

# Constants
TERRAFORM_VERSION = "1.7.4"
TERRAFORM_URL = f"https://releases.hashicorp.com/terraform/{TERRAFORM_VERSION}/terraform_{TERRAFORM_VERSION}_linux_amd64.zip"
VENV_DIR = os.path.abspath(".venv")
VENV_BIN = os.path.join(VENV_DIR, "bin")

def create_venv():
    print(f"Creating virtual environment in {VENV_DIR}...")
    subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])

def install_ansible():
    print("Installing Ansible in venv...")
    pip_path = os.path.join(VENV_BIN, "pip")
    try: 
        subprocess.check_call([pip_path, "install", "ansible"])
        print("Ansible installed successfully.")
    except Exception as e:
        print(f"Failed to install Ansible in venv: {e}")
        sys.exit(1)

def install_terraform():
    print("Installing Terraform...")
    zip_path = "terraform.zip"
    try:
        # Download
        print(f"Downloading from {TERRAFORM_URL}...")
        urllib.request.urlretrieve(TERRAFORM_URL, zip_path)
        
        # Unzip
        print("Extracting...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
            
        # Move to venv bin
        if not os.path.exists(VENV_BIN):
            os.makedirs(VENV_BIN)
        
        dest = os.path.join(VENV_BIN, "terraform")
        if os.path.exists(dest):
            os.remove(dest)
            
        shutil.move("terraform", dest)
        # Clean up
        if os.path.exists(zip_path):
            os.remove(zip_path)
        
        # Make executable
        os.chmod(dest, 0o755)
        
        print(f"Terraform installed to {dest}")
    except Exception as e:
        print(f"Failed to install Terraform: {e}")
        sys.exit(1)

if __name__ == "__main__":
    create_venv()
    install_ansible()
    install_terraform()
