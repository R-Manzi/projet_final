
import random
import random
from random import randint



POINTS_CARTES_JEU = { '3':3,'4':4,'5':5,'6':6,'Q':7,'J':8,'K':9,'7':10,"A":11, }

POiNTS_FIN_PARTIE = { '3':0,'4':0,'5':0,'6':0,'Q':2,'J':3,'K':4,'7':10,"A":11, }



class Itulufu:

    def __init__(self) -> None:

        self.main_joueur = []
        self.main_ordi = []
        self.pile_cartes = []
        self.carte_reference = []
        
        self.pile_point_joueur = []
        self.pile_point_ordi = []


    def afficher(self):
        print( f'{self.main_joueur} \n {self.main_ordi} \n {self.pile_cartes}')

    def afficher_main_joueur(self):
        print(f'{self.main_joueur}')

    def afficher_carte_reference(self):
        print(f'{self.carte_reference}')


    

    def distribuer_cartes(self):
        paquet = creation_paquet()
        for i in range(3):
            cartes_joueur, cartes_ordi= random.choice(paquet),
            random.choice(paquet)
            self.main_joueur.append(cartes_joueur),self.main_ordi.append(cartes_ordi)
            paquet.remove(cartes_joueur),paquet.remove(cartes_ordi)

        carte_ref = random.choice(paquet)
        self.carte_reference.append(carte_ref)
        paquet.remove(carte_ref)
        self.pile_cartes.append(paquet)


    
    def piger (self, paquet):
        f,g = random.choice(paquet),random.choice(paquet)
        if f not in self.main_joueur and g not in self.main_ordi:
            self.main_joueur.append(f),self.main_ordi.append(g),
            paquet.remove(f),paquet.remove(g)
        return paquet
    



    def comparer_paquet(self):
        pass




    def gagnant (self):
        pass




    
    def debut_jeu(self):
        
        # loop_jeu = False
        # while not loop_jeu:
        print()
        debut= int(input('Entrer 1 pour commencer /  0 pour quiter : '))
        if debut == 0 :
            exit()
        
        else :
            print('la partie commence !!! : Bonne chance')
            self.distribuer_cartes()
            
    
            self.afficher_main_joueur()
            pile_a_piger = self.pile
            print('tu commencer la partie, choit une carte :')
            for count, carte in enumerate :
                pass






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
# 