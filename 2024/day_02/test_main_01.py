import pytest

from main_01 import count_safe_reports


@pytest.mark.parametrize(
    "reports,safe_reports",
    [
        ([[1, 2, 3]], 1),
        ([[1, 2, 7]], 0),
    ],
)
def test_count_safe_reports(reports, safe_reports):
    assert count_safe_reports(reports) == safe_reports
