
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


        def distribuer_cartes(self):
            pass

        def piger_cartes(self):
            pass

        def comparer_paquet(self):
            pass








class Carte:
    SUITS = ['♠','♦','♥','♣']
    VALUES= ['A','3','4','5','6','7','J','Q','K']
    

class Paquet:

    POINTS= [("Q",2),("J",3),("K",4),("7",11),("A",11)]
    
    def __init__(self): 
        self.paquet = creation_paquet()

    def afficher(self):
        liste = []
        for element in self.paquet:
            liste.append(element)
        print(liste)

    
    
    def shuffle(self):
        random.shuffle(self.paquet)

    
    def enlever_carte(self):
        return self.paquet.pop()

    




class JoueurMain (Paquet):
    def __init__(self, id_joueur=""):
        self.cartes = []
        self.id_joeur = id




 


class Classement:
    pass
    


def creation_paquet():
    paquet= []
    for i in range((len(Carte.SUITS))):
        for suit in Carte.SUITS:
            for value in Carte.VALUES:
                paquet.append(value+suit)
    return paquet



def demarrer():







 
b= Paquet()
b.afficher()
b.shuffle()
print()
b.afficher()
