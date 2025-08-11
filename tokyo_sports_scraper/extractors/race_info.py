from bs4 import BeautifulSoup
from .utils import get_text_by_selector

def extract_race_title(soup: BeautifulSoup) -> str | None:
    """
    タイトルを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - タイトル（str）または None
    """
    return get_text_by_selector(soup, '.race-detail__ttl')

def extract_race_subtitle(soup: BeautifulSoup) -> str | None:
    """
    サブタイトルを抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - サブタイトル（str）または None
    """
    selector = 'div.race-detail__sub-ttl'
    return get_text_by_selector(soup, selector)

def extract_race_weather(soup: BeautifulSoup) -> str | None:
    """
    天候を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - 天候（str）または None
    """
    try:
        selector = 'div.race-detail__weather span:nth-of-type(2)'
        text = get_text_by_selector(soup, selector)
        return text.partition('：')[2] if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_temperature(soup: BeautifulSoup) -> str | None:
    """
    気温を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - 気温（str）または None
    """
    try:
        selector = 'div.race-detail__weather span:nth-of-type(2)'
        text = get_text_by_selector(soup, selector)
        return text.partition('：')[2] if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_humidity(soup: BeautifulSoup) -> str | None:
    """
    湿度を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - 湿度（str）または None
    """
    try:
        selector = 'div.race-detail__weather span:nth-of-type(3)'
        text = get_text_by_selector(soup, selector)
        return text.partition('：')[2] if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_pavement_temperature(soup: BeautifulSoup) -> str | None:
    """
    路面温度を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - 路面温度（str）または None
    """
    try:
        selector = 'div.race-detail__weather span:nth-of-type(4)'
        text = get_text_by_selector(soup, selector)
        return text.partition('：')[2] if text else None
    except (AttributeError, ValueError):
        return None

def extract_race_track_condition(soup: BeautifulSoup) -> str | None:
    """
    レースの走路状態を抽出する。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - 走路状態（str）または None
    """
    selector = 'div.race-detail__weather span:nth-of-type(5)'
    return get_text_by_selector(soup, selector)
