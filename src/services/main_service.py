from typing import Dict, List

from src.api.client import APIClient
from src.Models.Vessels import Vessel
from src.api.endpoints import VesselSearchEndpoint, EventsEndpoint, BaseEndpoint
from src.data.processing import parse_vessel_data


def search_by_encounters():
    pass


def search_vessels_by_country(api_client: APIClient, search_vessel_endpoint: BaseEndpoint, country_code: str):
    # query: str = country_code
    vessels_by_country: List[Vessel] = []
    params: Dict[str, any] = search_vessel_endpoint.get_params().copy()
    params.update({"query": country_code})

    try:
        print(search_vessel_endpoint._get_full_url('some_path'))  # This will raise an exception
    except AttributeError as e:
        print(f"Error: {e}")
    response = api_client.make_request(search_vessel_endpoint.get_url(), params)
    parse_vessel_data(response)
    print(f"Response: {response}")


def create_endpoint(endpoint_type: str) -> BaseEndpoint:
    endpoint_mapping = {
        "vessel_search": VesselSearchEndpoint(),
        "event_search": EventsEndpoint(),
    }

    # TODO: add error caching
    endpoint = endpoint_mapping.get(endpoint_type)
    if endpoint is None:
        raise ValueError(f"Endpoint type '{endpoint_type}' is not recognized.")
    return endpoint