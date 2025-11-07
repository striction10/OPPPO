"""Module for general parameters."""
class Parameters:
    """Class for parameters."""

    def __init__(self, name: str, time: float):
        self.name = name
        self.time = time

    def get_name(self) -> str:
        """Get the name parameter."""
        return self.name

    def get_time(self) -> float:
        """Get the time parameter."""
        return self.time

    def __str__(self) -> str:
        """String representation of parameters."""
        return f"Name: {self.name}, Time: {self.time}"
