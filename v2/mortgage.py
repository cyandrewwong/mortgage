import datetime as dt
import pandas as pd
from typing import *


class Mortgage:
    def __init__(self, start: dt.date, periods: int, property_val: float, deposit: float):
        """

        :param start: string fmt of date 'dd-mm-yyyy'
        :param periods: number of months in mortgage, ie 30Y mortgage is 30x12
        :param property_val: property value
        :param deposit: Either int of actual deposit eg. 50000 or float for percentage eg. 0.10
        """
        self._property_val = property_val
        self._deposit = deposit
        self._loan = self._property_val - self._deposit
        self._headers = ['LoanValue']
        self._flows_table = self._init_flowstable(start, periods)

    def _init_flowstable(self, start: dt.date, periods: int) -> pd.DataFrame:
        schedule = pd.date_range(start, periods=periods, freq='M')
        return pd.DataFrame(index=schedule, columns=self._headers)

    def _init_deposit(self, deposit: float) -> float:
        """
        Determine what the value of the deposit is
        :param deposit: Either int of actual deposit eg. 50000 or float for percentage eg. 0.10
        :return: Actual deposit value
        """
        if deposit.is_integer():
            return deposit
        else:
            return deposit * self._property_val

    @property
    def flows_table(self):
        return self._flows_table


if __name__ == '__main__':
    calc = Mortgage(dt.date(2020, 9, 30), 10 * 12)
