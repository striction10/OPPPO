"""Tests for Song class."""
from src.models.song import Song


class TestSong:
    """Test cases for Song class."""

    def test_song_initialization(self, sample_song_data):
        """Test successful initialization of Song."""
        song = Song(**sample_song_data)

        assert song.name == "Test Song"
        assert song.time == 3.5
        assert song.musician == "Test Artist"

    def test_song_str_representation(self, sample_song_data):
        """Test string representation of Song."""
        song = Song(**sample_song_data)
        result = str(song)

        expected = "Песня: Test Song, Время: 3.5, Исполнитель: Test Artist."
        assert result == expected

    def test_song_empty_musician(self):
        """Test Song with empty musician."""
        song = Song("Test Song", 3.5, "")

        assert song.musician == ""

    def test_song_inheritance(self, sample_song_data):
        """Test that Song inherits from Parameters."""
        song = Song(**sample_song_data)

        assert isinstance(song, Song)
        assert hasattr(song, 'name')
        assert hasattr(song, 'time')
