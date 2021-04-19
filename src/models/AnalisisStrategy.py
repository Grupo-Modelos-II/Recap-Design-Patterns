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

        content_time_won = []
        content_performance_won = []

        content_time_lose = []
        content_performance_lose = []

        for index, row in data.iterrows():
            isBlueTeam = row["blueTeamTag"] == team
            won = int(row["bResult" if isBlueTeam else "rResult"])

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
            total = .15*dragons + .3*towers + .3*inhibs + .1*heralds + .15*barons
            if won:
                total_won += won
                content_time_won.append(time)
                content_performance_won.append(total)
            else:
                content_time_lose.append(time)
                content_performance_lose.append(total)
        
        content_won = {"time": content_time_won, "performance": content_performance_won}
        content_lose = {"time": content_time_lose, "performance": content_performance_lose}
        time_average /= count
        data = {"inhibs": total_inhibs, "dragons": total_dragons, "won": total_won, "average": time_average}
        self._results = {"Results": data, "Graph": {"won": content_won, "lose": content_lose}}


    def results(self):
        return self._results