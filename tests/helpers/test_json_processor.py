from src.helpers import json_processor as j


def test_get_duration():
    assert '1h 0m' == j.get_duration('5:00:00 AM', '6:00:00 AM')


def test_get_duration_fails():
    assert '-1h 0m' != j.get_duration('5:00:00 AM', '6:00:00 AM')
