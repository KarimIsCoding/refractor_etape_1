from vaches.domain.nourriture.TypeNourriture import TypeNourriture
from vaches.domain.errors.Vache import Vache
from vaches.domain.errors.vache_a_lait import VacheALait
from vaches.domain.errors.exception.InvalidVacheException import InvalidVacheException


class PieNoire(VacheALait):
    COEFFICIENT_LAIT_PAR_NOURRITURE = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    def __init__(self, petit_nom: str, poids: float, age: int, nb_taches_blanches: int, nb_taches_noires: int):
        super().__init__(petit_nom, poids, age)

        if not isinstance(nb_taches_blanches, int) or not isinstance(nb_taches_noires, int):
            raise InvalidVacheException("Le nombre de taches doit être un entier.")

        if nb_taches_blanches <= 0 or nb_taches_noires <= 0:
            raise InvalidVacheException("Les nombres de taches doivent être positifs.")

        self.nb_taches_blanches = nb_taches_blanches
        self.nb_taches_noires = nb_taches_noires
        self._ration = {}
        self.lait_disponible = 0.0
        self.lait_total_produit = 0.0

    @property
    def ration(self):
        return self._ration.copy()

    def brouter(self, quantite: float, nourriture: TypeNourriture = None):
        if quantite <= 0:
            raise InvalidVacheException("La quantité de nourriture doit être positive.")
        if self.panse + quantite > Vache.PANSE_MAX:
            raise InvalidVacheException("La panse ne peut pas contenir cette quantité de nourriture.")

        self.panse += quantite
        if nourriture:
            if nourriture not in self._ration:
                self._ration[nourriture] = 0
            self._ration[nourriture] += quantite

    def ruminer(self):
        lait = self._calculer_lait(self.panse)
        self._stocker_lait(lait)
        self._post_rumination(self.panse, lait)
        self.panse = 0

    def _calculer_lait(self, panse_avant: float) -> float:
        lait = VacheALait.RENDEMENT_LAIT * panse_avant
        for nourriture, quantite in self._ration.items():
            coefficient = PieNoire.COEFFICIENT_LAIT_PAR_NOURRITURE.get(nourriture, 0)
            lait += quantite * coefficient
        return lait


    def _stocker_lait(self, lait: float):
        self.lait_disponible += lait
        self.lait_total_produit += lait

    def _post_rumination(self, panse_avant: float, lait: float):
        self._ration.clear()
