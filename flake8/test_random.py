import random
from unittest.mock import patch


def roll():
    return random.randint(1, 100)


def test_roll_one():
    with patch("test_random.random.randint", return_value=5):
        assert roll() == 5


@patch("test_random.random.randint")
def test_roll_two(mock):
    mock.return_value = 100
    assert roll() == 100
