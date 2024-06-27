from typing import Dict, List

from src.api.client import APIClient
from src.Models.Vessels import Vessel
from src.api.endpoints import VesselSearchEndpoint, LoiteringEventsEndpoint, BaseEndpoint
from src.data.processing import parse_vessel_data


def search_by_encounters():
    pass


def search_vessels_by_country(api_client: APIClient, search_vessel_endpoint: BaseEndpoint, country_code: str):
    # query: str = country_code
    vessels_by_country: List[Vessel] = []
    params: Dict[str, any] = search_vessel_endpoint.get_params().copy()
    params.update({"where": f'registryInfo.flag="{country_code}"'})

    response = api_client.make_request(search_vessel_endpoint.get_url(), params)
    parse_vessel_data(response, country_code)
    print(f"Response: {response}")
