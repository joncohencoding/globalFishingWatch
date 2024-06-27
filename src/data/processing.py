import json
from typing import List

from src.Models.Vessels import Vessel


def parse_vessel_data(data):
    new_vessels: List[Vessel] = []
    vessel_id = ship_type = shipname = flag = callsign = None
    for entry in data.get('entries'):

        combined_sources_info = entry.get('combinedSourcesInfo')[0]
        vessel_id: str = combined_sources_info.get('shiptypes')[0].get('vesselId')
        ship_type: str = combined_sources_info.get('shiptypes')[0].get('name')
        for self_reported in entry.get('selfReportedInfo'):
            vessel_id: str = self_reported.get('id') if vessel_id is None else vessel_id
            shipname: str = self_reported.get('shipname')
            flag: str = self_reported.get('flag')
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
