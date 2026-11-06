from composant import Composant


class Composite(Composant):
    def __init__(self, nom: str):
        super().__init__(nom)
        self.composants = []

    def ajouter(self, composant: Composant):
        self.composants.append(composant)

    def capacite_totale(self):
        return sum(composant.capacite_totale() for composant in self.composants)

    def nb_spectacles(self):
        return sum(composant.nb_spectacles() for composant in self.composants)

    def afficher(self, prefixe: str = ""):
        print(f"{prefixe}{self.nom}")
        for composant in self.composants:
            composant.afficher(f"{prefixe}  ")


class Spectacle(Composite):
    def __init__(self, nom: str, capacite: int):
        super().__init__(nom)
        self.capacite = capacite

    def capacite_totale(self):
        return self.capacite

    def nb_spectacles(self):
        return 1


class Festival(Composite):
    def __init__(self, nom: str):
        super().__init__(nom)


class Scene(Composite):
    def __init__(self, nom: str):
        super().__init__(nom)


class Journee(Composite):
    def __init__(self, nom: str):
        super().__init__(nom)