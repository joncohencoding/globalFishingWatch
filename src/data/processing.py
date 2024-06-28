import json
from typing import List

from src.Models.Vessel import Vessel


def parse_vessel_data(data, check_flag: str = None) -> List[Vessel]:
    new_vessels: List[Vessel] = []
    vessel_id = ship_type = shipname = flag = callsign = None
    for entry in data.get('entries'):
        registry_info = entry.get('registryInfo')
        if flag is not None:
            flag: str = check_flag
        elif registry_info is not None and len(registry_info) > 0:
            flag = registry_info[0].get('flag')
        else:
            flag = "NO_DATA"

        combined_sources_info = entry.get('combinedSourcesInfo')
        if combined_sources_info is not None and len(combined_sources_info) > 0:
            vessel_id: str = combined_sources_info[0].get('shiptypes')[0].get('vesselId')
            ship_type: str = combined_sources_info[0].get('shiptypes')[0].get('name')

        self_reported_info = entry.get('selfReportedInfo')
        if self_reported_info is not None and len(self_reported_info) > 0:
            vessel_id: str = self_reported_info[0].get('id') if vessel_id is None else vessel_id
            shipname: str = self_reported_info[0].get('shipname')
            callsign: str = self_reported_info[0].get('callsign')

        vessel = Vessel(
            vessel_id=vessel_id,
            ship_type=ship_type,
            shipname=shipname,
            flag=flag,
            callsign=callsign,
            )
        new_vessels.append(vessel)
        print(vessel)

    return new_vessels


def parse_loitering_data(data, vessel) -> None:
    total_loitering_instances = data.get('total')
    vessel.total_loitering_events = total_loitering_instances
    return
