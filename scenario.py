from collection import CurveCollection
from typing import *
import datetime as dt


class Scenario:
    def __init__(self, valdate: dt.date, property_val: float, deposit: Any):
        self._valdate = valdate
        self._property_val = property_val
        self._deposit = deposit

    @property
    def valdate(self):
        return self._valdate

    @property
    def property_val(self):
        return self._property_val

    @property
    def deposit(self):
        return self._deposit
