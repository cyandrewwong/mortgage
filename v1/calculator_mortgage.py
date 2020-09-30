import datetime as dt
import pandas as pd
from v1.scenario import Scenario
from typing import *


class MortgageSchedule:
    def __init__(self, fixedrate: float, fixedmonths: int, maxterm: int):
        """
        :param fixedrate: Fixed interest rate
        :param fixedmonths: In terms of months eg. '12M'
        """
        self._fixedrate = fixedrate
        self._fixedmonths = fixedmonths
        self._maxterm = maxterm

    def fixed_enddate(self, valdate: dt.date) -> dt.date:
        """
        :param valdate: MortgageStartDate
        :return: Date of when fixed period ends
        """
        return valdate + dt.timedelta(days=self._fixedmonths * 30)

    def enddate(self, valdate: dt.date) -> dt.date:
        return valdate + dt.timedelta(days=self._maxterm * 365)

    def fixed_schedule(self, valdate: dt.date, mortgage_val: float):
        dates = [valdate]
        for month in range(1, self._fixedmonths + 1):
            dates.append(valdate + dt.timedelta(days=month * 30))
            mortgage_val
        return pd.Series(data=[self._fixedrate * mortgage_val], index=dates)


class Mortgage:
    def __init__(self, scenario: Scenario, valdate: dt.date, schedule: MortgageSchedule):
        self._valdate = valdate
        self._property_val = scenario.property_val
        self._deposit = Mortgage.imply_deposit(scenario.deposit, self._property_val)
        self._schedule = schedule

    @property
    def deposit(self) -> float:
        return self._deposit

    @staticmethod
    def imply_deposit(deposit: Any, principle: float = 0.0) -> float:
        if isinstance(deposit, float):
            return deposit
        elif isinstance(deposit, str) and '%' in deposit:
            idx = deposit.find('%')
            pct = float(deposit[0:idx]) / 100
            return principle * pct

    def interest_schedule(self):
        result = pd.DataFrame(columns=['PayDate', 'Interest'])
        result.append(self._schedule.fixed_schedule(self._valdate, self._property_val * 1 - self._deposit))
