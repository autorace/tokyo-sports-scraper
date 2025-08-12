import requests
from bs4 import BeautifulSoup
from .builder import build_race_url
from .extractors import (
    RaceInfo,
    RiderInfo,
)
from .model import Rider, Race

def scrape(race_date: str, race_circuit_number: int, race_number: int) -> Race:
    """
    東京スポーツのオートレース情報をスクレイプする。

    Parameters:
    - race_date: レースの日付（str）
    - race_circuit_number: レースのサーキット番号（int）
    - race_number: レースの番号（int）

    Returns:
    - オートレース情報（Race）
    """
    response = requests.get(build_race_url(race_date, race_circuit_number, race_number))
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    race_info = RaceInfo(soup)

    riders: list[Rider] = []
    for i in range(1, 9):
        rider_info = RiderInfo(soup, i)
        rider_name = rider_info.name()
        if rider_name:
            riders.append(Rider(
                name=rider_name,
                number=i,
                locker_ground=rider_info.locker_ground(),
                registration_term=rider_info.registration_term(),
                age=rider_info.age(),
                bike_class=rider_info.bike_class(),
                rank=rider_info.rank(),
                points=rider_info.points(),
                handicap=rider_info.handicap(),
                trial_time=rider_info.trial_time(),
                trial_deviation=rider_info.trial_deviation(),
                average_trial_time=rider_info.average_trial_time(),
                average_race_time=rider_info.average_race_time(),
                fastest_race_time=rider_info.fastest_race_time(),
            ))

    return Race(
        title=race_info.title(),
        subtitle=race_info.subtitle(),
        weather=race_info.weather(),
        temperature=race_info.temperature(),
        humidity=race_info.humidity(),
        pavement_temperature=race_info.pavement_temperature(),
        track_condition=race_info.track_condition(),
        riders=riders,
    )
