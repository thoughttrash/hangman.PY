import random
from app import Openfile

class Word:
    def __init__(self):
        self.data = Openfile("words.json")
        self.themes = self.data.data['themes'][0]
        # Default value is random for theme and word
        self.theme = random.choice(list(self.themes.keys()))
        self.word = random.choice(self.data.data['themes'][0][self.theme])
        self.revealed_letters = []
        self.secret_word = ""
        self.hidden_letters = []
        self.available_letters = []
        self.randletter = ""

    # Generates a random word from a specified theme
    def Word_from(self, theme):
        self.theme = theme
        self.word = random.choice(self.data.data['themes'][0][self.theme])
        return self.word

    def randomize(self):
        self.theme = random.choice(list(self.themes.keys()))
        self.word = random.choice(self.data.data['themes'][0][self.theme])
        return self.theme, self.word

    def get_word(self):
        return self.word

    def get_theme(self):
        return self.theme

    def get_hidden_word(self):
        self.hidden_letters = [letter if letter in self.revealed_letters else "_" for letter in self.word]
        self.secret_word = " ".join(self.hidden_letters).upper()
        return self.secret_word

    def show_random_letter(self):
        self.available_letters = [letter for letter in self.word if letter not in self.revealed_letters]
        self.randletter = random.choice(self.available_letters)
        self.revealed_letters.append(self.randletter)
        return self.randletter
    
    def show_letter(self, lucky_letter):
        self.available_letters = [letter for letter in self.word if letter not in self.revealed_letters]
        if lucky_letter not in self.revealed_letters:
            self.revealed_letters.append(lucky_letter)
            self.available_letters.remove(lucky_letter)
        else:
            return None
    
    def checker(self, lucky_letter):
        return lucky_letter in self.available_letters