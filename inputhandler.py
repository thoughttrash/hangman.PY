import sys

class InputHandler:
    def __init__(self):
        self.input_data = []

    def get_input(self, prompt):
        user_input = input(prompt).lower().strip()
        self.input_data.append(user_input)
        return user_input

    def get_all_inputs(self):
        return self.input_data

    def clear_inputs(self):
        self.input_data = []

    def play(self):
        print("Play")
        

    def tips(self):
        print("Score: You get +1 score everytime you get a correct letter.")
        print("Once a word is completely guessed, you get points based on the length of the word.")
        print("Game over: 7 wrong guesses.")
        print("You will remove one of the stickman's figure if you get a correct guess.")
        print("You can type 'menu' during a game to go back to the menu. ")
        print("Type 'back' to go back to the menu or just press enter")
        input("Back>")

    def quit(self):
        print("Quit")
        sys.exit()

    def invalid(self):
        print("Invalid command.")
    