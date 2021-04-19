from .RouteStrategy import RouteStrategy
from pandas.io.parsers import read_csv
from models import PredictFacade

class PredictionStrategy(RouteStrategy):

    _predict_facate: PrectFacade

    def _upload(self, data_set):
        self._csv = data_set

    def _clean(self):
        self._csv = self.csv.filter([
            "blueTeamTag",
            "redTeamTag",
            "gamelength",
            "bInhibs",
            "rInhibs",
            "rDragons",
            "bDragons",
            "rTowers",
            "bTowers",
            "rBarons",
            "bBarons",
            "rHeralds",
            "bHeralds",
            "rResult",
            "bResult"
        ])

    def _filtter(self,teams):
        self._predict_facate = PrectFacade(self._csv, team_a, team_b)

    def results(self,data_set,teams):
        self._upload(data_set)
        self._clean()
        self._filter(teams)
        return self._results
