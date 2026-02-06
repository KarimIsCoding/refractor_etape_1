from vaches.domain.errors.exception.InvalidVacheException import InvalidVacheException

class VacheALait:
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    _laitDisponible : float
    _laitTotalProduit : float
    _laitTotalTraite : float

    def __init__(self, petit_nom: str, poids: float, age: int):
        self._nom