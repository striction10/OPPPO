"""Tests for Parameters class."""
from src.models.general_param import Parameters


class TestParameters:
    """Test cases for Parameters class."""

    def test_parameters_initialization(self):
        """Test successful initialization of Parameters."""
        params = Parameters("Test Name", 10.5)

        assert params.name == "Test Name"
        assert params.time == 10.5

    def test_parameters_empty_name(self):
        """Test initialization with empty name."""
        params = Parameters("", 10.5)

        assert params.name == ""
        assert params.time == 10.5

    def test_parameters_zero_time(self):
        """Test initialization with zero time."""
        params = Parameters("Test Name", 0)

        assert params.name == "Test Name"
        assert params.time == 0

    def test_parameters_negative_time(self):
        """Test initialization with negative time."""
        params = Parameters("Test Name", -5.0)

        assert params.name == "Test Name"
        assert params.time == -5.0
