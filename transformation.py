from abc import ABC, abstractmethod

class Transformation(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def application(self,jeu_de_donnees):
        pass