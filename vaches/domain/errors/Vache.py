from vaches.domain.errors.exception import InvalidVacheException

class Vache:
    AGE_MAX = 25
    AGE_MINI_NAISSANCE = 0
    POIDS_MAX = 1000.0
    POIDS_MIN_PANSE = 2.0
    PANSE_MAX = 50.0
    RENDEMENT_RUMINATION = 0.25
    _NEXT_ID = 1

    def __init__(self, petit_nom: str, poids: float, age: int):
        if not petit_nom or petit_nom.strip() == "":
            raise InvalidVacheException("Le nom ne peut pas etre vide")

        if age < Vache.AGE_MINI_NAISSANCE or age > Vache.AGE_MAX:
            raise InvalidVacheException("L'age doit être entre 0 et 25 ans")

        if poids < Vache.POIDS_MIN_PANSE or poids > Vache.POIDS_MAX:
            raise InvalidVacheException("Erreur dans le poids")

        self.petit_nom = petit_nom
        self.poids = poids
        self.age = age
        self.panse = 0.0

    def brouter(self, quantite: float, nourriture=None):
        if nourriture is not None:
            raise InvalidVacheException("La vache ne peut pas brouter de nourriture.")

        if quantite <= 0:
            raise InvalidVacheException("La quantite doit etre positive.")

        if self.panse + quantite > Vache.PANSE_MAX:
            raise InvalidVacheException("Erreur sur la panse")

        self.panse += quantite

    def ruminer(self):
        if self.panse <= 0:
            raise InvalidVacheException("Erreur")

        gain = Vache.RENDEMENT_RUMINATION * self.panse
        self.poids += gain
        self.panse = 0.0

    def vieillir(self):
        if self.age >= Vache.AGE_MAX:
            raise InvalidVacheException('L age maximum est atteint.')

        self.age += 1
