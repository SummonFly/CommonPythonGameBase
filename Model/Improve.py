from abc import ABC, abstractmethod


class IImproveable(ABC):
    def Improve(self, improvement):
        improvement.Accept(self)


class IImprovement(ABC):
    @abstractmethod
    def Accept(self, obj: IImproveable):
        pass

