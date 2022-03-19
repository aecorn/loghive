import pytest
from queen.queen import Queen
import datetime

@pytest.fixture
def temp_queen():
    return Queen("Queen1", datetime.datetime.now())


def test_queen_has_name(temp_queen):
    assert bool(temp_queen.name)
    assert isinstance(temp_queen.name, str)

def test_queen_has_birthmonth(temp_queen):
    assert bool(temp_queen.birthmonth)
    assert isinstance(temp_queen.birthmonth, datetime.datetime)

def test_queen_has_color(temp_queen):
    assert bool(temp_queen.color)
    assert isinstance(temp_queen.color, str)
    assert temp_queen.color in ['white', 'yellow', 'red', 'blue', 'green']

def test_queen_has_registertime(temp_queen):
    assert bool(temp_queen.birthmonth)
    assert isinstance(temp_queen.birthmonth, datetime.datetime)

def test_queen_has_id(temp_queen):
    assert bool(temp_queen.id)
    assert isinstance(temp_queen.id, str)

def test_queen_has_mother_maybe(temp_queen):
    if temp_queen.mother:
        assert isinstance(temp_queen.mother, str)
        # Check if queen is actually registered?