import json
from typing import List

from src.Models.Vessel import Vessel


def parse_vessel_data(data, check_flag: str = None) -> List[Vessel]:
    new_vessels: List[Vessel] = []
    vessel_id = ship_type = shipname = flag = callsign = None
    for entry in data.get('entries'):
        registry_info = entry.get('registryInfo')
        if check_flag is not None and len(registry_info) > 0:
            flag: str = registry_info[0].get('flag') if registry_info[0].get('flag') == check_flag else "FLAG_MISMATCH"
        elif len(registry_info) > 0:
            flag = registry_info[0].get('flag')
        else:
            flag = None

        combined_sources_info = entry.get('combinedSourcesInfo')
        if len(combined_sources_info) > 0:
            vessel_id: str = combined_sources_info[0].get('shiptypes')[0].get('vesselId')
            ship_type: str = combined_sources_info[0].get('shiptypes')[0].get('name')

        self_reported = entry.get('selfReportedInfo')
        if len(self_reported) > 0:
            vessel_id: str = self_reported[0].get('id') if vessel_id is None else vessel_id
            shipname: str = self_reported[0].get('shipname')
            callsign: str = self_reported[0].get('callsign')

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
