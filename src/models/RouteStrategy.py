from abc import ABCMeta,abstractmethod

from pandas import read_csv, DataFrame

class RouteStrategy(metaclass=ABCMeta):

    def upload(self, data):
        self._csv: DataFrame = read_csv(data)
        self.clean()

    def clean(self):
        self._csv = self._csv.filter([
            "blueTeamTag",
            "redTeamTag",
            "gamelength",
            "bInhibs",
            "rInhibs",
            "rDragons",
            "bDragons",
            "rResult",
            "bResult"
        ])

    @abstractmethod
    def filtter(self, team):
        pass

    @abstractmethod
    def results(self):
        pass

    @property
    def csv(self):
        return self._csv