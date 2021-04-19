from models.AnalisisStrategy import AnalisisStrategy

class Controller:

    def __init__(self):
        self._strategy = AnalisisStrategy()
        self._strategy.upload('/home/jema/Git/GitHub/Grupales/Recap-Design-Patterns/docs/LeagueofLegends.csv')
        # self._strategy.upload('/home/user/Documentos/Recap-Design-Patterns/docs/LeagueofLegends.csv')

    def select_strategy(self,strategy):
        self._strategy = strategy

    def exec_strategy(self,team_name):
        self._strategy.filtter(team_name)
        return self._strategy.results()

    def get_team_list(self):
        return self._strategy.get_team_list()