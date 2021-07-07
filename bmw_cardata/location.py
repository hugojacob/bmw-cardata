"""
location.py
"""
import pathlib
import typing

import yaml


class Location:
    """
    Abstraction to a location.

    A location is useful to qualify a charging session so that the charging costs can be
    computed.
    """

    @classmethod
    def from_file(cls: typing.Type, file: pathlib.Path) -> list:
        """
        Load the locations from an YAML file.
        """
        locations = yaml.load(file.read_text())
        return [cls(location) for location in locations]

    def __init__(self, data: dict):
        self.name = data["name"]
        self.cost_minute = data["cost"]["minute"]
        self.cost_kwh = data["cost"]["kwh"]
        self.match = data["match"]

    def match_session(self, charging_session: dict) -> bool:
        """
        Match a given charging session and the location.
        """
        for key, value in self.match.items():
            if key in charging_session["chargingLocation"]:
                if charging_session["chargingLocation"][key] != value:
                    return False
            else:
                return False

        return True

    def costs(self, charging_session: dict) -> typing.Union[float, None]:
        """
        Check whether a charging session matches the location and return the charging
        session costs.

        If the charging session doesn't match the location, then `None` is returned.

        :param charging_session: The charging session to compute the costs.
        """
        if self.match(charging_session):
            return 0.0

        return None
