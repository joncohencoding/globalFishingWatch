# TODO: move these config variables to a config file?

from typing import Dict

BASE_URL: str = "https://jsonplaceholder.typicode.com"
USERS_ENDPOINT: str = f"{BASE_URL}/users"

HEADERS: Dict[str, str] = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

DEFAULT_QUERY_PARAMS: Dict[str, any] = {
    "limit": 100,
}
# Timeout Settings (in seconds)
TIMEOUT: int = 10

# Retry settings
RETRY_COUNT = 3
RETRY_BACKOFF_FACTOR = 0.3
