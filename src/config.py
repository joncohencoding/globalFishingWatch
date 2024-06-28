import os
from typing import Dict
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

config: Dict[str, any] = {
    "BASE_URL": "https://gateway.api.globalfishingwatch.org/v3",

    # PATHS
    "EVENTS_SEARCH_PATH": "events",
    "VESSELS_SEARCH_PATH": "vessels/search",

    # DATASETS
    "LOITERING_DATA_SET": "public-global-loitering-events:latest",
    "VESSELS_DATA_SET": "public-global-vessel-identity:latest",

    "LIMIT": 50,
    "OFFSET": 0,
    "BEARER_TOKEN": os.getenv("BEARER_TOKEN"),

    "TIMEOUT": 300,
    "RETRY_COUNT": 5,
    "RETRY_BACKOFF_FACTOR": 1,

    "COUNTRY_CODE_LIST": ["GRC", "FRA", "USA", "SAU", "COL", "RUS", "JPN", "ARG", "AUS", "ETH", "BRA"]
}

