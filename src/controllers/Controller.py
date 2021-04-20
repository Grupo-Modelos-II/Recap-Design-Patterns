from models.AnalisisStrategy import AnalisisStrategy
from models.PredictionStrategy import PredictionStrategy
from functions import functions as f

class Controller:

    def __init__(self):
        self._strategy = None

    def create_analisis(self):
        self._strategy = AnalisisStrategy()

    def create_prediction(self):
        self._strategy = PredictionStrategy()

    def exec_strategy(self,*teams):
        return self._strategy.results(f.get_csv(),teams)


# AnalisisStrategy(Path('docs','LeagueofLegends.csv'))