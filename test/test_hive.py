import pytest
from hive.hive import Hive

@pytest.fixture
def temp_hive():
    return Hive("A1", 7)

def test_hive_has_id(temp_hive):
    assert bool(temp_hive.id)
    assert isinstance(temp_hive.id, str)

def test_hive_has_strength(temp_hive):
    assert bool(temp_hive.strength)
    assert isinstance(temp_hive.strength, int)