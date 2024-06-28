import asyncio
from typing import Dict, List

from src.Models.Country import Country
from src.api.client import APIClient
from src.config import config
from src.services.main_services_helper_functions import get_vessels_by_country, gather_loitering_data_for_vessels, \
    get_average_loitering_events


async def run_application():
    print("Starting application designed to find average loitering events for a sample of ships by country")
    api_client = APIClient()
    await analyze_loitering_by_country(api_client, config["COUNTRY_CODE_LIST"])


# Get sample vessels from each country
# gather loitering data for each vessel
async def process_country(api_client: APIClient, country: Country):
    country.vessels = await get_vessels_by_country(api_client, country.country_code)
    await gather_loitering_data_for_vessels(api_client, country.vessels)
    country.average_loitering_encounters = get_average_loitering_events(country.vessels)


async def analyze_loitering_by_country(api_client: APIClient, country_code_list: List[str]) -> None:
    country_list: List[Country] = [Country(country_code=code) for code in country_code_list]

    # Create tasks for each country so they can be analyzed concurrently
    tasks = [process_country(api_client, country) for country in country_list]

    await asyncio.gather(*tasks)

    # Display loitering information
    Country.print_header()
    for country in country_list:
        print(country.to_table_row())
