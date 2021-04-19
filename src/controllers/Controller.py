from models.AnalisisStrategy import AnalisisStrategy
from pathlib import Path

class Controller:

    def __init__(self):
        self._strategy = None

    def create_analisis(self, path):
        self._strategy = AnalisisStrategy()

        def create_analisis(self, path):
        self._strategy = AnalisisStrategy(Path('docs','LeagueofLegends.csv'))

    def exec_strategy(self,team_name):
        return self._strategy.results()

    def get_team_list(self):
        return self._strategy.get_team_list()

"""

    def get_team_list(self):
        array = []
        for index, obj in self._csv.iterrows():
            (name_blue, name_red) = obj.filter(["blueTeamTag", "redTeamTag"])
            # array.append(name_blue)
            if name_blue not in array:
                array.append(name_blue)
        return array

"""

# AnalisisStrategy(Path('docs','LeagueofLegends.csv'))