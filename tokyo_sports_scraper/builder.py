from .formatter import format_race_date

def build_race_url(race_date: str, race_circuit_number: int, race_number: int) -> str:
    """
    スクレイピング対象のURLを組み立てる。

    Parameters:
    - race_date: 日付（str）
    - race_circuit_number: サーキット番号（int）
    - race_number: 番号（int）

    Returns:
    - スクレイピング対象のURL（str）
    """
    base_url = 'https://autorace.tokyo-sports.co.jp/list/race/'
    formatted_race_date = format_race_date(race_date)
    formatted_race_circuit_number = f'{race_circuit_number:02}'
    return f'{base_url}{formatted_race_date}{formatted_race_circuit_number}{race_number}'
