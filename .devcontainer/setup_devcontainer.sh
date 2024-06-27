#!/bin/bash

# echo "Updating package lists and installing packages..."
# sudo apt update
# sudo apt install -y vim

echo "Installing Python Packages..."
cd ./poker
pip3 install -e .

# ./.devcontainer/setup_git.sh
if [ -f ~/.github-token ]; then
  echo "GitHub token found, proceeding with authentication..."
  ./setup_git.sh
else
  echo "No GitHub token found, skipping authentication..."
fi
