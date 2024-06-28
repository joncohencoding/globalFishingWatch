import asyncio
from typing import Dict, List

from src.api.client import APIClient
from src.Models.Vessel import Vessel
from src.data.processing import parse_vessel_data, parse_loitering_data


async def get_vessels_by_country(api_client: APIClient, country_code: str) -> List[Vessel]:
    params: Dict[str, any] = api_client.search_vessel_endpoint.get_params().copy()
    params.update({"where": f'registryInfo.flag="{country_code}"'})

    response = await api_client.make_request(api_client.search_vessel_endpoint.get_url(), params)
    sample_vessels = parse_vessel_data(response, check_flag=country_code)
    return sample_vessels


# Given a vessel_id, gather loitering data
async def get_loitering_events_by_vessel_id(api_client: APIClient, vessel_id: List[str]):
    params: Dict[str, any] = api_client.loitering_events_endpoint.get_params().copy()
    params.update({"vessels[]": vessel_id})
    response = await api_client.make_request(api_client.loitering_events_endpoint.get_url(), params)
    return response


# Given a list of vessels, fetch the loitering data for each vessel, then update the vessel object
# with count of loitering instances
async def gather_loitering_data_for_vessels1(api_client: APIClient, vessels: List[Vessel]) -> None:
    tasks = []
    for vessel in vessels:
        if vessel.vessel_id is not None:
            task = get_loitering_events_by_vessel_id(api_client, [vessel.vessel_id])
            tasks.append(task)
    loitering_data_list_by_vessel = await asyncio.gather(*tasks)
    # TODO: to improve performance, just grab the total when making api call, if possible
    for data, vessel in zip(loitering_data_list_by_vessel, vessels):
        parse_loitering_data(data, vessel)


async def gather_loitering_data_for_vessels(api_client: APIClient, vessels: List[Vessel]) -> None:
    url_params_list = []
    for vessel in vessels:
        if vessel.vessel_id is not None:
            # task = get_loitering_events_by_vessel_id(api_client, [vessel.vessel_id])
            params: Dict[str, any] = api_client.loitering_events_endpoint.get_params().copy()
            params.update({"vessels[]": vessel.vessel_id})
            url_params_list.append({"url": api_client.loitering_events_endpoint.get_url(), "params": params})
    results = await api_client.make_concurrent_requests(url_params_list)
    # TODO: to improve performance, just grab the total when making api call, if possible
    for result, vessel in zip(results, vessels):
        parse_loitering_data(result, vessel)


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
        print(f'Average loitering events for {vessels[0].flag}: {round(average_loitering_events)}')
    else:
        average_loitering_events = -1
        print("No vessels found")

    return average_loitering_events

