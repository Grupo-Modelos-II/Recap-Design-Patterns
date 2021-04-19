import pandas as pd

class PrectFacade():

	def __init__(self, data, teamA, teamB):
		self._csv = data
		self._teamA = teamA
		self._teamB = teamB
		self._teamAInfo = []
		self._teamAInfo = []

	def execute(self):
		self._getWinrate()
		return [self._teamAInfo[0]+self._teamAInfo[1], 
		self._teamAInfo[2]+self._teamAInfo[3], 
		(self._teamAInfo[0]+self._teamAInfo[2])*100/(self._teamAInfo[0]+self._teamAInfo[1]+self._teamAInfo[2]+self._teamAInfo[3])]


	def _getWinrate(self):
		winsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 1)].count()
		defeatsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 0)].count()
		winsLadoR = self._csv['League'][self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['rResult'] == 1)].count()
		defeatsLadoR = self._csv['League'][self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['rResult'] == 0)].count()
		self._teamAInfo.append(winsLadoA)
		self._teamAInfo.append(defeatsLadoA)
		self._teamAInfo.append(winsLadoR)
		self._teamAInfo.append(defeatsLadoR)
