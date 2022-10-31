
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
 


    def afficher(self):
        print( f'{self.main_joueur} \n {self.main_ordi} \n {self.pile_cartes}')

    def afficher_main_joueur(self):
        print(f'{self.main_joueur}')

    def afficher_carte_reference(self):
        print(f'{self.carte_reference}')




    def distribuer_cartes(self):
        paquet = creation_paquet()
        for i in range(3):
            cartes_joueur = random.choice(paquet)
            self.main_joueur.append(cartes_joueur)
            paquet.remove(cartes_joueur)
            cartes_ordi= random.choice(paquet)
            self.main_ordi.append(cartes_ordi)
            paquet.remove(cartes_ordi)

        carte_ref = random.choice(paquet)
        self.carte_reference.append(carte_ref)
        paquet.remove(carte_ref)
        self.pile_cartes.append(paquet)



    def piger (self, paquet):
        cartes_joueur = random.choice(paquet)
        self.main_joueur.append(cartes_joueur)
        paquet.remove(cartes_joueur)
        cartes_ordi= random.choice(paquet)
        self.main_ordi.append(cartes_ordi)
        paquet.remove(cartes_ordi)




        f,g = random.choice(paquet),random.choice(paquet)
        if f not in self.main_joueur and g not in self.main_ordi:
            self.main_joueur.append(f),self.main_ordi.append(g),
            paquet.remove(f),paquet.remove(g)
        return paquet


    def comparer_carte(self):
        pass





    def gagnant (self):
        pass



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
                print('tu commencer la partie, choit une carte :')
                for count, carte in enumerate :
                    pass



class Carte:
    SUITS = ['♠','♦','♥','♣']
    VALUES= ['A','3','4','5','6','7','J','Q','K']


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


class Main:
    def __init__(self) -> None:
        self.main = []

    def afficher(self):
        print(self.main)

    def ajouter_carte(self, carte):
        self.main.append(carte)


    def jouer_carte_ordi(self):
        for i in range:
            pass








itulufu = Itulufu()
# itulufu.debut_jeu()


