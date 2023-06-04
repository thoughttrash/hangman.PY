"""
Hangman Game
=============

This module implements the Hangman game. It contains the `Hangman` class
which manages the game flow, word selection, player input, and scoring.

Usage:
------
Create an instance of the `Hangman` class and call the `loadmenu()` method
to start the game.

Example:
--------
hangman = Hangman()
hangman.loadmenu()
"""


from word import Word
from inputhandler import InputHandler
from player import Player
from filehandler import Openfile


class Hangman:
    """
    The main class that represents the Hangman game.

    This class manages the gameplay, including initializing the game,
    displaying the menu, handling user input, and controlling the
    flow of the game.

    Attributes:
        word_obj (Word): An instance of the Word class to manage
                         word-related operations.
        word (str): The current word to be guessed.
        theme (str): The theme of the current word.
        player_obj (Player): An instance of the Player class to manage
                             player-related operations.
        inputhlr (InputHandler): An instance of the InputHandler class
                                 to handle user input.

    Methods:
        display(name): Displays the ASCII art corresponding to the
                       specified name.
        loadmenu(): Loads and displays the main menu, and handles
                    user commands.
        init_game(): Initializes the game by obtaining the word, theme,
                     and revealing random letters.
        play(): Starts and manages the main game loop.

    Example Usage:
        hangman = Hangman()
        hangman.loadmenu()
    """
    def __init__(self):
        """
        Initialize the Hangman game.

        This initializes the game by setting up the necessary objects
         and variables.
        It creates instances of the `Word`, `Player`, and
        `InputHandler` classes.
        """
        self.word_obj = None
        self.word = None
        self.theme = None
        self.player_obj = Player()
        self.inputhlr = InputHandler()

    def display(self, name):
        """
        Display an ASCII art based on the given name.

        Parameters:
        -----------
        name : str
            The name of the ASCII art to display.
        """
        data = Openfile('arts.json')
        art = data.data[name]
        print(art)

    def loadmenu(self):
        """
        Load the game menu and handle user commands.

        This method displays the game menu with ASCII arts, prompts the user
        for a command, and handles the command accordingly. The available
        commands are 'play', 'tips', and 'quit'.
        """
        menu = ["line", "hangman", "line", "menu"]
        for i in menu:
            self.display(i)
        command = self.inputhlr.get_input("> ").lower()
        if command == "play":
            self.inputhlr.play()
            self.play()
        elif command == "tips":
            self.inputhlr.tips()
            self.loadmenu()
        elif command == "quit":
            self.inputhlr.quit()
        else:
            self.inputhlr.invalid()
            self.loadmenu()
        self.inputhlr.clear_inputs()

    def init_game(self):
        """
        Initialize the game by obtaining the word, theme, and revealing random
        letters.

        This method creates an instance of the `Word` class, gets the word and
        theme,
        and reveals some random letters in the word based on its length.
        """
        self.word_obj = Word()
        self.word = self.word_obj.get_word()
        self.theme = self.word_obj.get_theme()
        if len(self.word) > 6:
            self.word_obj.show_random_letter()
            self.word_obj.show_random_letter()
        self.word_obj.show_random_letter()

    def play(self):
        """
        Play the Hangman game.

        This method starts the main game loop where the player guesses letters
        to reveal the hidden word.
        It checks the player's input, updates the game state, and handles
        win/lose conditions.
        """
        self.init_game()
        while self.word_obj.available_letters and self.player_obj.life != 0:
            print("\n" * 30)
            print(f"Theme: '{self.theme.title()}'")
            print(f"Score: {str(self.player_obj.score)}")
            self.display(str(self.player_obj.life))
            print(self.word_obj.get_hidden_word())
            guess = self.inputhlr.get_input("Guess a letter> ").lower()
            try:
                if guess == "menu":
                    self.loadmenu()
                    break
                guess = guess[0]
                if self.word_obj.checker(guess):
                    self.word_obj.show_letter(guess)
                    self.player_obj.life += 1
                    self.player_obj.score += 1
                else:
                    self.player_obj.life -= 1
                    self.player_obj.score -= 1
                self.inputhlr.clear_inputs()
            except IndexError:
                self.inputhlr.clear_inputs()
                print("No letter found.")
        if self.player_obj.life == 0:
            print("Game over")
            print(f"You lost {self.player_obj.score} score.")
            play_again = input("Play again? (y/n)> ").lower().strip()
            if play_again != "n":
                self.player_obj.life = 7
                self.player_obj.score = 0
                self.play()
            else:
                self.loadmenu()
        elif not self.word_obj.available_letters:
            self.player_obj.score += len(self.word_obj.get_word())
            self.player_obj.life = 7
            print(self.word_obj.get_hidden_word())
            print(f"You earned +{len(self.word_obj.get_word())} points for"
                  + f"guessing {self.word_obj.get_word().title()}!")
            continue_wait = input("Continue (y/n)> ").lower().strip()
            if continue_wait != "n":
                self.play()
            else:
                self.loadmenu()
        else:
            pass


hangman = Hangman()
hangman.loadmenu()
