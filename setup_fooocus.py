import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
    else:
        print(f"Successfully executed: {command}")
        print(f"Output: {result.stdout}")

# Set up environment
commands = [
    # Navigate to project directory
    "cd code/Foocus/FooocusAPI",
    
    # Activate virtual environment
    "source venv/bin/activate",
    
    # Update and install Python 3.10
    "sudo apt-get update",
    "sudo apt-get upgrade",
    "sudo apt-get install -y software-properties-common",
    "sudo add-apt-repository ppa:deadsnakes/ppa",
    "sudo apt-get update",
    "sudo apt-get install -y python3.10",
    "python --version",
    
    # Start the application
    "python main.py",
    
    # Docker installation and setup
    "sudo apt-get update",
    "sudo apt install apt-transport-https ca-certificates curl software-properties-common",
    "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
    'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"',
    "sudo apt-get update",
    "sudo apt install docker-ce",
    "sudo systemctl status docker",
    
    # Docker cleanup and reinstallation
    "sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras",
    "sudo rm -rf /var/lib/docker",
    "sudo rm -rf /var/lib/containerd",
    'for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done',
    "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin",
    "sudo systemctl restart docker",
    
    # Prune Docker system
    "docker system prune -a",
    
    # Build and run Docker containers
    "docker-compose build",
    "docker-compose up",
    
    # Check and restart Docker
    "sudo systemctl restart docker",
    "sudo systemctl status docker",
    
    # Fix port conflict in Docker configuration
    "sudo sed -i 's/1414/80/g' /path/to/nginx.conf /path/to/docker-compose.yml",
    
    # Fix daemon.json configuration
    'echo \'{"runtimes": {"nvidia": {"path": "nvidia-container-runtime","runtimeArgs": []},"default-runtime": "nvidia"}}\' | sudo tee /etc/docker/daemon.json',
    "sudo systemctl restart docker",
    
    # Reinstall NVIDIA container toolkit
    "distribution=$(. /etc/os-release;echo $ID$VERSION_ID)",
    "curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -",
    'curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list',
    "sudo apt-get update",
    "sudo apt-get install -y nvidia-docker2",
    "sudo systemctl restart docker",
    
    # Install and start Nginx
    "sudo apt update",
    "sudo apt install nginx"
]

for command in commands:
    run_command(command)

