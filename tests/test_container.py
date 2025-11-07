"""Tests for Container class."""
import json
from src.models.container import Container


class TestContainer:
    """Test cases for Container class."""

    def test_add_song_and_symphony_success(self):
        """Test successful addition of both Song and Symphony."""
        container = Container()

        # Тестовые данные
        song_data = {
            "name": "Test Song",
            "time": 3.5,
            "musician": "Test Artist"
        }

        symphony_data = {
            "name": "Test Symphony",
            "time": 25.0,
            "composer": "Test Composer"
        }

        song_json = json.dumps(song_data)
        result_song = container.add(song_json)

        assert result_song is True
        assert len(container.musics) == 1
        assert container.musics[0].name == "Test Song"
        assert container.musics[0].musician == "Test Artist"

        symphony_json = json.dumps(symphony_data)
        result_symphony = container.add(symphony_json)

        assert result_symphony is True
        assert len(container.musics) == 2
        assert container.musics[1].name == "Test Symphony"
        assert container.musics[1].composer == "Test Composer"

    def test_rem_by_condition_success(self):
        """Test removal by different conditions."""
        container = Container()

        test_items = [
            {"name": "Song1", "time": 3.0, "musician": "Artist1"},
            {"name": "Song2", "time": 4.0, "musician": "Artist2"},
            {"name": "Symphony1", "time": 20.0, "composer": "Composer1"}
        ]

        for item in test_items:
            container.add(json.dumps(item))

        assert len(container.musics) == 3

        removed_count = container.rem("name == Song1")
        assert removed_count == 1
        assert len(container.musics) == 2
        assert all(music.name != "Song1" for music in container.musics)

        removed_count = container.rem("time > 10.0")
        assert removed_count == 1
        assert len(container.musics) == 1
        assert all(music.time <= 10.0 for music in container.musics)

        removed_count = container.rem("musician == Artist2")
        assert removed_count == 1
        assert len(container.musics) == 0
