import json

class Openfile:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename,'r') as file:
            self.data = json.load(file)
