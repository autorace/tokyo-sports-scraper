import re
from bs4 import BeautifulSoup
from .utils import get_text_by_selector

def extract_race_rider_name(soup: BeautifulSoup, rider_number: int) -> str | None:
    """
    選手の車番に対応する名前を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の名前（str）または None
    """
    selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__name a'
    return get_text_by_selector(soup, selector)

def extract_race_rider_locker_ground(soup: BeautifulSoup, rider_number: int) -> str | None:
    """
    選手の車番に対応するLGを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手のLG（str）または None
    """
    try:
        selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__info'
        text = get_text_by_selector(soup, selector)
        return text.split('/')[0].strip() if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_registration_term(soup: BeautifulSoup, rider_number: int) -> str | None:
    """
    選手の車番に対応する期別を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の期別（str）または None
    """
    try:
        selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__info'
        text = get_text_by_selector(soup, selector)
        return text.split('/')[1].strip() if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_age(soup: BeautifulSoup, rider_number: int) -> str | None:
    """
    選手の車番に対応する年齢を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の年齢（str）または None
    """
    try:
        selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__info'
        text = get_text_by_selector(soup, selector)
        text = text.split('/')[2].strip() if text else None
        match = re.match(r'(\d+歳)(\d+級)', text) if text else None
        return match.group(1) if match else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_bike_class(soup: BeautifulSoup, rider_number: int) -> str | None:
    """
    選手の車番に対応する車級を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の車級（str）または None
    """
    try:
        selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__info'
        text = get_text_by_selector(soup, selector)
        text = text.split('/')[2].strip() if text else None
        match = re.match(r'(\d+歳)(\d+級)', text) if text else None
        return match.group(2) if match else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_rank(soup: BeautifulSoup, rider_number: int) -> str | None:
    """
    選手の車番に対応するランクを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手のランク（str）または None
    """
    try:
        selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__info'
        text = get_text_by_selector(soup, selector)
        return text.split('/')[3].strip() if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_points(soup: BeautifulSoup, rider_number: int) -> float | None:
    """
    選手の車番に対応する審査ポイントを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の審査ポイント（float）または None
    """
    try:
        selector = f'tr.player-color-{rider_number} div.race-table__player-info div.race-table__info'
        text = get_text_by_selector(soup, selector)
        return float(text.split('/')[4].strip()) if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_handicap(soup: BeautifulSoup, rider_number: int) -> int | None:
    """
    選手の車番に対応するハンデを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手のハンデ（int）または None
    """
    try:
        selector = f'tr.player-color-{rider_number}:nth-of-type({rider_number * 3 - 2}) td.race-table__txt:nth-of-type(4)'
        text = get_text_by_selector(soup, selector)
        return int(text) if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_trial_time(soup: BeautifulSoup, rider_number: int) -> float | None:
    """
    選手の車番に対応する試走タイムを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の試走タイム（float）または None
    """
    try:
        selector = f'tr.player-color-{rider_number}:nth-of-type({rider_number * 3 - 1}) td.race-table__txt:nth-of-type(1)'
        text = get_text_by_selector(soup, selector)
        return float(text) if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_trial_deviation(soup: BeautifulSoup, rider_number: int) -> float | None:
    """
    選手の車番に対応する試走偏差を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の試走偏差（float）または None
    """
    try:
        selector = f'tr.player-color-{rider_number}:nth-of-type({rider_number * 3}) td.race-table__txt:nth-of-type(1)'
        text = get_text_by_selector(soup, selector)
        return float(text) if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_average_trial_time(soup: BeautifulSoup, rider_number: int) -> float | None:
    """
    選手の車番に対応する平均試走タイムを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の平均試走タイム（float）または None
    """
    try:
        selector = f'tr.player-color-{rider_number}:nth-of-type({rider_number * 3 - 2}) td.race-table__txt:nth-of-type(5)'
        text = get_text_by_selector(soup, selector)
        return float(text) if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_rider_average_race_time(soup: BeautifulSoup, rider_number: int) -> float | None:
    """
    選手の車番に対応する平均競走タイムを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - rider_number: 選手の車番（int）

    Returns:
    - 選手の平均競走タイム（float）または None
    """
    try:
        selector = f'tr.player-color-{rider_number}:nth-of-type({rider_number * 3 - 1}) td.race-table__txt:nth-of-type(2)'
        text = get_text_by_selector(soup, selector)
        return float(text) if text else None
    except (AttributeError, ValueError):
        return None
