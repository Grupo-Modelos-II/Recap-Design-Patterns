from abc import ABC, abstractmethod, abstractproperty

class BuildGUI(ABC):

    @abstractmethod
    def _buildPage1(self):
        pass

    @abstractmethod
    def _buildPage2(self):
        pass

    @abstractmethod
    def _handleAnalysis(self):
        pass

    @abstractmethod
    def _handlePrediction(self):
        pass

    @abstractmethod
    def _handleEvents(self):
        pass

    @abstractmethod
    def getGUI(self):
        pass

