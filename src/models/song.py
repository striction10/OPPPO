"""Module for songs."""
from src.models.general_param import Parameters


class Song(Parameters):
    """Constructor for Song class."""

    def __init__(self, name: str, time: float, musician: str):
        super().__init__(name, time)
        self.musician = musician


    def __str__(self):
        """Print Song info."""
        return f"Песня: {self.name}, Время: {self.time}, Исполнитель: {self.musician}."
