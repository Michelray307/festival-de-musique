from composant import Composant


class Feuille(Composant):
    def __init__(self, nom: str):
        super().__init__(nom)

    def capacite_totale(self):
        return 0

    def nb_spectacles(self):
        return 0


class Artiste(Feuille):
    def __init__(self, nom: str):
        super().__init__(nom)

    def afficher(self, prefixe: str = ""):
        print(f"{prefixe}Artiste: {self.nom}")