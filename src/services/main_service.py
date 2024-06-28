from typing import Dict, List

from src.Models.Country import Country
from src.api.client import APIClient
from src.config import config
from src.services.main_services_helper_functions import get_vessels_by_country, gather_loitering_data_for_vessels, \
    get_average_loitering_events


def run_application():
    print("Starting application designed to find average loitering events for a sample of ships by country")
    api_client = APIClient()
    analyze_loitering_by_country(api_client, config["COUNTRY_CODE_LIST"])


def analyze_loitering_by_country(api_client: APIClient, country_code_list: List[str]) -> None:
    country_list: List[Country] = []
    # Create country objects
    for country_code in country_code_list:
        country_list.append(Country(country_code=country_code))

    # Get sample vessels from each country
    # gather loitering data for each vessel
    for country in country_list:
        country.vessels = get_vessels_by_country(api_client, country.country_code)
        gather_loitering_data_for_vessels(api_client, country.vessels)
        country.average_loitering_encounters = get_average_loitering_events(country.vessels)

    # Display loitering information
    for country in country_list:
        print(f"\nCountry code: {country.country_code}")
        print(f"Vessels analyzed: {len(country.vessels)}")
        print(f"Average loitering events per ship: {country.average_loitering_encounters}\n")
