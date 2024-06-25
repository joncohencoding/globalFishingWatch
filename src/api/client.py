import requests

from src.api.endpoints import BASE_URL, USERS_ENDPOINT, HEADERS, DEFAULT_QUERY_PARAMS, TIMEOUT, RETRY_COUNT, RETRY_BACKOFF_FACTOR


class APIClient:
    @staticmethod
    def get_user_by_username(username):
        query_url = f"{USERS_ENDPOINT}?username={username}"
        response = requests.get(query_url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP errors
        users = response.json()
        if users:
            return users[0]
        return None
