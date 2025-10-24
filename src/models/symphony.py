"""Module for Symphony."""
from src.models.general_param import Parameters


class Symphony(Parameters):
    """Constructor for Symphony class."""
    def __init__(self, name: str, time: float, composer: str):
        super().__init__(name, time)
        self.composer = composer


    def __str__(self):
        """Print Symphony info."""
        return f"Симфония: {self.name}, Время: {self.time}, Композитор: {self.composer}."
