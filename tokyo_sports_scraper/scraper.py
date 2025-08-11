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
    extract_race_rider_name,
    extract_race_rider_locker_ground,
    extract_race_rider_registration_term,
    extract_race_rider_age,
    extract_race_rider_bike_class,
    extract_race_rider_rank,
    extract_race_rider_points,
    extract_race_rider_handicap,
    extract_race_rider_trial_time,
    extract_race_rider_trial_deviation,
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
        rider_name = extract_race_rider_name(soup, i)
        if rider_name:
            riders.append(Rider(
                name=rider_name,
                number=i,
                locker_ground=extract_race_rider_locker_ground(soup, i),
                registration_term=extract_race_rider_registration_term(soup, i),
                age=extract_race_rider_age(soup, i),
                bike_class=extract_race_rider_bike_class(soup, 1),
                rank=extract_race_rider_rank(soup, i),
                points=extract_race_rider_points(soup, i),
                handicap=extract_race_rider_handicap(soup, i),
                trial_time=extract_race_rider_trial_time(soup, i),
                trial_deviation=extract_race_rider_trial_deviation(soup, i),
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
