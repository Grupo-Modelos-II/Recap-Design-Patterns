from .RouteStrategy import RouteStrategy
from ast import literal_eval

class AnalisisStrategy(RouteStrategy):

    def filtter(self, team):
        self._csv = self._csv[(self._csv["blueTeamTag"] == team) | (self._csv["redTeamTag"] == team)]

        timeAverage = 0
        totalInhibs = 0
        totalDragons = 0
        totalWon = 0
        count = 0

        for index, row in self._csv.iterrows():
            isBlueTeam = row["blueTeamTag"] == team
            timeAverage += row["gamelength"]
            totalInhibs += len(literal_eval(row["bInhibs" if isBlueTeam else "rInhibs"]))
            totalDragons += len(literal_eval(row["bDragons" if isBlueTeam else "rDragons"]))
            totalWon += row["bResult" if isBlueTeam else "rResult"]
            count += 1
        
        timeAverage /= count
        self._results = {"Total Inhibidores": totalInhibs, "Total Dragones": totalDragons, "Partidas Ganadas": totalWon, "Tiempo Promedio": timeAverage}
            

    def results(self):
        return self._results