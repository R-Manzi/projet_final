
import random




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
        random.shuffle(self.paquet)


    
    def enlever_carte(self):
        return self.paquet.pop()




class joueur (Paquet):
    pass



class Classement:
    pass
    


class Points:
    POINTS= [("Q",2),("J",3),("K",4),("7",11),("A",11)]



def creation_paquet():
    paquet= []
    for i in range((len(Carte.SUITS))):
        for suit in Carte.SUITS:
            for value in Carte.VALUES:
                paquet.append(value+suit)
    return paquet

b= Paquet()
b.afficher()
b.shuffle()
print()
b.afficher()
