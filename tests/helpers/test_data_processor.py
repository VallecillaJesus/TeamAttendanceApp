from src.helpers import data_processor as d
from datetime import datetime


def test_get_datetime():
    current_datetime = datetime.now()
    result = d.get_datetime()

    date = str(current_datetime.date()).replace('-', '')
    time = str(current_datetime.time()).replace(':', '')[:5]
    expected_datetime = date + time

    assert expected_datetime == result
