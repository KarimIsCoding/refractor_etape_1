from vaches.domain.errors.exception.InvalidVacheException import InvalidVacheException
from vaches.domain.nourriture.TypeNourriture import TypeNourriture

class PieNoire:
    nombreTacheNoire : int
    nombreTacheBlanche : int
    COEFFICIENT_LAIT_PAR_NOURRITURE : dict

    def __init__(self, petit_nom: str, poids: float, age: int, nombreTacheBlanche: int, nombreTacheNoire: int):
        self.petit_nom = petit_nom
        self.poids = poids
        self.age = age
        self.panse = 0.0
        self.id = 1
        self.nombreTacheNoire = nombreTacheNoire
        self.nombreTacheBlanche = nombreTacheBlanche

    def getNombreTacheNoire(self):
        return self.nombreTacheNoire

    def getNombreTacheBlanche(self):
        return self.nombreTacheBlanche

    def __str__(self):
        return "La pie noire a "+{self.getNombreTacheBlanche}+" tâches blanches et "
        +{self.nombreTacheNoire}+" tâches noires."

    def brouter(self, quantite: float, nourriture: TypeNourriture = None):
        pass