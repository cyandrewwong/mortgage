import datetime as dt
import pandas as pd
from typing import *
from v2.interest_calc import MortgagePayments


class Mortgage:
    def __init__(self, start: dt.date, periods: int, property_val: float, deposit: float, equity_loan: float,  fixed_rate: float,
                 fixed_periods: int):
        """

        :param start: string fmt of date 'dd-mm-yyyy'
        :param periods: number of months in mortgage, ie 30Y mortgage is 30x12
        :param property_val: property value
        :param deposit: Either int of actual deposit eg. 50000 or float for percentage eg. 0.10
        """
        self._property_val = property_val
        self._deposit = deposit
        self._equity_loan = equity_loan
        self._fixed_rate = fixed_rate
        self._fixed_periods = fixed_periods
        self._loan = self._property_val - self._deposit
        self._headers = ['CashFlow']
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

    def generate_flows(self) -> None:
        loan_val = self._property_val - self._deposit - self._equity_loan
        calculator = MortgagePayments(self._flows_table, loan_val, self._fixed_rate, self._fixed_periods, 1550)
        self._flows_table = calculator.build_schedule()


if __name__ == '__main__':
    date_ = dt.date(2020, 9, 30)
    periods_ = 30 * 12
    property_val_ = 600000.0
    deposit_ = 0.05
    equity_loan_ = property_val_ * 0.4
    fixed_rate_ = 0.02
    fixed_periods_ = 24

    calc = Mortgage(date_, periods_, property_val_, deposit_, equity_loan_, fixed_rate_, fixed_periods_)
    calc.generate_flows()
    print()
