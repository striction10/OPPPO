from src.models.general_param import Parameters

class Song(Parameters):
    def __init__(self, name: str, time: float, musician: str):
        super().__init__(name, time)
        self.musician = musician

    def __str__(self):
        return f"Песня: {self.name}, Время: {self.time}, Исполнитель: {self.musician}."