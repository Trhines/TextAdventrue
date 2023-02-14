# TextAdventrue
This a short game based on a very dumb riddle that makes no sense. This project is very over built as a way to practice OOP within python.

Run python adventure.py to start the game, select a save slot and create a character. No data is actaully saved and will be wiped when the program is exited.

The answers to each stage are
    "look into the mirror"
    "take the saw"
    "cut the table"
    "put the halves together"
    "climb into the hole"

    -at any point during the game you may type exit to return to the main menu

The design works as follows:
    -The game manager class handles all macro elements and game data (main menus/save slots).

    -All actions within the game accure within the player class and are unique for each instance of said class.

    -All prompts are created through the UI element class displayed through UI handler class.

    -Each UI element has a prompt and a validator (an argument to determine wether or not the player input is valid). If the prompt requires a specific input (such as y/n or a number 1-4) adapting the prompt to reflect the required input is done by the UI handler. Handling of valid responses should be done within either the player or game manager classes.

    -Even though the game is short and linear, there is no fixed game state. All possible interactions are dictated throught the inventory and environment(instances of the collection class) and the items they contain.