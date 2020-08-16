from datetime import date
from typing import List
from typing import Tuple
from copy import deepcopy


class StampDuty:
    def __init__(self, property_val: float, valdate: date, thresholds: List[Tuple[float, float, float]] = None,
                 london: bool = True):
        self._property_val = property_val
        self._valdate = valdate
        self._london = london
        self._thresholds = self.define_thresholds(thresholds)

    # TODO Finish me
    def define_thresholds(self, thresholds: List[Tuple[float, float, float]] = None) -> List[
        Tuple[float, float, float]]:
        if thresholds is None and self._valdate < date(2021, 4, 1):
            if self._london:
                return [(1500000.0, 9999999999.0, 0.12),
                        (925000.0, 1500000.0, 0.1),
                        (500000.0, 925000.0, 0.05),
                        (0.0, 500000.0, 0.0)]
            else:
                return [(0.0, 0.0, 0.0)]

        elif thresholds is None and self._valdate > date(2021, 4, 1):
            if self._london:
                return [(0.0, 0.0, 0.0)]
            else:
                return [(0.0, 0.0, 0.0)]

        else:
            return thresholds

    def cost(self):
        cost = 0.0
        w_val = self._property_val
        for i in self._thresholds:
            if all([w_val > i[0], w_val <= i[1]]):
                diff = w_val - i[0]
                cost += (diff * i[2])
                w_val -= w_val - diff
        return cost
