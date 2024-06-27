# TODO: move these config variables to a config file?
import os
from abc import abstractmethod
from typing import Dict
from src.config import config

BASE_URL: str = "https://gateway.api.globalfishingwatch.org/v3/events"
ENCOUNTERS_ENDPOINT: str = f"{BASE_URL}"



HEADERS: Dict[str, str] = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "AUTHORIZATION": f"Bearer {config['BEARER_TOKEN']}"
}

ENCOUNTERS_QUERY_PARAMS: Dict[str, any] = {
    "limit": 1,
    "datasets[0]": "public-global-loitering-events:latest",
    "offset": 0,
    # "sort":"-start",
    # "start-date":"2024-06-20",
    # "encounter-types": ["CARRIER-FISHING", "FISHING-CARRIER"],
    # "include-regions": "MPA",
    # "confidences": [2, 3, 4],
}
# Timeout Settings (in seconds)
TIMEOUT: int = 30

# Retry settings
RETRY_COUNT = 5
RETRY_BACKOFF_FACTOR = 1


# TODO:  make this abstract
# TODO: Reevaluate how base_params are added. May be a conflict with adding both new base_params and additional params. Maybe just get rid of base_params in parent class
class BaseEndpoint:
    def __init__(self, base_params: Dict[str, any] = None) -> None:
        self.base_url = config["BASE_URL"]
        self.params = base_params if base_params else {}
        self.headers = HEADERS

    # There is probably a cleaner way to do this. DOn't want to accidentally
    # call get_full_url from child classes
    def _get_full_url(self, path) -> str:
        return f"{self.base_url}/{path}"

    @abstractmethod
    def get_url(self):
        raise NotImplementedError

    def get_params(self) -> Dict[str, any]:
        return self.params

    def set_params(self, **kwargs) -> None:
        self.params.update(kwargs)


class VesselSearchEndpoint(BaseEndpoint):
    # TODO: reevaluate how params are ingested
    def __init__(self, additional_params: Dict[str, any] = None):
        super().__init__()
        # self.path = "vessels/search"
        self.path = config["VESSELS_SEARCH_PATH"]
        self.params = {
            "datasets[0]": "public-global-vessel-identity:latest",
            "limit": config["LIMIT"]
        }
        if additional_params:
            self.params.update(additional_params)

    def get_url(self):
        return self._get_full_url(self.path)


class EventsEndpoint(BaseEndpoint):
    # TODO: update the way params are handled
    def __init__(self):
        # ? Is this super init necessary
        super().__init__()
        self.path = config["EVENTS_SEARCH_PATH"]

    def get_url(self):
        return self._get_full_url(self.path)
