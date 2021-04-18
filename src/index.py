#!/bin/python

from models.AnalisisStrategy import AnalisisStrategy

def main() -> None:
    app: AnalisisStrategy = AnalisisStrategy()
    app.upload('/home/jema/Git/GitHub/Grupales/Recap-Design-Patterns/docs/LeagueofLegends.csv')
    app.filtter('TSM')
    app.results()

if __name__ == '__main__':
    main()