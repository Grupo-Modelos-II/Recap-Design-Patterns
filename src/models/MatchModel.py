class Match:
	def __init__(self, winsA, winsB):
		self._winsA = winsA
		self._winsB = winsB

	def getWinrates(self):
		return [int(self._winsA*100/(self._winsA+self._winsB)), 100 - int(self._winsA*100/(self._winsA+self._winsB))]
		