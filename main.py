from composite import Spectacle, Festival, Scene, Journee
from feuille import Artiste

# Artistes
arcade_fire = Artiste("Arcade Fire")
tame_impala = Artiste("Tame Impala")
loud = Artiste("Loud")
alaclair = Artiste("Alaclair Ensemble")

# Spectacles (sur une scène de 50 000 places)
spectacle_1 = Spectacle("21h00", capacite=50_000)
spectacle_1.ajouter(arcade_fire)

spectacle_2 = Spectacle("18h00", capacite=50_000)
spectacle_2.ajouter(tame_impala)

# Scène principale — journée vendredi
scene_principale = Scene("Scène principale")
scene_principale.ajouter(spectacle_1)
scene_principale.ajouter(spectacle_2)

# Scène émergente (1 500 places)
spectacle_3 = Spectacle("20h00", capacite=1_500)
spectacle_3.ajouter(loud)
spectacle_3.ajouter(alaclair)  # ← deux artistes pour un même spectacle

scene_emergente = Scene("Scène émergente")
scene_emergente.ajouter(spectacle_3)

vendredi = Journee("Vendredi 1er août")
vendredi.ajouter(scene_principale)
vendredi.ajouter(scene_emergente)

osheaga = Festival("Osheaga 2025")
osheaga.ajouter(vendredi)

print(f"Capacité totale : {osheaga.capacite_totale():,} spectateurs")
print(f"Nombre de spectacles : {osheaga.nb_spectacles()}")
osheaga.afficher()