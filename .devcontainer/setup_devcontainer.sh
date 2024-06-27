# echo "Updating package lists and installing packages..."
# sudo apt update
# sudo apt install -y vim

echo "Installing Python Packages..."
cd ./poker
pip3 install -e .

echo "Running Git Config..."
if [ -f ~/.github-token ]; then
  echo "GitHub token found, proceeding with authentication..."
  gh auth login --with-token < ~/.github-token
  gh auth status || echo "GitHub auth failed, check your permissions."
else
  echo "No GitHub token found, skipping authentication..."
fi