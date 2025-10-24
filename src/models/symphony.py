from src.models.general_param import Parameters

class Symphony(Parameters):
    def __init__(self, name: str, time: float, composer: str):
        super().__init__(name, time)
        self.composer = composer

    def __str__(self):
        return f"Симфония: {self.name}, Время: {self.time}, Композитор: {self.composer}."