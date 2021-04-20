class Team:
	def __init__(self, name, winsLadoA, winsLadoR, defeatsLadoA, defeatsLadoR):
		self._name = name
		self._winsLadoA = winsLadoA
		self._defeatsLadoA = defeatsLadoA
		self._winsLadoR = winsLadoR
		self._defeatsLadoR = defeatsLadoR
		self._winrateLadoA = self._winsLadoA*100/(self._winsLadoA+self._defeatsLadoA)
		self._winrateLadoB = self._winsLadoR*100/(self._winsLadoR+self._defeatsLadoR)
		self._winrate = (self._winsLadoA+self._winsLadoR)*100/(self._winsLadoA+self._winsLadoR+self._defeatsLadoA+self._defeatsLadoR)

	def getWinrateLadoA(self):
		return self._winrateLadoA

	def getWinrateLadoB(self):
		return self._winrateLadoB

	def getWinrate(self):
		return self._winrate