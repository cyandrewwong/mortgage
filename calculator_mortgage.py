from typing import *
from curve import Curve
from scenario import Scenario
from collection import CurveCollection
from testscenario import TestScenario
import datetime as dt


class MortgageCalculator:
    def __init__(self, scen: Scenario, curves: CurveCollection = None):
        self._valdate = scen.valdate
        self._property_val = scen.property_val
        self._deposit = MortgageCalculator.imply_deposit(scen.deposit, scen.property_val)
        self._curves = curves

    @property
    def deposit(self):
        return self._deposit

    @staticmethod
    def imply_deposit(deposit: Any, principle: float = 0.0):
        if isinstance(deposit, float):
            return deposit
        elif isinstance(deposit, str) and '%' in deposit:
            idx = deposit.find('%')
            pct = float(deposit[0:idx]) / 100
            return principle * pct


if __name__ == '__main__':
    calculator = MortgageCalculator(TestScenario.scenario, )
