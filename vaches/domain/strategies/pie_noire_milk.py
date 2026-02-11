from vaches.domain.strategies.protocols import rumination_strategy
from vaches.domain.errors.pie_noire import PieNoire
from vaches.domain.errors.Vache import Vache


class PieNoireMilkStrategy(rumination_strategy.RuminationStrategy):
    def __init__(self):
        self.coefficient_lait = {
            "HERBE": 1.0,
            "FOIN": 0.8,
            "CEREALES": 1.2,
            "MARGUERITE": 1.1,
        }

    def calculer_lait(self, vache: "Vache", panse_avant: float) -> float:
        lait = Vache.RENDEMENT_LAIT * panse_avant
        somme = 0
        for nourriture, quantite in vache.ration.items():
            somme += quantite * self.coefficient_lait.get(nourriture, 0)
        lait += somme
        return lait

    def stocker_lait(self, vache: "Vache", lait: float) -> None:
        vache._lait_disponible += lait
        vache._lait_total_produit += lait
        return

    def post_rumination(self, vache: "Vache", panse_avant: float, lait: float) -> None:
        vache.ration.clear()
        return


strategy: rumination_strategy.RuminationStrategy = PieNoireMilkStrategy()