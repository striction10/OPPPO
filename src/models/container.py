"""Container module."""
import json
from typing import List, Union
from src.models.song import Song
from src.models.symphony import Symphony


class MusicFactory:
    """Factory for creating music objects."""

    @staticmethod
    def create_music(data: dict) -> Union[Song, Symphony]:
        """Create music object from data."""
        name = data.get("name", "").strip()
        if not name:
            raise ValueError("Имя не может быть пустым!")

        try:
            time = float(data.get("time", 0))
        except (TypeError, ValueError):
            raise ValueError("Время принимает только числовое значение!")

        if time <= 0:
            raise ValueError("Время должно иметь положительное значение!")

        if "composer" in data:
            composer = data.get("composer", "").strip()
            if not composer:
                raise ValueError("Композитор не может быть пустым!")
            return Symphony(name, time, composer)
        elif "musician" in data:
            musician = data.get("musician", "").strip()
            if not musician:
                raise ValueError("Исполнитель не может быть пустым!")
            return Song(name, time, musician)
        else:
            raise ValueError("Неизвестное поле!")


class ConditionParser:
    """Parser for removal conditions."""

    @staticmethod
    def parse(condition: str) -> tuple:
        """Parse condition string."""
        parts = condition.strip().split(" ", 2)
        if len(parts) < 3:
            raise ValueError("Неверный формат условия!")

        field, operator, value = parts
        return field, operator, value

    @staticmethod
    def create_filter(field: str, operator: str, value: str):
        """Create filter function based on condition."""
        if operator == "==":
            return ConditionParser._create_equals_filter(field, value)
        elif operator == ">":
            return ConditionParser._create_greater_than_filter(field, value)
        else:
            raise ValueError(f"Неизвестный оператор: {operator}")

    @staticmethod
    def _create_equals_filter(field: str, value: str):
        """Create equals filter."""
        field_filters = {
            "name": lambda music: music.name == value,
            "musician": lambda music: hasattr(music, "musician") and music.musician == value,
            "composer": lambda music: hasattr(music, "composer") and music.composer == value,
            "time": lambda music: music.time == ConditionParser._parse_time_value(value)
        }

        if field not in field_filters:
            raise ValueError(f"Неизвестное поле: {field}")

        return field_filters[field]

    @staticmethod
    def _create_greater_than_filter(field: str, value: str):
        """Create greater than filter."""
        if field != "time":
            raise ValueError(f"Оператор > поддерживается только с временем!")

        time_value = ConditionParser._parse_time_value(value)
        return lambda music: music.time > time_value

    @staticmethod
    def _parse_time_value(value: str) -> float:
        """Parse time value from string."""
        try:
            return float(value)
        except ValueError:
            raise ValueError("Время должно быть числом!")


class Container:
    """Container for music items."""

    def __init__(self):
        self.musics: List[Union[Song, Symphony]] = []
        self.factory = MusicFactory()

    def add(self, json_str: str) -> bool:
        """Add a music item from JSON string."""
        try:
            data = json.loads(json_str)
            music_item = self.factory.create_music(data)
            self.musics.append(music_item)
            return True
        except (json.JSONDecodeError, ValueError) as e:
            print(f"\nОшибка при добавлении: {e}")
            return False

    def rem(self, condition: str) -> int:
        """Remove music items by condition."""
        try:
            initial_count = len(self.musics)
            field, operator, value = ConditionParser.parse(condition)
            filter_func = ConditionParser.create_filter(field, operator, value)

            self.musics = [music for music in self.musics if not filter_func(music)]

            return initial_count - len(self.musics)
        except ValueError as e:
            print(f"\nОшибка в условии: {e}")
            return 0

    def print(self):
        """Print list of musics."""
        if not self.musics:
            print("\nСписок пуст!")
            return
        print("\n------------------СПИСОК ПЕСЕН------------------")
        for i, music in enumerate(self.musics, start=1):
            print(f"{i}. {music}")
