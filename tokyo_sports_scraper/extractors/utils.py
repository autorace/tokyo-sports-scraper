import re
from bs4 import BeautifulSoup

def get_text_by_selector(soup: BeautifulSoup, selector: str) -> str | None:
    """
    指定したCSSセレクタに一致する最初の要素のテキストを取得し、
    余分な空白を削除して返す。

    Parameters:
    - soup: BeautifulSoupオブジェクト
    - selector: CSSセレクタ文字列

    Returns:
    - テキスト（str）または None
    """
    try:
        if tag := soup.select_one(selector):
            text = tag.get_text(strip=True)
            return re.sub(r'\s+', ' ', text).strip()
        return None
    except (AttributeError, ValueError):
        return None

def count_weather_predictions(soup: BeautifulSoup) -> int:
    """
    晴予想と雨予想の項目数を返す。

    Parameters:
    - soup: BeautifulSoupオブジェクト

    Returns:
    - 項目数（int）または None
    """
    count = 0
    check_texts = ['晴予想', '雨予想']

    for i, expected in enumerate(check_texts, start=1):
        selector = f'thead.race-table__head th:nth-of-type({i})'
        text = get_text_by_selector(soup, selector)
        if text == expected:
            count += 1

    return count
