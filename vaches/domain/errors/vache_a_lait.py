from vaches.domain.errors.exception.InvalidVacheException import InvalidVacheException

class VacheALait:
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    _laitDisponible : float
    _laitTotalProduit : float
    _laitTotalTraite : float

    def __init__(self, petit_nom: str, poids: float, age: int):
        self.petit_nom = petit_nom
        self.poids = poids
        self.age = age
        self.panse = 0.0
        self.id = 1

    def getLait_disponible(self):
        return self._laitDisponible

    def getLaitTotalProduit(self):
        return self._laitTotalProduit

    def getLaitTotalTraite(self):
        return self._laitTotalTraite

    def __str__(self):
        return "La vache à lait a "+{self.getLait_disponible}+" de lait disponible, "+
        {self.getLaitTotalProduit}+" produit et enfin "+{self.getLaitTotalTraite}+" de lait traitée."

    def ruminer(self):
        if self.panse <= 0:
            raise InvalidVacheException("Erreur")

        gain = Vache.RENDEMENT_LAIT * self.panse
        self.poids += gain
        self.panse = 0.0

    def traire(self):
        pass