import pandas as pd

class PrectFacade():

	def __init__(self, data: DataFrame, teamA: string, teamB: string):
		self._csv = data
		self._teamA = teamA
		self._teamB = teamB
		self._teamAInfo = []
		self._teamAInfo = []

	def execute():
		getWinrate()
		return [self._teamAInfo[0]+self._teamAInfo[1], 
		self._teamAInfo[2]+self._teamAInfo[3], 
		(self._teamAInfo[0]+self._teamAInfo[2])*100/(self._teamAInfo[0]+self._teamAInfo[1]+self._teamAInfo[2]+self._teamAInfo[3])]


	def getWinrate():
		winsLadoA = self._csv['League'][(data['blueTeamTag'] == self._teamA) & (data['bResult'] == 1)].count()
		defeatsLadoA = self._csv['League'][(data['blueTeamTag'] == self._teamA) & (data['bResult'] == 0)].count()
		winsLadoR = self._csv['League'][data['League'][(data['redTeamTag'] == self._teamA) & (data['rResult'] == 1)].count()
		defeatsLadoR = self._csv['League'][data['League'][(data['redTeamTag'] == self._teamA) & (data['rResult'] == 0)].count()
		self._teamAInfo.appens(winsLadoA)
		self._teamAInfo.appens(defeatsLadoA)
		self._teamAInfo.appens(winsLadoR)
		self._teamAInfo.appens(defeatsLadoR)
