"""
A Schedule of date -> value
"""
from v3.structs.data_struct import PData, to_lists
from collections import OrderedDict
from typing import List, Any, Tuple, Iterable
from datetime import date


class Schedule(PData):
    """
    Class for a schedule of date>value
    """
    def __init__(self, schedule: Iterable = None):
        self._data = OrderedDict()
        self._init_data(schedule)

    def _init_data(self, schedule: Iterable) -> None:
        """
        Iterate the schedule object and assign to data as tuple
        :param schedule:
        :return: None
        """
        if schedule is not None:
            for itr in schedule:
                self._validate_data(itr)
                self._data[itr[0]] = itr[1]
            self._order_schedule()

    def _validate_data(self, data) -> None:
        """
        Check whether input schedule is valid shape and type
        :param data: row of schedule data to check
        :return: None
        """
        if not all([len(data) == 2, isinstance(data[0], date), isinstance(data[1], float)]):
            raise ValueError(f'Data {data} is not Length 2 or satisfy [date, float]')

    @property
    def data(self) -> OrderedDict:
        return self._data

    def value(self, dt: date) -> float:
        """
        Get value based on date from Schedule
        :param dt: date querying
        :return: Value from schedule
        """
        return self._data.get(dt)

    def display(self) -> List[List[Any]]:
        """
        Display the data as a standard List[List]
        :return:
        """
        return to_lists(self._data)

    def _order_schedule(self) -> None:
        """
        Reorder the schedule to be in date order
        :return: None
        """
        dates = sorted(list(self._data.keys()))
        newdict = OrderedDict()
        for i in dates:
            newdict[i] = self._data[i]
        self._data = newdict
