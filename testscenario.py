from scenario import Scenario
from curve import Curve
from collection import CurveCollection
import datetime as dt

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


class TestMkt:
    curves = crv_collection


class TestScenario:
    scenario = Scenario(valdate=dt.date.today(), property_val=575000, deposit='10%')
