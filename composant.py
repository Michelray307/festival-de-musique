from abc import ABC, abstractmethod

class Composant(ABC):
    def __init__(self, nom: str):
        self.nom = nom


    @abstractmethod
    def capacite_totale(self):
        pass
    
    @abstractmethod
    def nb_spectacles(self):
        pass

    @abstractmethod
    def afficher(self, prefixe: str = ""):
        pass