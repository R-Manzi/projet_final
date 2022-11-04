
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
        Carte.CARTE_REFERENCE = self.pile_cartes.carte_reference()
        
        print(f'la carte de reference', self.carte_reference)
        self.carte = Carte()
  
        self.points_joeur = []
        self.points_ordi = []
       
    

      

    def valeur_fin_partie (self,carte):
        for cle, valeur in POiNTS_FIN_PARTIE.items():
            if cle == carte[0]:
                return valeur


    def gagnant(self, pile_joeur, pile_ordi):    
        points_joeur = 0
        points_ordi = 0
        for card in pile_joeur:
            points_joeur += self.valeur_fin_partie(card)
            for carte in pile_ordi:
                 points_ordi += self.valeur_fin_partie(carte)
        
        if points_ordi > points_joeur :
            print("ordinateur a pagner !!")

        elif points_ordi > points_joeur :
            print("vous avez pagnee!!")
        else:
            print("parti nulle")

   

    # print()#******************debut du jeu par cette methode*************************************#
    def debut_jeu(self):
       
        loop_jeu = False
        while not loop_jeu:
            print()
            print("******Itulufu*****")
            print('la partie commence !!! : Bonne chance')
            print()
            
            print(" -----La carte de reference est :", self.carte_reference)
            print()

            loop_jeu = False
            while not loop_jeu:

                loop_mache = False
                while  not loop_mache :

                
                    self.carte_played_joueur = self.main_joueur.jouer_carte()
                    self.carte_played_ordi = self.main_ordinateur.jouer_ordi(self.carte_reference, self.carte_played_joueur)
                    print()
                    print( f'les cartes joues sont :{self.carte_played_joueur}  {self.carte_played_ordi}')
                
                    self.main_gagnant = self.carte.comparaison_carte(self.carte_played_joueur,self.carte_played_ordi,self.carte_reference)
                    
                    if self.main_gagnant is self.carte_played_joueur: 
                        self.points_joeur.append(self.carte_played_joueur)
                        self.points_joeur.append(self.carte_played_ordi)
                    
                        print('-------------joueur gagne la manche------')

                    elif self.main_gagnant is self.carte_played_ordi: 
                        self.points_ordi.append(self.carte_played_ordi)
                        self.points_ordi.append(self.carte_played_joueur)
                        print('-------------Ordinateur gagne la manche -----')

            
                    self.pile_cartes.distribuer_cartes(self.main_joueur)
                    self.pile_cartes.distribuer_cartes(self.main_ordinateur)
                    print('il reste ',self.pile_cartes.count_objt())

                    loop_mache = self.pile_cartes.count_objt()
                    if loop_mache == 0:            

                        print('on est ici 1')
                        
                        self.carte_played_ordi = self.main_ordinateur.jouer_ordi(self.carte_reference, self.carte_played_joueur)
                        print()
                       
                        print( f'les cartes joues sont :{self.carte_played_joueur}  {self.carte_played_ordi}')
                    


                        self.main_gagnant = self.carte.comparaison_carte(self.carte_played_joueur,self.carte_played_ordi,self.carte_reference)
                        
                        if self.main_gagnant is self.carte_played_joueur: 
                            self.points_joeur.append(self.carte_played_joueur)
                            self.points_joeur.append(self.carte_played_ordi)
                        
                            print('-------------joueur gagne la manche------')

                        elif self.main_gagnant is self.carte_played_ordi: 
                            self.points_ordi.append(self.carte_played_ordi)
                            self.points_ordi.append(self.carte_played_joueur)
                            print('-------------Ordinateur gagne la manche -----')
                        


                        print('on est ici 2')
                        self.carte_played_joueur = self.main_joueur.jouer_carte()
                        self.carte_played_ordi = self.main_ordinateur.jouer_ordi(self.carte_reference, self.carte_played_joueur)
                        print()
                        self.main_joueur.afficher()
                        self.main_ordinateur.afficher()
                        print('on est ici 2')

                    

                        print( f'les cartes joues sont :{self.carte_played_joueur}  {self.carte_played_ordi}')
                    


                        self.main_gagnant = self.carte.comparaison_carte(self.carte_played_joueur,self.carte_played_ordi,self.carte_reference)
                        print(self.main_gagnant)
                        if self.main_gagnant is self.carte_played_joueur: 
                            self.points_joeur.append(self.carte_played_joueur)
                            self.points_joeur.append(self.carte_played_ordi)
                        
                            print('-------------joueur gagne la manche------')

                        elif self.main_gagnant is self.carte_played_ordi: 
                            self.points_ordi.append(self.carte_played_ordi)
                            self.points_ordi.append(self.carte_played_joueur)
                            print('-------------Ordinateur gagne la manche -----')

                        print('on est ici 3')

                        self.carte_played_joueur = self.main_joueur.jouer_carte()
                        self.carte_played_ordi = self.main_ordinateur.jouer_ordi(self.carte_reference, self.carte_played_joueur)
                        print()
                        print( f'les cartes joues sont :{self.carte_played_joueur}  {self.carte_played_ordi}')
                       
                    
                    Winner = self.gagnant(self.points_joeur,self.points_ordi)
                    print(Winner)
                    

                        


            


            

            


 

class Carte:
    SUITS = ['♠','♦','♥','♣']
    VALUES= ['A','3','4','5','6','7','J','Q','K']


    def suit(self):
        return self.suit

    def __lt__(self): # <
        pass
        itulfu = Carte.CARTE_REFERENCE

    
    def retourne_valeur(self,carte):
        for cle, valeur in POINTS_CARTES_JEU.items():
            if carte[0] == cle :
                return valeur

    def comparaison_carte(self,carte_joeur,carte_ordi,itulufu):
        a = self.retourne_valeur(carte_joeur)
        b = self.retourne_valeur(carte_ordi)
        
        if carte_joeur[1] == itulufu[1] and carte_ordi[1] != itulufu[1] :
            return carte_joeur

        elif carte_ordi[1] == itulufu[1] and carte_joeur[1] != itulufu[1] :
            return carte_ordi

        elif carte_joeur[1] == itulufu[1] and carte_ordi[1] == itulufu[1]:
        
            a = self.retourne_valeur(carte_joeur)
            b = self.retourne_valeur(carte_ordi)
            if a > b:
                a = carte_joeur
                return carte_joeur
            elif a < b:
                b = carte_ordi
                return carte_ordi
        
        elif carte_joeur[1] != itulufu[1] and carte_ordi[1] != itulufu[1] and a > b :
            return carte_joeur

        elif carte_joeur[1] != itulufu[1] and carte_ordi[1] != itulufu[1] and b > a :
            return carte_ordi

    
        elif carte_joeur[1] != itulufu[1] and carte_ordi[1] != itulufu[1] and a == b:
            return carte_ordi

        

        

    def comparer_endgame(self, carte_joeur,carte_ordi):
        a = self.retourne_valeur(carte_joeur)
        b = self.retourne_valeur(carte_ordi)

        if a > b:
            return carte_joeur
        
        elif a < b:
            b = carte_ordi
            return carte_ordi
               
        
        
    

    
 
class Paquet:
    def __init__(self):
        self.paquet = self.creation_paquet()

    def creation_paquet(self):
        paquet= []
        for suit in Carte.SUITS:
            for value in Carte.VALUES:
                paquet.append(value+suit)#paquet.apped(Carte(value, suit))
        return paquet

    def afficher(self):
        print(*self.paquet)



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

    
    def count_objt(self):
        return len(self.paquet)


    
    
class Main:
    def __init__(self) -> None:
        self.main = []

    def afficher(self):
        print(*self.main)

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def jouer_carte(self):
        print(*self.main)
        carte= int(input('choisit une carte 0,1,2 :'))
        if carte not in (0,1,3):
            print('choisissez un chiffre parmi 0-1-2')
            carte= int(input('choisit une carte 0,1,2 :'))
        
        
        else:
            carte = self.main[carte]
            self.main.remove(carte)
            return carte
        
    def jouer_ordi(self,carte_reference,carte_joue_joeur):
        for card in self.main :
            if card[1] == carte_reference[1] and carte_joue_joeur != carte_reference :
                if carte_joue_joeur[0] == '7' or carte_joue_joeur[0] =='A' or carte_joue_joeur[0] =='K':
                    self.main.remove(card)
                    return card
            
            elif card[0]  in ('3','4','5','6','7') :
                if carte_joue_joeur[1] != carte_reference[1]:
                    self.main.remove(card)
                    return card
        
        if  self.count_objt() == 1 :
            return self.main


        else:
            carte = (random.choice(self.main))
            self.main.remove(carte)
            return carte

    def count_objt(self):
        return len(self.main)
                
                    




itulufu = Itulufu()
itulufu.debut_jeu()


