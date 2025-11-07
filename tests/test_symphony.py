"""Tests for Symphony class."""
from src.models.symphony import Symphony


class TestSymphony:
    """Test cases for Symphony class."""

    def test_symphony_initialization(self, sample_symphony_data):
        """Test successful initialization of Symphony."""
        symphony = Symphony(**sample_symphony_data)

        assert symphony.name == "Test Symphony"
        assert symphony.time == 25.0
        assert symphony.composer == "Test Composer"

    def test_symphony_str_representation(self, sample_symphony_data):
        """Test string representation of Symphony."""
        symphony = Symphony(**sample_symphony_data)
        result = str(symphony)

        expected = "Симфония: Test Symphony, Время: 25.0, Композитор: Test Composer."
        assert result == expected

    def test_symphony_empty_composer(self):
        """Test Symphony with empty composer."""
        symphony = Symphony("Test Symphony", 25.0, "")

        assert symphony.composer == ""

    def test_symphony_inheritance(self, sample_symphony_data):
        """Test that Symphony inherits from Parameters."""
        symphony = Symphony(**sample_symphony_data)

        assert isinstance(symphony, Symphony)
        assert hasattr(symphony, 'name')
        assert hasattr(symphony, 'time')
