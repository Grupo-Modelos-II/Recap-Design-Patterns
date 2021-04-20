import pandas as pd
from TeamModel import Team
from MatchModel import Match

class PrectFacade:

	def __init__(self, data, teamA, teamB):
		self._csv = data
		self._teamA = teamA
		self._teamB = teamB
		self._teamAInfo = none
		self._teamBInfo = none
		self._match = none

	def execute(self):
		self._getWinrate()

		rateA = self._teamAInfo.getWinrateLadoA() + self._teamAInfo.getWinrate()*2
		rateB = self._teamBInfo.getWinrateLadoB() + self._teamBInfo.getWinrate()*2

		if self._match != none:
			rateA = self._match.getWinrates[0]*3 + rateA
			rateB = self._match.getWinrates[0]*3 + rateA

		return [self._teamA, self._teamB, rateA*100/(rateA + rateB),100 - (rateA*100/(rateA + rateB))]

	def _getWinrate(self):
		winsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 1)].count()
		defeatsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 0)].count()
		winsLadoR = self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['rResult'] == 1)].count()
		defeatsLadoR = self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['rResult'] == 0)].count()
		self._teamAInfo = Team(self._teamA, winsLadoA, winsLadoR, defeatsLadoA, defeatsLadoR)

		winsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamB) & (self._csv['bResult'] == 1)].count()
		defeatsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamB) & (self._csv['bResult'] == 0)].count()
		winsLadoR = self._csv['League'][(self._csv['redTeamTag'] == self._teamB) & (self._csv['rResult'] == 1)].count()
		defeatsLadoR = self._csv['League'][(self._csv['redTeamTag'] == self._teamB) & (self._csv['rResult'] == 0)].count()
		self._teamBInfo = Team(self._teamB, winsLadoA, winsLadoR, defeatsLadoA, defeatsLadoR)

	def _infoMatch(self):
		winsTeamA = 0
		winsTeamB = 0

		winsTeamA = self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['blueTeamTag'] == self._teamB) & (self._csv['rResult'] == 1)].count()
		winsTeamA += self._csv['League'][(self._csv['redTeamTag'] == self._teamB) & (self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 1)].count()

		winsTeamB = self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['blueTeamTag'] == self._teamB) & (self._csv['bResult'] == 1)].count()
		winsTeamB += self._csv['League'][(self._csv['redTeamTag'] == self._teamB) & (self._csv['blueTeamTag'] == self._teamA) & (self._csv['rResult'] == 1)].count()

		if(winsTeamA != 0 & winsTeamB != 0):
			self._match = Match(winsTeamA, winsTeamB)