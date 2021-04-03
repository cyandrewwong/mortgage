from abc import ABC, abstractmethod
from typing import Any


class PData(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def data(self):
        pass


def to_lists(data: Any):
    pass
