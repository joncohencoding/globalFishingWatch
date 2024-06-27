from api.client import APIClient
from src.api.endpoints import BaseEndpoint, create_endpoint
from src.services.main_service import search_vessels_by_country


if __name__ == '__main__':
    print("Hello world")
    api_client = APIClient()
    search_vessel_endpoint: BaseEndpoint = create_endpoint("vessel_search")
    search_vessels_by_country(api_client, search_vessel_endpoint, "NRU")
