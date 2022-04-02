import pytest
from core.calendar import Calendar
import datetime
import _hashlib

@pytest.fixture
def temp_calendar():
    calendar = Calendar()
    yield calendar
    calendar.delete()

def test_calendar_is_created(temp_calendar):
    assert isinstance(temp_calendar, Calendar)
    assert bool(temp_calendar)
