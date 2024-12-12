class Routeur:
    def __init__(self, nom, table, voisins):
        self.nom = nom
        self.table = [[nom, nom, 0]]
        self.voisins = []

    def ajoute_voisin(self, voisin):
        self.voisins.append(voisin)

    def affiche_table(self):
        