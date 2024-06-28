import asyncio

import aiohttp
from typing import Dict, Optional, List
from urllib.parse import urlencode
import logging

import requests
from src.config import config

from src.api.endpoints import HEADERS, TIMEOUT, BaseEndpoint, create_endpoint

RETRY_COUNT = config["RETRY_COUNT"]
RETRY_BACKOFF_FACTOR = config["RETRY_BACKOFF_FACTOR"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self):
        self.search_vessel_endpoint: BaseEndpoint = create_endpoint("vessel_search")
        self.loitering_events_endpoint: BaseEndpoint = create_endpoint("loitering_event_search")

    @staticmethod
    def make_request_sync(query_url: str, params: Dict[str, any] = None) -> Optional[requests.Response]:
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

    @staticmethod
    async def fetch(session, url: str, params: Dict[str, any] = None) -> Dict:
        for attempt in range(RETRY_COUNT):
            try:
                async with session.get(url, params=params, headers=HEADERS, timeout=TIMEOUT) as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.client_exceptions.ServerDisconnectedError as e:
                logger.error(f"Server disconnected. Attempt {attempt + 1} of {RETRY_COUNT}.")
                if attempt < RETRY_COUNT - 1:
                    await asyncio.sleep(RETRY_BACKOFF_FACTOR * (2 ** attempt))
                else:
                    raise
            except aiohttp.client_exceptions.ClientResponseError as e:
                logger.error(f"Client response error: {e}.")
                raise
            except aiohttp.ClientError as e:
                logger.error(f"Client error: {e}.")
                raise

    async def make_request(self, query_url: str, params: Dict[str, any] = None) -> Optional[Dict]:
        async with aiohttp.ClientSession() as session:
            return await self.fetch(session, query_url, params)

    async def make_concurrent_requests(self, url_params_list: List[Dict[str, any]]):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, item['url'], item['params']) for item in url_params_list]
            return await asyncio.gather(*tasks)

# async def fetch(self, status, query_url, params):
#     async with self.make_request(query_url, params) as req:
#         return await req.text
#
# async def fetch_all(self, api_client, status, query_url, params):
