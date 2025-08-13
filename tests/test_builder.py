import pytest
import tokyo_sports_scraper.formatter as formatter
from tokyo_sports_scraper.builder import build_race_url
from unittest.mock import patch

@pytest.mark.parametrize(
    'race_date, race_circuit_number, race_number, expected',
    [
        ('2025-08-01', 3, 5, 'https://autorace.tokyo-sports.co.jp/list/race/20250801035'),
        ('2025-08-02', 5, 10, 'https://autorace.tokyo-sports.co.jp/list/race/202508020510'),
    ]
)
def test_build_race_url(race_date, race_circuit_number, race_number, expected):
    with patch.object(formatter, 'format_race_date', return_value=race_date.replace('-', '')):
        assert build_race_url(race_date, race_circuit_number, race_number) == expected
