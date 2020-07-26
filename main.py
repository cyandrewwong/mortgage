from typing import *
from salary_schedules import *
import datetime as dt


class MortgageCalculator:
    def __init__(self, valdate: dt.date):
        self._valdate = valdate
