import pandas as pd

class PrectFacade:

	def __init__(self, data, teamA, teamB):
		self._csv = data
		self._teamA = teamA
		self._teamB = teamB
		self.teamAInfo = []
		self._teamBInfo = []

	def execute(self):
		self._getWinrate()
		return [self.teamAInfo[0]+self.teamAInfo[1], 
		self.teamAInfo[2]+self.teamAInfo[3], 
		(self.teamAInfo[0]+self.teamAInfo[2])*100/(self.teamAInfo[0]+self.teamAInfo[1]+self.teamAInfo[2]+self.teamAInfo[3])]


	def _getWinrate(self):
		winsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 1)].count()
		defeatsLadoA = self._csv['League'][(self._csv['blueTeamTag'] == self._teamA) & (self._csv['bResult'] == 0)].count()
		winsLadoR = self._csv['League'][self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['rResult'] == 1)].count()
		#defeatsLadoB = self._csv['League'][(self._csv['redTeamTag'] == self._teamA) & (self._csv['rResult'] == 0)].count()
		self.teamAInfo.append(2)
		self.teamAInfo.append(3)
		self.teamAInfo.append(4)
		self.teamAInfo.append(1)
