from src.helpers import csv_processor as c


def test_filter_report_directories_by_date():
    dirs = ['04252022', '09092022', '09162022']
    expected_results = ['09092022', '09162022']
    result = c.filter_report_directories_by_date('09092022', '09162022', dirs)
    assert result == expected_results


def test_filter_report_directories_by_date_fails():
    dirs = ['04252022', '09092022', '09162022']
    expected_results = ['04252022']
    result = c.filter_report_directories_by_date('09092022', '09162022', dirs)
    assert result != expected_results
