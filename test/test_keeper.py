import pytest
from keeper.keeper import Keeper
import datetime
import _hashlib

@pytest.fixture
def temp_keeper():
    keeper = Keeper("Keeper1")
    yield keeper
    #keeper.delete()

def test_keeper_has_name(temp_keeper):
    assert isinstance(temp_keeper.name, str)
    assert bool(temp_keeper.name)