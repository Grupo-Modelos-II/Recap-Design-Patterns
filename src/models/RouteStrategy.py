from abc import ABCMeta,abstractmethod

class RouteStrategy(metaclass=ABCMeta):

    @abstractmethod
    def upload(self,data):
        pass

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def filtter(self):
        pass

    @abstractmethod
    def results(self):
        pass