# Tokyo Sports Scraper

[![tests](https://github.com/autorace/tokyo-sports-scraper/actions/workflows/tests.yml/badge.svg)](https://github.com/autorace/tokyo-sports-scraper/actions/workflows/tests.yml)
[![publish](https://github.com/autorace/tokyo-sports-scraper/actions/workflows/publish.yml/badge.svg)](https://github.com/autorace/tokyo-sports-scraper/actions/workflows/publish.yml)
![issues](https://img.shields.io/github/issues/autorace/tokyo-sports-scraper)
![pull requests](https://img.shields.io/github/issues-pr/autorace/tokyo-sports-scraper)
[![last commit](https://img.shields.io/github/last-commit/autorace/tokyo-sports-scraper)](https://github.com/autorace/tokyo-sports-scraper/commits/main)
[![pypi](https://img.shields.io/pypi/v/autorace-tokyo-sports-scraper)](https://pypi.org/project/autorace-tokyo-sports-scraper/)
[![python](https://img.shields.io/badge/python-%3E%3D3.10-blue)](https://pypi.org/project/autorace-tokyo-sports-scraper/)
[![license](https://img.shields.io/github/license/autorace/tokyo-sports-scraper)](LICENSE)

東京スポーツのオートレース情報をスクレイピングするライブラリです。

## インストール
```bash
pip install autorace-tokyo-sports-scraper
```

## 使い方
```python
from tokyo_sports_scraper import scrape, Race, Rider

if __name__ == '__main__':
    race_info: Race = scrape('2025/08/04', 5, 8)

    print(f'タイトル: {race_info.title}')
    print(f'サブタイトル: {race_info.subtitle}')
    print(f'天候: {race_info.weather}')
    print(f'気温: {race_info.temperature}')
    print(f'湿度: {race_info.humidity}')
    print(f'走路温度: {race_info.pavement_temperature}')
    print(f'走路状況: {race_info.track_condition}')
    print('---')

    for rider_info in race_info.riders:
        print(f'車番: {rider_info.number}')
        print(f'名前: {rider_info.name}')
        print(f'LG: {rider_info.locker_ground}')
        print(f'期別: {rider_info.registration_term}')
        print(f'年齢: {rider_info.age}')
        print(f'車級: {rider_info.bike_class}')
        print(f'ランク: {rider_info.rank}')
        print(f'審査ポイント: {rider_info.points}')
        print(f'ハンデ: {rider_info.handicap}')
        print(f'試走タイム: {rider_info.trial_time}')
        print(f'試走偏差: {rider_info.trial_deviation}')
        print(f'平均試走タイム: {rider_info.average_trial_time}')
        print(f'平均競走タイム: {rider_info.average_race_time}')
        print(f'最高競走タイム: {rider_info.fastest_race_time}')
        print('---')
```

## ライセンス
Tokyo Sports Scraperは [MITライセンス](LICENSE) の元で公開されています。
