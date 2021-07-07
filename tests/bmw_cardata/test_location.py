"""
Tests for bmw_cardata/location.py.
"""

import pytest

import bmw_cardata.location


class TestLocation:
    def test_match_1(self):
        location = bmw_cardata.location.Location(
            {
                "name": "Test Location",
                "cost": {
                    "minute": 1.23,
                    "kwh": 0.0,
                },
                "match": {},
            }
        )
        assert location.match_session({})

        location.match["foo"] = "foo"
        charging_session = {
            "chargingLocation": {
                "foo": "foo",
            },
        }
        assert location.match_session(charging_session)

        location.match["foo"] = "bar"
        assert not location.match_session(charging_session)
