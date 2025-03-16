import pytest


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


@pytest.mark.parametrize(
    "a, b, excepted",
    [
        (1, 2, 3),
        (2, 3, 5),
    ]
)
def test_add(a, b, excepted):
    assert add(a, b) == excepted


@pytest.mark.parametrize(
    "a, b, excepted",
    [
        (1, 2, 2),
        (2, 3, 6),
    ]
)
def test_mul(a, b, excepted):
    assert mul(a, b) == excepted
