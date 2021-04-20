class Match:
	def __init__(winsA, winsB):
		self._winsA = winsA
		self._winsB = winsB

	def getWinrates():
		return [int(self._winsA*100/(self._winsA+self._winsB)), 100 - int(self._winsA*100/(self._winsA+self._winsB))]
		