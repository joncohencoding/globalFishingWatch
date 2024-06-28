from typing import List

from src.Models.Vessel import Vessel


class Country:
    def __init__(self, country_code: str = None, vessels: List[Vessel] = None, average_loitering_encounters: int = -1):
        self.country_code = country_code
        self.vessels = vessels
        self.average_loitering_encounters = average_loitering_encounters

    # What is this?
    def __repr__(self):
        return (f"\nCountry code: {self.country_code}"
                f"\nVessels analyzed: {len(self.vessels)}"
                f"\nAverage loitering events per ship: {self.average_loitering_encounters}"
                )
        # return f"Country(country_code={self.country_code}, total_vessels_examined={len(self.vessels)}, average_loitering_encounters={self.average_loitering_encounters})"
