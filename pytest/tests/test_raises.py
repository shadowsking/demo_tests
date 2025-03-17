import pytest


def div(a, b):
    return a / b


def test_raise():
    with pytest.raises(ZeroDivisionError) as ex:
        div(2, 0)

    assert str(ex.value) == "div by 0"
