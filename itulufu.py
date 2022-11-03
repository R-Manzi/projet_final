
import random




POINTS_CARTES_JEU = { '3':3,'4':4,'5':5,'6':6,'Q':7,'J':8,'K':9,'7':10,"A":11, }

POiNTS_FIN_PARTIE = { '3':0,'4':0,'5':0,'6':0,'Q':2,'J':3,'K':4,'7':10,"A":11, }




class Itulufu:

    def __init__(self) -> None:

        self.pile_cartes = Paquet()
        self.pile_cartes.afficher()
        self.pile_cartes.shuffle()
        self.pile_cartes.afficher()
        self.main_joueur = Main()
        self.main_joueur.afficher()
        self.main_ordinateur = Main()
        self.main_ordinateur.afficher()
        self.pile_cartes.distribuer_cartes_initial(self.main_joueur)
        self.main_joueur.afficher()
        self.pile_cartes.distribuer_cartes_initial(self.main_ordinateur)
        self.main_joueur.afficher()
        self.carte_reference = self.pile_cartes.carte_reference()
  
        self.points_joeur = []
        self.points_ordi = []
        print(self.carte_reference)
        print(self.carte_reference)
    

        
 


    
    


    # def piger (self, paquet):
    #     cartes_joueur = random.choice(paquet)
    #     self.main_joueur.append(cartes_joueur)
    #     paquet.remove(cartes_joueur)
    #     cartes_ordi= random.choice(paquet)
    #     self.main_ordi.append(cartes_ordi)
    #     paquet.remove(cartes_ordi)




    #     f,g = random.choice(paquet),random.choice(paquet)
    #     if f not in self.main_joueur and g not in self.main_ordi:
    #         self.main_joueur.append(f),self.main_ordi.append(g),
    #         paquet.remove(f),paquet.remove(g)
    #     return paquet


   

    # print()#*******************************************************#
    def debut_jeu(self):
      
        loop_jeu = False
        while not loop_jeu:
            print()
            debut= int(input('Entrer un chiffre pour commencer /  0 pour quiter : '))
            if debut == 0 :
                exit()

            else:
                print('la partie commence !!! : Bonne chance')
                print()
                print()
                self.carte_played_joueur = self.main_joueur.jouer_carte()
                self.carte_played_ordi = self.main_ordinateur.jouer_ordi()
                
            

class Carte:
    SUITS = ['♠','♦','♥','♣']
    VALUES= ['A','3','4','5','6','7','J','Q','K']

    def __init__(self, value,suit):
        self.value = value
        self.suit = suit

    
    def suit(self):
        return self.suit  

    def value(self):
        if self.value == 'A':
            return 11
        elif self.value == '7':
            return 10
        elif self.value == 'K':     
            return 9
        elif self.value == 'J':
            return 8
        elif self.value == 'Q':
            return 7
        
        elif self.value == '6':
            return 6
        
        elif self.value == '5':
            return 5
        elif self.value == '4':
            return 4
        elif self.value == '3':
            return 3

 

    def get_valeur_jeu(self):
        pass








class Paquet:
    def __init__(self):
        self.paquet = self.creation_paquet()

    def creation_paquet(self):
        paquet= []
        for suit in Carte.SUITS:
            for value in Carte.VALUES:
                paquet.append(value+suit)
        return paquet

    def afficher(self):
        liste = []
        for element in self.paquet:
            liste.append(element)
        print(self.paquet)



    def shuffle(self):
        random.shuffle(self.paquet)    


    def distribuer_cartes(self, main):
        carte = random.choice(self.paquet)
        main.ajouter_carte(carte)
        self.paquet.remove(carte)
    
    def distribuer_cartes_initial(self,main):
        for i in range(3):
            self.distribuer_cartes(main)


    def carte_reference(self):    
        carte = random.choice(self.paquet)
        self.paquet.remove(carte)
        return carte
    
    def suit(self):
        return self.suit


class Main:
    def __init__(self) -> None:
        self.main = []

    def afficher(self):
        print(self.main)

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def jouer_carte(self):
        print(self.main)
        carte= int(input('choisit une carte 0,1,2 :'))
        carte = self.main[carte]
        print(carte)
        self.main.remove(carte)
        print(self.main)
        return carte


def is_itulufu(self):
        return Itulufu.carte_reference[1]










itulufu = Itulufu()
itulufu.debut_jeu()


