#!/bin/bash

# This script automates the installation of Docker on Ubuntu.
# It performs the following steps:
# 1. Removes any existing older versions of Docker.
# 2. Updates the package lists.
# 3. Installs necessary dependencies.
# 4. Adds Docker's official GPG key.
# 5. Sets up the Docker stable repository.
# 6. Installs the latest version of Docker Engine, containerd, and Docker Compose.
# 7. Adds the current user to the 'docker' group to run commands without sudo.
# 8. Verifies the installation with a 'hello-world' container.

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Starting Docker installation process..."

# ============================ Step 1: Remove Old Versions ============================
echo "1. Removing any existing Docker packages..."
for pkg in docker.io docker-doc docker-compose docker-ce docker-ce-cli containerd.io runc; do
  sudo apt-get remove -y "$pkg" &>/dev/null || true
done
echo "Previous Docker packages removed (if they existed)."

# ============================ Step 2: Set up the Repository ============================
echo "2. Updating package index and installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

echo "Dependencies installed."

echo "3. Adding Docker's official GPG key..."
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "GPG key added."

echo "4. Setting up the Docker stable repository..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
echo "Repository configured."

# ============================ Step 3: Install Docker Engine ============================
echo "5. Installing the latest version of Docker Engine..."
sudo apt-get update -y
sudo apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin
echo "Docker Engine, containerd, and Compose installed successfully."

# ============================ Step 4: Configure User & Verify ============================
echo "6. Adding the current user to the 'docker' group..."
# The usermod command requires a valid username, so we use the current user.
sudo usermod -aG docker "$USER"
echo "Your user '$USER' has been added to the 'docker' group."

echo "--------------------------------------------------------"
echo "IMPORTANT: You must log out and log back in for the group changes to take effect."
echo "Alternatively, you can run 'newgrp docker' in your current terminal session."
echo "--------------------------------------------------------"

echo "7. Verifying the Docker installation with 'hello-world'..."
# This command will fail without the user being in the docker group, so we run it with sudo for initial verification.
sudo docker run hello-world
echo "Docker installation verified successfully!"

echo "Docker installation is complete."