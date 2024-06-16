# Number Guessing Game

A simple number-guessing game with a graphical user interface built using `tkinter` in Python. The game generates a random number between 1 and 100, and the player tries to guess the number. Feedback is given for each guess, indicating whether it is too high, too low, or correct. The game also includes options to play again or exit the application.

## Features

- Random number generation between 1 and 100
- Graphical user interface using `tkinter`
- User feedback on guesses
- Option to play again or exit the game

## Requirements

- Python 3.x

## How to Run

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Francis-SE/CODXO.git
    cd CODXO
    ```

2. **Run the Game**:

    ```bash
    python number_guessing_game.py
    ```

## Code Overview

The main logic of the game is contained in the `NumberGuessingGame` class, which initializes the game, sets up the UI, and handles user interactions. Here is an overview of the key components:

- **initialize_game**: Sets up the initial state of the game, including generating the random number.
- **check_guess**: Handles the user's guess, providing feedback and checking if the guess is correct.
- **play_again**: Resets the game state to allow the player to play again.
- **exit_game**: Closes the application.
