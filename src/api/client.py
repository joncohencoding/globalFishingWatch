from typing import Dict, Optional

import requests

from src.api.endpoint_gf import BASE_URL, ENCOUNTERS_ENDPOINT, HEADERS, ENCOUNTERS_QUERY_PARAMS, TIMEOUT, RETRY_COUNT, RETRY_BACKOFF_FACTOR
# from src.api.endpoints import BASE_URL, USERS_ENDPOINT, HEADERS, DEFAULT_QUERY_PARAMS, TIMEOUT, RETRY_COUNT, RETRY_BACKOFF_FACTOR


class APIClient:
    # @staticmethod
    # def get_user_by_username(username):
    #     query_url = f"{USERS_ENDPOINT}?username={username}"
    #     response = requests.get(query_url, headers=HEADERS, timeout=TIMEOUT)
    #     response.raise_for_status()  # Raise an exception for HTTP errors
    #     users = response.json()
    #     if users:
    #         return users[0]
    #     return None

    @staticmethod
    def get_encounters():
        query_url = f"{ENCOUNTERS_ENDPOINT}"
        print(f"Requesting encounter data...")
        response = requests.get(query_url, headers=HEADERS, timeout=TIMEOUT, params=ENCOUNTERS_QUERY_PARAMS)
        print(f"Generated URL: {response.url}")
        try:
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error occurred: {error}")  # Print the HTTP error
            print(f"Response text: {response.text}")  # Print the response body for more details
            raise
        encounters = response.json()
        return encounters if encounters else None

    # pull headers from config file
    # pull timeout from config file
    @staticmethod
    def make_request(query_url: str, params: Dict[str, any] = None) -> Optional[requests.Response]:
        print(f"Requesting data...")
        response = requests.get(query_url, params=params, headers=HEADERS, timeout=TIMEOUT)
        print(f"Generated URL: {response.url}")
        try:
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error occurred: {error}")  # Print the HTTP error
            print(f"Response text: {response.text}")  # Print the response body for more details
            raise
        return response.json() if response else None
