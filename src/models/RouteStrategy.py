from abc import ABCMeta,abstractmethod
from pandas import read_csv

class RouteStrategy(metaclass=ABCMeta):

    def __init__(self):
        self._csv = None

    def upload(self, data):
        self._csv = read_csv(data)
        self.clean()

    def clean(self):
        self._csv.fillna('NAN')
        self._csv = self.csv.filter([
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

    def get_team_list(self):
        array = []
        for index, obj in self._csv.iterrows():
            (name_blue, name_red) = obj.filter(["blueTeamTag", "redTeamTag"])
            # array.append(name_blue)
            if name_blue not in array:
                array.append(name_blue)
        return array