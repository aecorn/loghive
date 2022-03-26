import pytest
from entries.entries import Entry
import datetime
import _hashlib


@pytest.fixture
def temp_entry():
    entry = Entry()
    yield entry
    entry.delete()


def test_entry_is_created(temp_entry):
    assert isinstance(temp_entry, Entry)
    assert bool(temp_entry)