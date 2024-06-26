from typing import Dict

from api.client import APIClient
from src.api.endpoint_gf import VesselSearchEndpoint, EventsEndpoint, BaseEndpoint


def search_by_encounters():
    client = APIClient()
    print("APIClient Initialized...")
    data = client.get_encounters()
    print(data)


def search_vessels_by_country(api_client: APIClient, search_vessel_endpoint: BaseEndpoint, country_code: str):
    # query: str = country_code
    params: Dict[str, any] = search_vessel_endpoint.get_params().copy()
    params.update({"query": country_code})

    response = api_client.make_request(search_vessel_endpoint.get_url(), params)
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


if __name__ == '__main__':
    print("Hello world")
    # search_by_username()
    api_client = APIClient()
    # search_by_encounters()
    search_vessel_endpoint: BaseEndpoint = create_endpoint("vessel_search")
    search_vessels_by_country(api_client, search_vessel_endpoint, "NRU")
