import requests
from bs4 import BeautifulSoup
from .builder import build_race_url
from .extractors import (
    extract_race_title,
    extract_race_subtitle,
    extract_race_weather,
    extract_race_temperature,
    extract_race_humidity,
    extract_race_pavement_temperature,
    extract_race_track_condition,
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
        title=extract_race_title(soup),
        subtitle=extract_race_subtitle(soup),
        weather=extract_race_weather(soup),
        temperature=extract_race_temperature(soup),
        humidity=extract_race_humidity(soup),
        pavement_temperature=extract_race_pavement_temperature(soup),
        track_condition=extract_race_track_condition(soup),
        riders=riders,
    )
