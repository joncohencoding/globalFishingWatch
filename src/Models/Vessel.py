class Vessel:
    def __init__(self, vessel_id: str = None, ship_type: str = None, shipname: str = None, flag: str = None, callsign: str = None, total_loitering_events: int = 0):
        self.vessel_id = vessel_id
        self.ship_type = ship_type
        self.shipname = shipname
        self.flag = flag
        self.callsign = callsign
        self.total_loitering_events = total_loitering_events

    # What is this?
    def __repr__(self):
        return f"Vessel(vessel_id={self.vessel_id}, ship_type={self.ship_type}, shipname={self.shipname}, flag={self.flag}, callsign={self.callsign})"
