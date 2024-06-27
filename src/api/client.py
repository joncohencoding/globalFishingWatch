from typing import Dict, Optional
from urllib.parse import urlencode

import requests

from src.api.endpoints import HEADERS, ENCOUNTERS_QUERY_PARAMS, TIMEOUT, RETRY_COUNT, RETRY_BACKOFF_FACTOR, \
    BaseEndpoint, create_endpoint


# from src.api.endpoints import BASE_URL, USERS_ENDPOINT, HEADERS, DEFAULT_QUERY_PARAMS, TIMEOUT, RETRY_COUNT, RETRY_BACKOFF_FACTOR


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
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error occurred: {error}")
            print(f"Response text: {response.text}")
            raise
        return response.json() if response else None

    @staticmethod
    def make_special_request(query_url: str, params: Dict[str, any] = None) -> Optional[requests.Response]:
        query_string = urlencode(params, doseq=True)
        url = f"{query_url}?{query_string}"
        print(f"  special url: {url}")
        response = requests.get(url)
        print(f"special reponse.json: {response.json}")
        return response.json()

