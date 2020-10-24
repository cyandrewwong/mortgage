import pandas as pd


class MortgagePayments:
    def __init__(self, in_df: pd.DataFrame, loan_value: float, fixedrate: float, fixedperiods: int,
                 monthly_payment: float):
        self._df = in_df
        self._loan_value = loan_value
        self._fixedrate = fixedrate
        self._fixedperiods = fixedperiods
        self._monthly_payment = monthly_payment

    def build_schedule(self) -> pd.DataFrame:
        self._build_rates()
        self._build_loan_schedule()
        return self._df

    # TODO: Implement Floating rates/ Currently using dummy float rate
    def _build_rates(self) -> None:
        fixed_end = self._df.index[0] + pd.DateOffset(months=2)
        fixedinterest_df = self._df[self._df.index <= fixed_end]
        fixedinterest_df['M_Annual_InterestRate'] = self._fixedrate
        self._df['M_Annual_InterestRate'] = fixedinterest_df['M_Annual_InterestRate']

        dummy_floatrate = 0.03
        self._df['M_Annual_InterestRate'].loc[self._df['M_Annual_InterestRate'].isnull()] = dummy_floatrate
        self._df['M_InterestRate'] = self._df['M_Annual_InterestRate'] / 12

    # TODO: Possible Change Repyaments/Overpayments
    def _build_loan_schedule(self):
        loan_value = []
        rates = self._df['M_InterestRate'].astype(float).tolist()

        for idx, rate in enumerate(rates, 0):
            if idx == 0:
                interest = self._loan_value * rate
                loan_value.append(self._loan_value - self._monthly_payment + interest)
            else:
                interest = loan_value[idx - 1] * rate
                loan_value.append(loan_value[idx - 1] - self._monthly_payment + interest)
        self._df['M_Repayments'] = self._monthly_payment
        self._df['M_LoanValue'] = loan_value

        self._df['LTV'] = self._df['M_LoanValue'] / 600000

        print()


class EquityLoanPayments:
    pass
