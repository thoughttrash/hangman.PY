"""
player.py
=========

This module defines the Player class for managing player data such as life
and score.

Classes:
    - Player: Represents a player with life and score attributes.

Example usage:
    ```
    # Create a player instance
    player = Player()

    # Get the player's current life
    life = player.life

    # Set the player's life to a new value
    player.life = 5

    # Get the player's current score
    score = player.score

    # Set the player's score to a new value
    player.score = 100
    ```

"""


class Player:
    """Represents a player with life and score attributes."""

    def __init__(self):
        self._life = 7
        self._score = 0

    @property
    def life(self):
        """Get the player's current life."""
        return self._life

    @life.setter
    def life(self, value):
        """Set the player's life to a new value."""
        if value < 0:
            self._life = 0
        elif value > 7:
            self._life = 7
        else:
            self._life = value

    @property
    def score(self):
        """Get the player's current score."""
        return self._score

    @score.setter
    def score(self, value):
        """Set the player's score to a new value."""
        if value < 0:
            self._score = 0
        else:
            self._score = value
