from vaches.domain.strategies.protocols import rumination_strategy
from vaches.domain.errors.Vache import Vache


class StandardMilkStrategy(rumination_strategy.RuminationStrategy):

    def __init__(self):
        self._lait_disponible = 0.0
        self._lait_total_produit = 0.0

    @staticmethod
    def calculer_lait(vache: "Vache", panse_avant: float) -> float:
        lait = Vache.RENDEMENT_LAIT * panse_avant
        return lait

    def stocker_lait(self, vache: "Vache", lait: float) -> None:
        self._lait_disponible += lait
        self._lait_total_produit += lait

    def post_rumination(self, vache: "Vache", panse_avant: float, lait: float) -> None:
        pass


strategy: rumination_strategy.RuminationStrategy = StandardMilkStrategy()