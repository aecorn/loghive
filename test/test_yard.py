import pytest
from yard.yard import Yard
import datetime
import _hashlib

@pytest.fixture
def temp_yard():
    yard = Yard("Home1")
    yield yard
    yard.delete()

def test_yard_has_name_with_length(temp_yard):
    assert bool(temp_yard.name) and len(temp_yard.name)

def test_yard_can_be_deleted(temp_yard):
    assert temp_yard in Yard.instances
    temp_yard.delete()
    assert not temp_yard in Yard.instances