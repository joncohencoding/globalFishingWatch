import os
from typing import Dict
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

config: Dict[str, any] = {
    "BASE_URL": "https://gateway.api.globalfishingwatch.org/v3/",

    # PATHS
    "EVENTS_SEARCH_PATH": "events",
    "VESSELS_SEARCH_PATH": "vessels/search",

    "LIMIT": 50,
    "OFFSET": 0,
    "BEARER_TOKEN": os.getenv("BEARER_TOKEN")

}

