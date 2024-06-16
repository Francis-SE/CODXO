"""
Simple number-guessing game with a graphical user interface built using 
'tkinter'. The game generates a random number between 1 and 100, and the 
player tries to guess the number. Feedback is given for each guess, 
indicating whether the guess is lower or higher than the number or correct.
The game also includes options to play again or exit the application.
"""

import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    """
    Creates a GUI for a number guessing game where the user has to guess a
    randomly generated number between 1 and 100.
    """

    # Initializes a game GUI with labels, entry fields, and buttons
    def __init__(self, app):
        self.app = app
        self.app.title("Number Guessing Game")

        self.initialize_game()
        
        self.label = tk.Label(app,
                              text = "Think of a number between 1 and 100.",
                              font = ("Helvetica", 14))
        self.label.grid(row = 0, column = 0, columnspan = 2, pady = 10)

        self.guess_label = tk.Label(app,
                                    text = "Enter your guess:",
                                    font = ("Helvetica", 14))
        self.guess_label.grid(row = 1, column = 0, pady = 5, padx = 5,
                              sticky="e")

        self.guess_entry = tk.Entry(app, font = ("Helvetica", 14))
        self.guess_entry.grid(row = 1, column = 1, pady = 5, padx = 5,
                              sticky="w")

        self.guess_button = tk.Button(app,
                                      text = "Guess", font = ("Helvetica", 14),
                                      command = self.check_guess)
        self.guess_button.grid(row = 2, column = 0, columnspan = 2, pady = 5)

        self.result_label = tk.Label(app, text = "", font = ("Helvetica", 14))
        self.result_label.grid(row = 3, column = 0, columnspan = 2, pady = 10)

        self.play_again_button = tk.Button(app,
                                           text = "Play Again",
                                           font = ("Helvetica", 14),
                                           command = self.play_again)
        self.play_again_button.grid(row = 4, column = 0, pady = 20, padx = 20,
                                    sticky="e")

        self.exit_button = tk.Button(app,
                                     text = "Exit", font = ("Helvetica", 14),
                                     command = self.exit_game)
        self.exit_button.grid(row = 4, column = 1, pady = 20, padx = 20,
                              sticky = "w")

    # Sets up a game by generating a random number to guess
    def initialize_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.number_of_guesses = 0

    # Checks user's input against the randonly generated number to be guessed
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.number_of_guesses += 1

            if guess < self.number_to_guess:
                self.result_label.config(text = "Make it Higher")
            elif guess > self.number_to_guess:
                self.result_label.config(text = "Make it Lower")
            else:
                self.result_label.config(text = f"Congratulations!"
                                                f" You guessed the number.")
                self.guess_button.config(state = tk.DISABLED)
                messagebox.showinfo("Congratulations",
                                    f"It took you {self.number_of_guesses} "
                                    f"attempts to guess this number.")
        # Handle non-integer input
        except ValueError:
            messagebox.showerror("Invalid input",
                                 "Please enter a valid number.")
    # Resets the game 
    def play_again(self):
        self.initialize_game()
        self.result_label.config(text = "")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

    # Exits the game
    def exit_game(self):
        self.app.destroy()
                

if __name__ == "__main__":
    # Create the main window
    app = tk.Tk()
    game = NumberGuessingGame(app)
    app.mainloop()
