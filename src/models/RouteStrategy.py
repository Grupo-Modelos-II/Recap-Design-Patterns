from abc import ABCMeta,abstractmethod

class RouteStrategy(metaclass=ABCMeta):

    @abstractmethod
    def _upload(self, data):
        pass

    @abstractmethod
    def _clean(self):
        pass

    @abstractmethod
    def _filter(self, teams):
        pass

    @abstractmethod
    def results(self,data_set,teams):
        pass