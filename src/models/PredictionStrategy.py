from .RouteStrategy import RouteStrategy
from pandas.io.parsers import read_csv

class PredictionStrategy(RouteStrategy):

    _predict_facate: PrectFacade

    def __init__(self, data):
        self._upload(data)

    def _filtter(self, team_a, team_b):
        self._predict_facate = PrectFacade(self._csv, team_a, team_b)

    def _results(self):
        pass