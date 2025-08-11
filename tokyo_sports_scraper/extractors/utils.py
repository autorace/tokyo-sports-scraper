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
