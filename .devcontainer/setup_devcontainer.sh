#!/bin/bash

echo "Installing Python Packages..."
cd ./poker
pip3 install -e .

# ./.devcontainer/setup_git.sh
if [ -f /workspaces/poker/.devcontainer/.github-token ]; then
  echo "GitHub token found, proceeding with authentication..."
  gh auth login --with-token < /workspaces/poker/.devcontainer/.github-token
  gh auth status || echo "GitHub auth failed, check your permissions."
else
  echo "No GitHub token found, skipping authentication..."
fi
