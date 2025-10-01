#!/bin/bash
# ec2-setup.sh
# Automated setup script for EC2 to prepare for CI/CD pipeline

set -e

echo "Starting EC2 setup..."

if [ -f /etc/debian_version ]; then
    OS="ubuntu"
    echo "Detected Ubuntu"
    sudo apt update -y
    sudo apt install -y docker.io git
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker ubuntu
elif [ -f /etc/system-release ]; then
    OS="amazon-linux"
    echo "Detected Amazon Linux"
    sudo yum update -y
    sudo amazon-linux-extras install docker -y
    sudo service docker start
    sudo usermod -aG docker ec2-user
else
    echo "Unsupported OS"
    exit 1
fi

if ! command -v docker &> /dev/null
then
    echo "Docker installation failed."
    exit 1
fi

echo "Docker installed successfully."
docker --version

newgrp docker <<EONG
echo "Docker group updated for $OS user."
EONG

echo "EC2 setup completed."
