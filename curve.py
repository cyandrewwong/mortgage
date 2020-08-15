from typing import *
import datetime as dt


class Curve:
    def __init__(self, schedule: Dict[str, float]):
        self._base = Curve.load_schedule(schedule)

    @property
    def base(self):
        return self._base

    @staticmethod
    def load_schedule(schedule: Dict[str, float]) -> Dict[dt.datetime, float]:
        new_schedule = {}
        for key, value in schedule.items():
            new_schedule[dt.datetime.strptime(key, "%d/%m/%Y")] = value
        return new_schedule

    def rate(self, term: Any) -> float:
        if isinstance(term, str):
            curr_term = dt.datetime.strptime(term, "%d/%m/%Y")
        elif isinstance(term, dt.date):
            curr_term = term
        else:
            curr_term = dt.date(0, 0, 0)

        try:
            return self._base[curr_term]
        except KeyError:
            return self.interpolate(curr_term, "FLAT")

    def interpolate(self, term: dt.datetime, mode: str = "FLAT") -> float:
        if mode == "FLAT":
            return self.interpolate_flat(term)

    def interpolate_flat(self, term_i: dt.date) -> float:
        terms = self._base.keys()
        deltas = {}  # {delta, term}
        for j in terms:
            delta_i = term_i - j
            if delta_i > dt.timedelta(days=0.0):
                deltas[term_i - j] = j
        return self._base[Curve.closest_prev_term(deltas)]

    @staticmethod
    def closest_prev_term(deltas: Dict[dt.timedelta, dt.datetime]) -> dt.datetime:
        mindelta = min(deltas.keys())
        return deltas[mindelta]
