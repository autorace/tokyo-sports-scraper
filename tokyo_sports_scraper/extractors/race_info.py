from bs4 import BeautifulSoup
from .utils import get_text_by_selector

class RaceInfo:
    def __init__(self, soup: BeautifulSoup):
        """
        レースの各種情報を抽出するためのクラス。

        Parameters:
        - soup: BeautifulSoupオブジェクト
        """
        self.soup = soup

    def _get_text_by_selector(self, selector: str) -> str | None:
        """
        指定したCSSセレクタに一致する最初の要素のテキストを取得し、
        余分な空白を削除して返す。

        Parameters:
        - selector: CSSセレクタ文字列

        Returns:
        - テキスト（str）または None
        """
        return get_text_by_selector(self.soup, selector)

    def title(self) -> str | None:
        """
        タイトルを抽出する。

        Returns:
        - タイトル（str）または None
        """
        return self._get_text_by_selector('.race-detail__ttl')

    def subtitle(self) -> str | None:
        """
        サブタイトルを抽出する。

        Returns:
        - サブタイトル（str）または None
        """
        selector = 'div.race-detail__sub-ttl'
        return self._get_text_by_selector(selector)

    def weather(self) -> str | None:
        """
        天候を抽出する。

        Returns:
        - 天候（str）または None
        """
        try:
            selector = 'div.race-detail__weather span:nth-of-type(2)'
            text = self._get_text_by_selector(selector)
            return text.partition('：')[2] if text else None
        except (AttributeError, ValueError):
            return None

    def temperature(self) -> str | None:
        """
        気温を抽出する。

        Returns:
        - 気温（str）または None
        """
        try:
            selector = 'div.race-detail__weather span:nth-of-type(2)'
            text = self._get_text_by_selector(selector)
            return text.partition('：')[2] if text else None
        except (AttributeError, ValueError):
            return None

    def humidity(self) -> str | None:
        """
        湿度を抽出する。

        Returns:
        - 湿度（str）または None
        """
        try:
            selector = 'div.race-detail__weather span:nth-of-type(3)'
            text = self._get_text_by_selector(selector)
            return text.partition('：')[2] if text else None
        except (AttributeError, ValueError):
            return None

    def pavement_temperature(self) -> str | None:
        """
        路面温度を抽出する。

        Returns:
        - 路面温度（str）または None
        """
        try:
            selector = 'div.race-detail__weather span:nth-of-type(4)'
            text = self._get_text_by_selector(selector)
            return text.partition('：')[2] if text else None
        except (AttributeError, ValueError):
            return None

    def track_condition(self) -> str | None:
        """
        レースの走路状態を抽出する。

        Returns:
        - 走路状態（str）または None
        """
        selector = 'div.race-detail__weather span:nth-of-type(5)'
        return self._get_text_by_selector(selector)
