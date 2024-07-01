from typing import List

from src.Models.Vessel import Vessel


class Country:
    def __init__(self, country_code: str = None, vessels: List[Vessel] = None, average_loitering_encounters: int = -1):
        self.country_code = country_code
        self.vessels = vessels
        self.average_loitering_encounters = average_loitering_encounters

    def __repr__(self):
        return (f"\nCountry code: {self.country_code}"
                f"\nVessels analyzed: {len(self.vessels)}"
                f"\nAverage loitering events per ship: {self.average_loitering_encounters}"
                )

    def to_table_row(self):
        return f"| {self.country_code:<12} | {len(self.vessels):<18} | {self.average_loitering_encounters:<28} |"

    @staticmethod
    def print_header():
        print(f"| {'Country Code':<12} | {'Vessel Sample Size':<18} | {'Avg Loitering Events by Ship':<27} |")
        print("|" + "-" * 14 + "|" + "-" * 20 + "|" + "-" * 30 + "|")