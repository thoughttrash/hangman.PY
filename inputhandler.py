"""
input_handler.py
================

This module defines the InputHandler class for handling user input and
providing game-related functionalities.

Classes:
    - InputHandler: Handles user input and provides game-related
                    functionalities.

Example usage:
    ```
    # Create an instance of InputHandler
    handler = InputHandler()

    # Get user input with a prompt
    user_input = handler.get_input("Enter your guess: ")

    # Get all recorded inputs
    all_inputs = handler.get_all_inputs()

    # Clear the recorded inputs
    handler.clear_inputs()

    # Play the game
    handler.play()

    # Show game tips
    handler.tips()

    # Quit the game
    handler.quit()

    # Handle an invalid command
    handler.invalid()
    ```

"""

import sys


class InputHandler:
    """Handles user input and provides game-related functionalities."""

    def __init__(self):
        self.input_data = []

    def get_input(self, prompt):
        """Get user input with a prompt and record the input."""
        user_input = input(prompt).lower().strip()
        self.input_data.append(user_input)
        return user_input

    def get_all_inputs(self):
        """Get all recorded inputs."""
        return self.input_data

    def clear_inputs(self):
        """Clear the recorded inputs."""
        self.input_data = []

    def play(self):
        """Play the game."""
        print("Play")

    def tips(self):
        """Display game tips and instructions."""
        instructions = [
            "Score: You get +1 score every time you get a correct letter.",
            "Once a word is completely guessed, you get points based on"
            + "the length of the word.",
            "Game over: 7 wrong guesses.",
            "You will remove one of the stickman's figure if you get" +
            "a correct guess.",
            "You can type 'menu' during a game to go back to the menu.",
            "Type 'back' to go back to the menu or just press enter."
        ]

        for instruction in instructions:
            print(instruction)

        input("Back> ")

    def quit(self):
        """Quit the game.

        Note:
            This method relies on the `sys` module being imported for
            `sys.exit` to work properly.
        """
        print("Quit")
        sys.exit()

    def invalid(self):
        """Handle an invalid command."""
        print("Invalid command.")
