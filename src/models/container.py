"""Container module."""
import json
from src.models.song import Song
from src.models.symphony import Symphony


class Container:
    """Constructor container class."""
    def __init__(self):
        self.musics = []


    def add(self, json_str: str):
        """Add a music."""
        try:
            data = json.loads(json_str)
            name = data.get("name", "").strip()
            if name == "":
                print("\nНе заполнено поле name!")
                return
            try:
                time = float(data.get("time", 0))
                if time <= 0:
                    print("\nВремя не может быть равно или меньше нуля!")
                    return
            except ValueError:
                print("\nВремя не может быть строкой!")
                return
            if data.get("composer") is not None:
                composer = data.get("composer", "").strip()
                if not composer == "":
                    self.musics.append(Symphony(name, time, composer))
                else:
                    print("\nНе заполнено поле composer!")
                    return
            elif data.get("musician") is not None:
                musician = data.get("musician", "")
                if not musician == "":
                    self.musics.append(Song(name, time, musician))
                else:
                    print("\nНе заполнено поле musician!")
                    return
        except json.JSONDecodeError:
            print("\nОшибка в формате JSON!")


    def rem(self, condition: str):
        """Remove a music from list."""
        count_musics = len(self.musics)
        condition = condition.split(" ")
        if len(condition) < 3:
            print("\nНеверный формат команды!")
            return
        field, operator, value = condition[0], condition[1], " ".join(condition[2:])
        if operator == "==":
            if field == "name":
                self.musics = [m for m in self.musics if m.name != value]
            elif field == "musician":
                self.musics = [m for m in self.musics if not hasattr(m, "musician") or \
                               m.musician != value]
            elif field == "composer":
                self.musics = [m for m in self.musics if not hasattr(m, "composer") or \
                               m.composer != value]
            elif field == "time":
                try:
                    value = float(value)
                    self.musics = [m for m in self.musics if m.time != value]
                except ValueError:
                    print("\nВремя не может быть строкой!")
        elif operator == ">":
            if field == "time":
                try:
                    value = float(value)
                    self.musics = [m for m in self.musics if m.time <= value]
                except ValueError:
                    print("\nВремя не может быть строкой!")
        else:
            print(f"\nОператор {operator} не поддерживается")
            return
        count_rem = count_musics - len(self.musics)
        print(f"\nУдалено произведений: {count_rem}")


    def print(self):
        """Print list of musics."""
        if not self.musics:
            print("\nСписок пуст!")
            return
        print("\n------------------СПИСОК ПЕСЕН------------------")
        for i, music in enumerate(self.musics, start=1):
            print(f"{i}. {music}")
