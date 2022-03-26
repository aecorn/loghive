import pytest
from queen.queen import Queen
import datetime
import _hashlib

@pytest.fixture
def temp_queen():
    queen = Queen("Queen1", datetime.datetime.now())
    yield queen
    queen.delete()

@pytest.fixture
def temp_queen2(temp_queen):
    queen2 = Queen("Queen2", datetime.datetime.now(),  mother="Queen1", fathers_mother=temp_queen.id)
    yield queen2
    queen2.delete()


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
    assert isinstance(temp_queen.id, _hashlib.HASH)

def test_queen_has_mother_maybe(temp_queen, temp_queen2):
    if temp_queen2.mother:
        assert temp_queen2.mother == temp_queen.id

def test_queen_has_fathers_mother_maybe(temp_queen, temp_queen2):
    if temp_queen2.fathers_mother:
        assert temp_queen2.fathers_mother == temp_queen.id