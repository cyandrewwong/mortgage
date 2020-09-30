from typing import *
import datetime as dt


class MortgageFees:
    def __init__(self):
        self.booking_fee = None
        self.arrangement_fee = None
        self.transaction_fee = None
        self.mortgage_val_fee = None

    def total(self):
        return self.booking_fee + self.arrangement_fee + self.transaction_fee + self.mortgage_val_fee


class Scenario:
    def __init__(self, valdate: dt.date, property_val: float, deposit: Any, valuation_fee: float, surveryor_fee: float,
                 legal_fee: float, removal_cost: float, mortgage_fees: MortgageFees):
        self._valdate = valdate
        self._property_val = property_val
        self._deposit = deposit
        self._valuation_fee = valuation_fee
        self._surveyor_fee = surveryor_fee
        self._legal_fee = legal_fee
        self._removal_cost = removal_cost
        self._mortgage_fees = mortgage_fees

    @property
    def valdate(self):
        return self._valdate

    @property
    def property_val(self):
        return self._property_val

    @property
    def deposit(self):
        return self._deposit
