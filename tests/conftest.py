"""Test configuration and fixtures."""
import pytest
from src.models.song import Song
from src.models.symphony import Symphony


@pytest.fixture
def sample_song_data():
    return {
        "name": "Test Song",
        "time": 3.5,
        "musician": "Test Artist"
    }


@pytest.fixture
def sample_symphony_data():
    return {
        "name": "Test Symphony",
        "time": 25.0,
        "composer": "Test Composer"
    }


@pytest.fixture
def sample_song():
    return Song("Test Song", 3.5, "Test Artist")


@pytest.fixture
def sample_symphony():
    return Symphony("Test Symphony", 25.0, "Test Composer")


@pytest.fixture
def container_with_data(sample_song, sample_symphony):
    from src.models.container import Container
    container = Container()
    container.musics = [sample_song, sample_symphony]
    return container

@pytest.fixture
def empty_container():
    from src.models.container import Container
    return Container()
