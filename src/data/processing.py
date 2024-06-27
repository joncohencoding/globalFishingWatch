import json
from typing import List

from src.Models.Vessels import Vessel


def parse_vessel_data(data, check_flag: str = None):
    new_vessels: List[Vessel] = []
    vessel_id = ship_type = shipname = flag = callsign = None
    for entry in data.get('entries'):
        registry_info = entry.get('registryInfo')
        if check_flag is not None:
            flag: str = registry_info[0].get('flag') if registry_info[0].get('flag') == check_flag else "FLAG_MISMATCH"
        else:
            flag = registry_info[0].get('flag')


        combined_sources_info = entry.get('combinedSourcesInfo')[0]
        vessel_id: str = combined_sources_info.get('shiptypes')[0].get('vesselId')
        ship_type: str = combined_sources_info.get('shiptypes')[0].get('name')

        self_reported = entry.get('selfReportedInfo')[0]
        vessel_id: str = self_reported.get('id') if vessel_id is None else vessel_id
        shipname: str = self_reported.get('shipname')
        callsign: str = self_reported.get('callsign')

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
