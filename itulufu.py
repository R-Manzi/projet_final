
import random


POINTS_CARTES_JEU = { '3':3,'4':4,'5':5,'6':6,'Q':7,'J':8,'K':9,'7':10,"A":11, }

POiNTS_FIN_PARTIE = { '3':0,'4':0,'5':0,'6':0,'Q':2,'J':3,'K':4,'7':10,"A":11, }



class Itulufu:

    def __init__(self) -> None:

        self.cartes_joueur = []
        self.cartes_ordi = []
        self.pile_cartes = []
        self.carte_reference = []
        
        self.pile_point_joueur = []
        self.pile_point_ordi = []


    

    

    def distribuer_cartes(self,nbr_carte,):
        nouveau_pile = creation_paquet()
        while len(nouveau_pile) >= (nbr_carte)*2:
            for i in range(nbr_carte):
                cartes_joueur= nouveau_pile.pop(randint(0, len(nouveau_pile)-1))
                self.cartes_joueur.append(cartes_joueur)
                cartes_ordi= nouveau_pile.pop(randint(0,len(nouveau_pile)-1))
                self.cartes_ordi.append(cartes_ordi)
                self.pile_cartes.append(nouveau_pile)
            
        
    def comparer_paquet(self):
        pass




    def gagnant (self):
        pass


    def debut_jeu(self):
        self.distribuer_cartes(3)



class Carte:
    SUITS = ['♠','♦','♥','♣']
    VALUES= ['A','3','4','5','6','7','J','Q','K']
    

class Paquet:  
    def __init__(self): 
        self.paquet = creation_paquet()

    def afficher(self):
        liste = []
        for element in self.paquet:
            liste.append(element)
        print(liste)


    




    def shuffle(self):
        return random.shuffle(self.paquet)

    
    def piger_carte(self):
        return self.paquet.pop()


class JoueurMain (Paquet):
    def __init__(self):
        super().__init__(self)
        self.cartes = []
        
    def afficher(self):
        for i in range(len(self.cartes)):
            for carte in self.cartes:
                print(carte)
    


def creation_paquet():
    paquet= []
    for i in range((len(Carte.SUITS))):
        for suit in Carte.SUITS:
            for value in Carte.VALUES:
                paquet.append(value+suit)
    return paquet



itulufu = Itulufu()
itulufu.debut_jeu()





# b= Paquet()
# b.afficher()
# b.shuffle()
# print()
# b.afficher()
# */