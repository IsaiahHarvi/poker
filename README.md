
# Poker AI Integration Project
** WIP **

This repository is structured to facilitate the development and testing of poker AIs. Below is the directory structure and a brief description of each file.

## Directory Structure

```
└── 📁poker
    └── deck.py    # Handles deck operations
    └── game.py    # Core game logic and driver
    └── main.py    # Runs the game engine
    └── player.py
    └── 📁teams    # Contains directories containing AI of each team
        └── 📁example # Example directory for integration guidance
            └── ai.py 
```


## Getting Started

1. **Clone the Repository:**
   - Clone this repository to your local machine using `git clone <repo-url>`.
2. **Install Requirements:**
   - Ensure you have Python installed and then run `pip install -r requirements.txt` to install the necessary packages.
3. **Integrate Your AI:**
   - Navigate to the `teams` directory.
   - Create a new folder for your team and add your `ai.py` script that defines your AI's logic.
   - Ensure your AI script follows the interface used in the `example/ai.py`.
   - Additional files are no problem as long as the return format is the same, any additional packages should be accompanied by a requirements.txt in your directory.
4. **Running the Games:**
   - Run `python main.py` from the root of the `poker` directory
