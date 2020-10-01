from v2.interest_calc import *
from v2.mortgage import *


class TestALL:
    property_val = 600000
    calc_mortgage = Mortgage(dt.date(2020, 9, 30), 10 * 12, property_val, property_val * 0.1)
    calc_interest = InterestRatesCalculator(calc_mortgage.flows_table, 0.0275, 2, property_val * 0.9)

    def test_rates(self):
        rates = self.calc_interest.build_rates()
        assert rates == pd.Series([0.00275 * 0.9 * 600000, 0.00275 * 0.9 * 600000],
                                                  [dt.date(2020, 9, 30), dt.date(2020, 10, 31)])
