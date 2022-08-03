import pytest
from core.hive import Hive
from core.yard import Yard

@pytest.fixture
def temp_yard():
    temp_yard = Yard("Home1")
    yield temp_yard
    temp_yard.delete()

@pytest.fixture
def temp_hive(temp_yard):
    temp_hive = Hive("A1", 7, temp_yard)
    yield temp_hive
    temp_hive.delete()

@pytest.fixture
def temp_hive2():
    temp_hive2 = Hive("B2", 8)
    yield temp_hive2
    temp_hive2.delete()


def test_hive_has_id(temp_hive):
    assert bool(temp_hive.id)
    assert isinstance(temp_hive.id, str)

def test_hive_has_strength(temp_hive):
    assert bool(temp_hive.strength)
    assert isinstance(temp_hive.strength, int)

def test_hive_layer_num(temp_hive):
    assert temp_hive.layers == 1

def test_hive_layer_increase(temp_hive):
    temp_hive.layer_increase()
    assert temp_hive.layers > 1

def test_hive_is_in_a_yard(temp_hive):
    assert isinstance(temp_hive.yard, Yard)

def test_hive2_is_not_in_a_yard(temp_hive2):
    assert not temp_hive2.yard