from abc import ABC, abstractmethod, abstractproperty

class BuildGUI(ABC):

    @abstractmethod
    def buildPage1(self):
        pass

    @abstractmethod
    def buildPage2(self):
        pass

    @abstractmethod
    def handleAnalisis(self):
        pass

    @abstractmethod
    def handleAnalisis(self):
        pass

    @abstractmethod
    def handlePrediction(self):
        pass

    @abstractmethod
    def handleEvents(self):
        pass

    @abstractmethod
    def getGUI(self):
        pass

