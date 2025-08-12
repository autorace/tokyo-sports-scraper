from importlib.metadata import version, PackageNotFoundError
from .model import Rider, Race
from .scraper import scrape

try:
    __version__ = version("tokyo-sports-scraper")
except PackageNotFoundError:
    __version__ = '0.0.0'

__all__ = ['Rider', 'Race', 'scrape']
