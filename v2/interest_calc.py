import pandas as pd
import datetime as dt
import numpy as np


class InterestRatesCalculator:
    def __init__(self, in_df: pd.DataFrame, fixedrate: float, fixedperiods: int):
        self._df = in_df
        self._fixedrate = fixedrate
        self._fixedperiods = fixedperiods

    def build_schedule(self) -> pd.DataFrame:
        self._build_rates()
        self._build_loan_schedule()
        return self._df

    # TODO: Implement Floating rates
    def _build_rates(self) -> None:
        fixed_end = self._df.index[0] + pd.DateOffset(months=2)
        fixedinterest_df = self._df[self._df.index <= fixed_end]
        fixedinterest_df['InterestRate'] = self._fixedrate
        self._df['InterestRate'] = fixedinterest_df['InterestRate']

        dummy_floatrate = 0.03
        self._df['InterestRate'].loc[self._df['InterestRate'].isnull()] = dummy_floatrate


    def _build_loan_schedule(self):
        pass

