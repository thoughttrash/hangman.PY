"""
filehandler.py
===========

This module provides a class for opening and loading JSON data from a file
using the `json` module.

Classes:
    - Openfile: A class for opening and loading JSON data.

Example usage:
    ```
    # Create an instance of Openfile and load JSON data
    file = Openfile("data.json")

    # Retrieve the loaded JSON data
    data = file.get_data()

    # Perform some processing on the data
    processed_data = file.process_data()
    ```

Note:
    - This module requires the `json` module.

"""
import json


class Openfile:
    """A class for opening and loading JSON data from a file."""

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def get_data(self):
        """Returns the loaded JSON data."""
        return self.data

    def process_data(self):
        """Performs some processing on the loaded data."""
        # Add your processing logic here
        processed_data = self.data  # Placeholder example
        return processed_data
