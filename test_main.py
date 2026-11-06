import unittest

from composite import Festival, Journee, Scene, Spectacle
from feuille import Artiste


class FestivalTest(unittest.TestCase):
    def test_festival_capacity_and_show_count(self):
        arcade_fire = Artiste("Arcade Fire")
        tame_impala = Artiste("Tame Impala")
        loud = Artiste("Loud")
        alaclair = Artiste("Alaclair Ensemble")

        spectacle_1 = Spectacle("21h00", capacite=50_000)
        spectacle_1.ajouter(arcade_fire)

        spectacle_2 = Spectacle("18h00", capacite=50_000)
        spectacle_2.ajouter(tame_impala)

        scene_principale = Scene("Scène principale")
        scene_principale.ajouter(spectacle_1)
        scene_principale.ajouter(spectacle_2)

        spectacle_3 = Spectacle("20h00", capacite=1_500)
        spectacle_3.ajouter(loud)
        spectacle_3.ajouter(alaclair)

        scene_emergente = Scene("Scène émergente")
        scene_emergente.ajouter(spectacle_3)

        vendredi = Journee("Vendredi 1er août")
        vendredi.ajouter(scene_principale)
        vendredi.ajouter(scene_emergente)

        osheaga = Festival("Osheaga 2025")
        osheaga.ajouter(vendredi)

        self.assertEqual(osheaga.capacite_totale(), 101_500)
        self.assertEqual(osheaga.nb_spectacles(), 3)


if __name__ == "__main__":
    unittest.main()
