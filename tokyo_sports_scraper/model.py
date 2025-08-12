from dataclasses import dataclass

@dataclass
class Rider:
    name: str | None
    number: int | None
    locker_ground: str | None
    registration_term: str | None
    age: str | None
    bike_class: str | None
    rank: str | None
    points: float | None
    handicap: float | None
    trial_time: float | None
    trial_deviation: float | None # 試走偏差
    average_trial_time: float | None
    average_race_time: float | None
    fastest_race_time : float | None

@dataclass
class Race:
    title: str | None
    subtitle: str | None
    weather: str | None
    temperature: str | None
    humidity: str | None
    pavement_temperature: str | None
    track_condition: str | None
    riders: list[Rider]
