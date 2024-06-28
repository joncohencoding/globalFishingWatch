from typing import Dict, Optional
from urllib.parse import urlencode

import requests

from src.api.endpoints import HEADERS, TIMEOUT, BaseEndpoint, create_endpoint


class APIClient:
    def __init__(self):
        self.search_vessel_endpoint: BaseEndpoint = create_endpoint("vessel_search")
        self.loitering_events_endpoint: BaseEndpoint = create_endpoint("loitering_event_search")

    @staticmethod
    def make_request(query_url: str, params: Dict[str, any] = None) -> Optional[requests.Response]:
        print(f"Requesting data...")
        response = requests.get(query_url, params=params, headers=HEADERS, timeout=TIMEOUT)
        print(f"Generated URL: {response.url}")
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error occurred: {error}")
            print(f"Response text: {response.text}")
            raise
        return response.json() if response else None


