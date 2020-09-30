from v1.stampduty import StampDuty
from v1.curve import Curve
from v1.collection import CurveCollection
from v1.calculator_mortgage import *
from datetime import date


class TestStampDuty:
    def test_cost(self):
        stampduty = StampDuty(760000, date.today())
        assert stampduty.cost() == 13000

    def test_cost2(self):
        stampduty = StampDuty(550000, date.today())
        assert stampduty.cost() == 2500


class TestMortgageSchedule:
    def test_schedule(self):
        scheduler = MortgageSchedule(0.1, 3, 35)
        sched = scheduler.fixed_schedule(date(2020, 8, 30), 50000)
        assert sched == pd.Series()


class TestMortgage:
    # TODO Finish me
    def test_scenario(self):
        crv_salary = Curve({"22/08/2016": 38500,
                            "22/02/2018": 45500,
                            "01/01/2020": 65000,
                            "01/04/2021": 70000})
        crv_inflation = Curve({"22/08/2016": 0.01,
                               "22/02/2018": 0.01,
                               "01/01/2020": 0.01,
                               "01/04/2021": 0.01})

        crv_collection = CurveCollection({'SALARY': crv_inflation,
                                          'INFLATION': crv_inflation})
        mortgage = Mortgage(Scenario(date.today(), 575000, '10%'))
