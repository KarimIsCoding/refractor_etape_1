from vaches.domain.errors.exception.InvalidVacheException import InvalidVacheException
from vaches.domain.nourriture.TypeNourriture import TypeNourriture


class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1200.0
    PANSE_MAX = 200.0
    RENDEMENT_RUMINATION = 0.25

    def __init__(self, petit_nom: str, poids: float, age: int):
        if not petit_nom.strip():
            raise InvalidVacheException("Le petit nom ne peut pas être vide")
        if not (0 <= age <= Vache.AGE_MAX):
            raise InvalidVacheException(f"L'âge doit être entre 0 et {Vache.AGE_MAX}")
        if poids < 0 or poids > Vache.POIDS_MAX:
            raise InvalidVacheException(f"Le poids doit être entre 0 et {Vache.POIDS_MAX}")

        self.petit_nom = petit_nom
        self.age = age
        self.poids = poids
        self.panse = 0.0

    def ruminer(self):
        if self.panse <= 0:
            raise InvalidVacheException("La rumination est impossible, la panse est vide.")

        panse_avant = self.panse
        gain = Vache.RENDEMENT_RUMINATION * panse_avant
        self.poids += gain
        self.panse = 0
        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)
        self._post_rumination(panse_avant, lait)
        return lait

    def _calculer_lait(self, panse_avant: float) -> float:
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes.")

    def _stocker_lait(self, lait: float):
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes.")

    def _post_rumination(self, panse_avant: float, lait: float):
        pass
