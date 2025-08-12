import re
from bs4 import BeautifulSoup
from .utils import get_text_by_selector

class RiderInfo:
    def __init__(self, soup: BeautifulSoup, rider_number: int):
        """
        選手の車番を元に各種情報を抽出するためのクラス。

        Parameters:
        - soup: BeautifulSoupオブジェクト
        - rider_number: 選手の車番（int）
        """
        self.soup = soup
        self.rider_number = rider_number

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

    def name(self) -> str | None:
        """
        選手の車番に対応する名前を抽出する。

        Returns:
        - 選手の名前（str）または None
        """
        selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__name a'
        return self._get_text_by_selector(selector)

    def locker_ground(self) -> str | None:
        """
        選手の車番に対応するLGを抽出する。

        Returns:
        - 選手のLG（str）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__info'
            text = self._get_text_by_selector(selector)
            return text.split('/')[0].strip() if text else None
        except (AttributeError, ValueError):
            return None

    def registration_term(self) -> str | None:
        """
        選手の車番に対応する期別を抽出する。

        Returns:
        - 選手の期別（str）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__info'
            text = self._get_text_by_selector(selector)
            return text.split('/')[1].strip() if text else None
        except (AttributeError, ValueError):
            return None

    def age(self) -> str | None:
        """
        選手の車番に対応する年齢を抽出する。

        Returns:
        - 選手の年齢（str）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__info'
            text = self._get_text_by_selector(selector)
            text = text.split('/')[2].strip() if text else None
            match = re.match(r'(\d+歳)(\d+級)', text) if text else None
            return match.group(1) if match else None
        except (AttributeError, ValueError):
            return None

    def bike_class(self) -> str | None:
        """
        選手の車番に対応する車級を抽出する。

        Returns:
        - 選手の車級（str）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__info'
            text = self._get_text_by_selector(selector)
            text = text.split('/')[2].strip() if text else None
            match = re.match(r'(\d+歳)(\d+級)', text) if text else None
            return match.group(2) if match else None
        except (AttributeError, ValueError):
            return None

    def rank(self) -> str | None:
        """
        選手の車番に対応するランクを抽出する。

        Returns:
        - 選手のランク（str）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__info'
            text = self._get_text_by_selector(selector)
            return text.split('/')[3].strip() if text else None
        except (AttributeError, ValueError):
            return None

    def points(self) -> float | None:
        """
        選手の車番に対応する審査ポイントを抽出する。

        Returns:
        - 選手の審査ポイント（float）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number} div.race-table__player-info div.race-table__info'
            text = self._get_text_by_selector(selector)
            return float(text.split('/')[4].strip()) if text else None
        except (AttributeError, ValueError):
            return None

    def handicap(self) -> int | None:
        """
        選手の車番に対応するハンデを抽出する。

        Returns:
        - 選手のハンデ（int）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number}:nth-of-type({self.rider_number * 3 - 2}) td.race-table__txt:nth-of-type(4)'
            text = self._get_text_by_selector(selector)
            return int(text) if text else None
        except (AttributeError, ValueError):
            return None

    def trial_time(self) -> float | None:
        """
        選手の車番に対応する試走タイムを抽出する。

        Returns:
        - 選手の試走タイム（float）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number}:nth-of-type({self.rider_number * 3 - 1}) td.race-table__txt:nth-of-type(1)'
            text = self._get_text_by_selector(selector)
            return float(text) if text else None
        except (AttributeError, ValueError):
            return None

    def trial_deviation(self) -> float | None:
        """
        選手の車番に対応する試走偏差を抽出する。

        Returns:
        - 選手の試走偏差（float）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number}:nth-of-type({self.rider_number * 3}) td.race-table__txt:nth-of-type(1)'
            text = self._get_text_by_selector(selector)
            return float(text) if text else None
        except (AttributeError, ValueError):
            return None

    def average_trial_time(self) -> float | None:
        """
        選手の車番に対応する平均試走タイムを抽出する。

        Returns:
        - 選手の平均試走タイム（float）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number}:nth-of-type({self.rider_number * 3 - 2}) td.race-table__txt:nth-of-type(5)'
            text = self._get_text_by_selector(selector)
            return float(text) if text else None
        except (AttributeError, ValueError):
            return None

    def average_race_time(self) -> float | None:
        """
        選手の車番に対応する平均競走タイムを抽出する。

        Returns:
        - 選手の平均競走タイム（float）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number}:nth-of-type({self.rider_number * 3 - 1}) td.race-table__txt:nth-of-type(2)'
            text = self._get_text_by_selector(selector)
            return float(text) if text else None
        except (AttributeError, ValueError):
            return None

    def fastest_race_time(self) -> float | None:
        """
        選手の車番に対応する最高競走タイムを抽出する。

        Returns:
        - 選手の最高競走タイム（float）または None
        """
        try:
            selector = f'tr.player-color-{self.rider_number}:nth-of-type({self.rider_number * 3}) td.race-table__txt:nth-of-type(2)'
            text = self._get_text_by_selector(selector)
            return float(text) if text else None
        except (AttributeError, ValueError):
            return None
