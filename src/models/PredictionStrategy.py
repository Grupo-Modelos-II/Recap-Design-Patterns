from .RouteStrategy import RouteStrategy
from pandas.io.parsers import read_csv
from models.PredictFacade import PrectFacade

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

    def _filter(self,teams):
        self._predict_facate = PrectFacade(self._csv, teams[0], teams[1])

    def results(self,data_set,teams):
        self._upload(data_set)
        self._clean()
        self._filter(teams)
        return self._results
