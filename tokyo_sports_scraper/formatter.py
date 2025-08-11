from dateutil import parser

def format_race_date(race_date: str) -> str:
    """
    日付を整える。

    Parameters:
    - race_date: 日付（str）

    Returns:
    - 日付（str）
    """
    return parser.parse(race_date).strftime('%Y%m%d')
