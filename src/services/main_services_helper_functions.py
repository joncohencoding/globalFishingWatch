from typing import Dict, List

from src.api.client import APIClient
from src.Models.Vessel import Vessel
from src.data.processing import parse_vessel_data, parse_loitering_data


def get_vessels_by_country(api_client: APIClient, country_code: str) -> List[Vessel]:
    params: Dict[str, any] = api_client.search_vessel_endpoint.get_params().copy()
    params.update({"where": f'registryInfo.flag="{country_code}"'})

    response = api_client.make_request(api_client.search_vessel_endpoint.get_url(), params)
    sample_vessels = parse_vessel_data(response, check_flag=country_code)
    return sample_vessels


def search_loitering_events_by_vessel_id(api_client: APIClient, vessel_ids: List[str]):
    params: Dict[str, any] = api_client.loitering_events_endpoint.get_params().copy()
    params.update({"vessels[]": vessel_ids})
    response = api_client.make_request(api_client.loitering_events_endpoint.get_url(), params)
    return response


# TODO put endpoints in apiclient
def gather_loitering_data_for_vessels(api_client: APIClient, vessels: List[Vessel]) -> None:
    for vessel in vessels:
        if vessel.vessel_id is not None:
            data = search_loitering_events_by_vessel_id(api_client, [vessel.vessel_id])
            parse_loitering_data(data, vessel)


def get_average_loitering_events(vessels: List[Vessel]) -> float:
    total_vessels: int = len(vessels)
    total_loitering_events: int = 0
    for vessel in vessels:
        print(f'{vessel.vessel_id}: {vessel.total_loitering_events}')
        total_loitering_events += vessel.total_loitering_events
        total_vessels += 1

    print('--------------------------')
    if total_vessels > 0:
        average_loitering_events = round(total_loitering_events/total_vessels, 2)
        print(f'Average loitering events: {round(average_loitering_events)}')
    else:
        average_loitering_events = -1
        print("No vessels found")

    return average_loitering_events

