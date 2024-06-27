# Poker AI Integration Project
** WIP **

This repository is structured to facilitate the development and testing of poker AIs. Below is the directory structure and a brief description of each file.

## Directory Structure

```
poker/
├── .devcontainer
├── setup.py
├── requirements.in
├── requirements.txt
├── pytest.ini
├── src/
│   └── poker/
│       ├── __init__.py
│       ├── deck.py
│       ├── game.py
│       ├── main.py
│       ├── player.py
│       └── teams/
│           ├── example/
│           │   └── ai.py
│           ├── test1/
│           │   └── ai.py
│           └── test2/
│               └── ai.py
└── tests/
    ├── test_deck.py
    ├── test_game.py
```

## Getting Started

NOTE: There is a provided devcontainer (for use in the vscode extension) that will handle all of the inital setup. A github token (.github-token) can be placed in .devcontainer directory before building the container to provide git functionality. The only further action after building is to cd to poker/poker/.

1. **Clone the Repository:**
   - Clone this repository to your local machine using `git clone <repo-url>`.

2. **Set Up the Project as a Pip Package:**
   - Ensure you are running Python v3.11.9
   - Navigate to the poker/poker/ dir of the project (where `setup.py` is located).
   - Run `pip install -e .` to install the project in editable mode. This allows you to make changes to the code and have them immediately reflected without needing to reinstall the package.

4. **Integrate Your AI:**
   - Navigate to the `teams` directory.
   - Create a new folder for your team and add your `ai.py` script that defines your AI's logic.
      - Team directory names cannot contain spaces
   - Ensure your AI script follows the interface used in the `example/ai.py`.
   - Additional files are no problem as long as the return format is the same.
   - You are limited to the packages that are listed in the requirements.txt file.

5. **Setting the PYTHONPATH Environment Variable:**
   - To ensure Python can find the `poker` package, set the `PYTHONPATH` environment variable to include the `src` directory.

   #### For Windows PowerShell:
   ```powershell
   $env:PYTHONPATH="$pwd/src"
   ```

   #### For Windows Command Prompt:
   ```cmd
   set PYTHONPATH=%cd%\src
   ```

   #### For Bash (Linux/macOS):
   ```sh
   export PYTHONPATH=$(pwd)/src
   ```

6. **Running the Games:**
   - Ensure your cwd is poker/poker
   - After setting the `PYTHONPATH`, run the game by executing:
     ```sh
     python src/poker/main.py
     ```

## Running Tests

To run the tests, simply execute the following command in the poker/poker directory:

```sh
pytest
```

This will execute all test cases defined in the `tests` directory and ensure everything is working as expected.
