import pandas as pd
import datetime as dt
import numpy as np


class InterestRatesCalculator:
    def __init__(self, in_df: pd.DataFrame, fixedrate: float, fixedperiods: int, initial_loan: float):
        self._df = in_df
        self._fixedrate = fixedrate
        self._fixedperiods = fixedperiods
        self._init_loan = initial_loan

    def build_rates(self) -> pd.Series:
        fixed_end = self._df.index[0] + pd.DateOffset(months=2)

        fixedinterest = self._df[self._df.index <= fixed_end]
        fixedinterest['InterestRate'] = self._fixedrate
        self._df['InterestRate'] = fixedinterest['InterestRate']
        self._df[self._df['InterestRate'] == np.nan] = 99999

        # self._df[self._df.index > fixed_end]['InterestRate'] = 999999

        return self._df['InterestRate']
