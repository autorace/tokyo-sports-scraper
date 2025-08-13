import pytest
from tokyo_sports_scraper.formatter import format_race_date

@pytest.mark.parametrize(
    'race_date, expected',
    [
        ('20250801', '20250801'),
        ('2025-08-02', '20250802'),
        ('2025/08/03', '20250803'),
    ]
)
def test_format_race_date(race_date, expected):
    assert format_race_date(race_date) == expected
