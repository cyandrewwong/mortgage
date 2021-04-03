"""
Calculator for interest
"""
from v3.structs.schedule import Schedule
from typing import Union


class ClcIntersest:
    def __init__(self, notional: float, rates: Union[float, Schedule]):
        self._notional = notional
        self._rates = rates

    def generate_flows(self):
        pass