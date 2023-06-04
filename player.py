class Player:
    def __init__(self):
        self._life = 7
        self._score = 0

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        if value < 0:
            self._life = 0
        elif value > 7:
            self._life = 7
        else:
            self._life = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0:
            self._score = 0
        else:
            self._score = value
