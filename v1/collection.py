from v1.curve import Curve
from typing import *


class Collection:
    def __init__(self, data: Dict[str, Any] = None):
        self._data = data

    @property
    def data(self):
        return self._data


class CurveCollection(Collection):
    def __init__(self, data: Dict[str, Curve] = None):
        super(CurveCollection, self).__init__(data)

    def curve(self, key: str) -> Union[Curve, str]:
        try:
            return self.data[key]
        except KeyError:
            return 'No curve named: ' + key
