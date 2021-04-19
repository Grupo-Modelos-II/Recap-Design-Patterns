from abc import ABCMeta,abstractmethod

class RouteStrategy(metaclass=ABCMeta):

    @abstractmethod
    def _upload(self, data):
        pass

    @abstractmethod
    def _clean(self):
        pass

    @abstractmethod
    def _filtter(self, team):
        pass

    @abstractmethod
    def results(self):
        pass