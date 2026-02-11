from vaches.domain.errors.exception.InvalidVacheException import InvalidVacheException

class VacheALait:
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0
    PANSE_MAX = 50.0
    _laitDisponible : float
    _laitTotalProduit : float
    _laitTotalTraite : float

    def __init__(self, petitNom: str, poids: float, age: int):
        self.petitNom = petitNom
        self.poids = poids
        self.age = age
        self.panse = 0.0
        self.id = 1
        self._laitDisponible = 0.0
        self._laitTotalProduit = 0.0
        self._laitTotalTraite = 0.0


    def lait_disponible(self):
        return self._laitDisponible

    def lait_total_produit(self):
        return self._laitTotalProduit

    def lait_total_traite(self):
        return self._laitTotalTraite

    def __str__(self):
        return f"La vache à lait a {self.lait_disponible()} de lait disponible, {self.lait_total_produit()} produit et enfin {self.lait_total_traite()} de lait traitée."


    def ruminer(self):
        if self._laitTotalProduit + VacheALait.RENDEMENT_LAIT * self.panse > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Erreur : production de lait dépasse le maximum autorisé")

        if self.panse <= 0:
            raise InvalidVacheException("Erreur : panse vide")

        gain = VacheALait.RENDEMENT_LAIT * self.panse
        self.poids += gain
        self._laitDisponible += gain
        self._laitTotalProduit += gain
        self.panse = 0.0


    def traire(self,litres: float):
        if litres <= 0:
            raise InvalidVacheException("Erreur : quantité de lait à traire doit être positive")
        if litres > self._laitDisponible:
            raise InvalidVacheException("Erreur : quantité de lait à traire dépasse le lait disponible")

        self._laitDisponible -= litres
        self._laitTotalTraite += litres
        return litres

    def brouter(self, quantite: float, nourriture: str = "HERBE"):
        if quantite <= 0:
            raise InvalidVacheException("Erreur : la quantité de nourriture doit être positive")

        if nourriture == "FOIN":
            raise InvalidVacheException("Erreur : le type de nourriture 'FOIN' est interdit")

        nourriture_possible = min(quantite, VacheALait.PANSE_MAX - self.panse)

        self.panse += nourriture_possible

        if self.panse >= VacheALait.PANSE_MAX:
            raise InvalidVacheException("Erreur : panse trop pleine")