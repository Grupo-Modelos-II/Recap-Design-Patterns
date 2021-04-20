from pathlib import Path
from pandas.io.parsers import read_csv

def get_csv():
    return read_csv(Path('docs','LeagueofLegends.csv'))

def get_team_list():
    array = []
    for index, obj in get_csv().iterrows():
        (name_blue, name_red) = obj.filter(["blueTeamTag", "redTeamTag"])
            # array.append(name_blue)
        if name_blue not in array:
            array.append(name_blue)
    return array