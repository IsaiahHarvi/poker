# echo "Updating package lists and installing packages..."
# sudo apt update
# sudo apt install -y vim

echo "Installing Python Packages..."
cd ./poker
pip3 install -e .

echo "Running Git Config..."
# git lfs install # its probably unecessary to update hooks on build
gh auth login --with-token < ~/.github-token
gh auth status || echo "GitHub auth failed, did you provide a token?"
