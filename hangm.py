from word import Word
from inputhandler import InputHandler
import player
from app import Openfile
import time
import re

class Hangman:
    def __init__(self):
        word_obj.randomize()
        
    # Function display the ascii arts from arts.json
    def display(self, name):
        data = Openfile('arts.json')
        art = data.data[(name)]
        return print(art)


    # Loads the menu texts and arts
    def loadmenu(self):
        menu = ["line", "hangman", "line", "menu"]
        for i in menu:
            hangman.display(i)
        command = inputhlr.get_input("> ").lower()
        if command == "play":
            inputhlr.play()
            hangman.play()
        elif command == "tips":
            inputhlr.tips()
            hangman.loadmenu()
        elif command == "quit":
            inputhlr.quit()    
        else:
            inputhlr.invalid()
            hangman.loadmenu()
        inputhlr.clear_inputs()
        

    # Main game loop
    def play(self):
        word_obj = Word()
        word = word_obj.get_word()
        theme = word_obj.get_theme()
        if len(word) > 6:
            word_obj.show_random_letter()
            word_obj.show_random_letter()
        word_obj.show_random_letter()
        secret_word = word_obj.get_hidden_word()
        while word_obj.available_letters and player_obj.life != 0:
            print("\n"*30)
            # Print the game information, theme, score, and the hangman arts
            print(f"Theme: '{theme.title()}'")
            print(f"Score: {str(player_obj.score)}")
            hangman.display(str(player_obj.life))
            print(word_obj.get_hidden_word())
            guess = inputhlr.get_input("Guess a letter> ").lower()
            try:
                if guess == "menu":
                    hangman.loadmenu()
                    break
                guess = guess[0]
                # If guess is correct
                if word_obj.checker(guess):
                    # show the correct letter
                    word_obj.show_letter(guess)
                    player_obj.life += 1
                    player_obj.score += 1
                else:
                    player_obj.life -= 1
                    player_obj.score -= 1
                inputhlr.clear_inputs()
            except IndexError:
                inputhlr.clear_inputs()
                print("No letter found.")
        if player_obj.life == 0:
            print("Game over")
            print(f"You lost {player_obj.score} score.")
            play_again = input("Play again? (y/n)> ").lower().strip()
            if play_again != "n":
                player_obj.life = 7
                player_obj.score = 0
                hangman.play()
            else:
                hangman.loadmenu()
            command = inputhlr.get_input("> ").lower()
        elif not word_obj.available_letters:
            player_obj.score += len(word_obj.get_word())
            player_obj.life = 7
            print(word_obj.get_hidden_word()) 
            print(f"You earned +{len(word_obj.get_word())} points for guessing {word_obj.get_word().title()}!")
            continue_wait = input("Continue(y/n)> ").lower().strip()
            if continue_wait != "n":
                hangman.play()
            else:
                hangman.loadmenu()
        else:
            pass

player_obj = player.Player()
word_obj = Word()
hangman = Hangman()
inputhlr = InputHandler()


word = word_obj.get_word()
theme = word_obj.get_theme()
if len(word) > 6:
    word_obj.show_random_letter()
    word_obj.show_random_letter()
word_obj.show_random_letter()
secret_word = word_obj.get_hidden_word()

hangman.loadmenu()
