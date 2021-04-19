from .RouteStrategy import RouteStrategy
from ast import literal_eval

class AnalisisStrategy(RouteStrategy):

    def __init__(self):
        RouteStrategy.__init__(self)

    def filtter(self, team):

        data = self._csv[(self._csv["blueTeamTag"] == team) | (self._csv["redTeamTag"] == team)]

        total_won = 0
        time_average = 0
        total_inhibs = 0
        total_dragons = 0
        total_towers = 0
        total_barons = 0
        total_heralds = 0
        total = 0
        count = 1

        content_time = []
        content_performance = []

        for index, row in data.iterrows():
            isBlueTeam = row["blueTeamTag"] == team
            won = int(row["bResult" if isBlueTeam else "rResult"])

            if won:
                count += 1
                time = row["gamelength"]
                inhibs = len(literal_eval(row["bInhibs" if isBlueTeam else "rInhibs"]))
                dragons = len(literal_eval(row["bDragons" if isBlueTeam else "rDragons"]))
                towers = len(literal_eval(row["bTowers" if isBlueTeam else "rTowers"]))
                heralds = len(literal_eval(row["bHeralds" if isBlueTeam else "rHeralds"]))
                barons = len(literal_eval(row["bBarons" if isBlueTeam else "rBarons"]))
                time_average += time
                total_inhibs += inhibs
                total_dragons += dragons
                total_towers += towers
                total_barons += barons
                total_heralds += heralds
                total_won += won
                total = .15*dragons + .3*towers + .3*inhibs + .1*heralds + .15*barons
                content_time.append(time)
                content_performance.append(total)
        
        content = {"time": content_time, "performance": content_performance}
        time_average /= count
        data = {"inhibs": total_inhibs, "dragons": total_dragons, "won": total_won, "average": time_average}
        self._results = {"Results": data, "Graph": content}


    def results(self):
        return self._results