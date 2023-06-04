"""
word.py
=======

This module defines the Word class for managing word-related functionalities
in a game.

Classes:
    - Word: Represents a word and provides methods for word-related operations.

Example usage:
    ```
    # Create an instance of Word
    word = Word()

    # Get the current word
    current_word = word.get_word()

    # Get the current theme
    current_theme = word.get_theme()

    # Get the hidden word with revealed letters
    hidden_word = word.get_hidden_word()

    # Show a random letter from the word
    random_letter = word.show_random_letter()

    # Show a specific letter in the word
    word.show_letter('a')

    # Check if a letter is available in the word
    is_available = word.checker('b')
    ```

"""

import random
from filehandler import Openfile


class Word:
    """Represents a word and provides methods for word-related operations."""

    def __init__(self):
        self.data = Openfile("words.json")
        self.themes = self.data.data['themes'][0]
        self.theme = random.choice(list(self.themes.keys()))
        self.word = random.choice(self.data.data['themes'][0][self.theme])
        self.revealed_letters = []
        self.secret_word = ""
        self.hidden_letters = []
        self.available_letters = []
        self.randletter = ""

    def word_from(self, theme):
        """Set the word from a specific theme and return the selected word.

        Args:
            theme (str): The theme from which to select the word.

        Returns:
            str: The selected word from the specified theme.
        """
        self.theme = theme
        self.word = random.choice(self.data.data['themes'][0][self.theme])
        return self.word

    def get_word(self):
        """Get the current word.

        Returns:
            str: The current word.
        """
        return self.word

    def get_theme(self):
        """Get the current theme.

        Returns:
            str: The current theme.
        """
        return self.theme

    def get_hidden_word(self):
        """Get the hidden word with revealed letters.

        Returns:
            str: The hidden word with underscore '_' representing
                 unrevealed letters.
        """
        self.hidden_letters = [letter if letter in self.revealed_letters
                               else "_" for letter in self.word]
        self.secret_word = " ".join(self.hidden_letters).upper()
        return self.secret_word

    def show_random_letter(self):
        """Show a random letter from the word that has not been revealed.

        Returns:
            str: The randomly selected letter.
        """
        self.available_letters = [letter for letter in self.word if letter
                                  not in self.revealed_letters]
        self.randletter = random.choice(self.available_letters)
        self.revealed_letters.append(self.randletter)
        return self.randletter

    def show_letter(self, lucky_letter):
        """Reveal a specific letter in the word.

        Args:
            lucky_letter (str): The letter to be revealed in the word.
        """
        self.available_letters = [letter for letter in self.word if letter
                                  not in self.revealed_letters]
        if lucky_letter not in self.revealed_letters:
            self.revealed_letters.append(lucky_letter)
            self.available_letters.remove(lucky_letter)
            return

    def checker(self, lucky_letter):
        """Check if a letter is available in the word.

        Args:
            lucky_letter (str): The letter to be checked.

        Returns:
            bool: True if the letter is available in the word, False otherwise.
        """
        return lucky_letter in self.available_letters
