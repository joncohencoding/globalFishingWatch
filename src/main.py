from typing import List

from api.client import APIClient
from src.Models.Country import Country
from src.Models.Vessel import Vessel
from src.api.endpoints import BaseEndpoint, create_endpoint
from src.services.main_service import get_vessels_by_country, search_loitering_events_by_vessel_id, \
    check_each_vessel_for_loitering_event, get_average_loitering_events, analyze_loitering_by_country
from src.config import config

if __name__ == '__main__':
    print("Hello world")
    api_client = APIClient()
    analyze_loitering_by_country(api_client, config["COUNTRY_CODE_LIST"])
    # search_vessel_endpoint: BaseEndpoint = create_endpoint("vessel_search")
    # loitering_events_endpoint: BaseEndpoint = create_endpoint("loitering_event_search")
    # vessels: List[Vessel] = get_vessels_by_country(api_client,"NRU")
    # search_loitering_events_by_vessel_id(api_client, loitering_events_endpoint, vessel_ids=['372c7a017-73c5-48c9-6738-48dbda6f4d97'])
    # check_each_vessel_for_loitering_event(api_client, vessels)
    # get_average_loitering_events(vessels)
