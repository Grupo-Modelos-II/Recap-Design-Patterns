from abc import ABCMeta,abstractmethod

from pandas import read_csv, DataFrame

class RouteStrategy(metaclass=ABCMeta):

    def upload(self, data: str) -> None:
        self._csv: DataFrame = read_csv(data)

    @abstractmethod
    def clean(self) -> None:
        pass

    @abstractmethod
    def filtter(self) -> None:
        pass

    @abstractmethod
    def results(self) -> None:
        pass

    @property
    def csv(self) -> DataFrame:
        return self._csv