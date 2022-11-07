
const SUITS = ['♦','♣','♥','♠']
const VALUES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


class Paquet {
    constructor(cards = nouveauPaquet()) {
    this.cards = cards 
    }

    get fullCartes() {
        return this.cards.length

    }

   distribuer_card () {
        return this.cards.pop();
   }
   
   fin_pile () {
    return (this.cards.length ==0);
   }

    length(){
        return this.cards.length;

    }

    shuffle() {
        const newPaquet = []
        const newHalf1 = this.cards.slice(0,this.fullCartes-26);
        const newHalf2 = this.cards.slice(this.halfCartes,this.fullCartes);
        let i = 0;
        while (i < this.halfCartes){
            newPaquet.push(newHalf1[i]);
            newPaquet.push(newHalf2[i]);
        i++;

        }

        this.cards = newPaquet
        return this.cards;
          
    }
}
    console.log(this.cards)
    

    
    distriberr3 () {
        this.cards = []
        for (let suit in SUITS){
            for (let value in VALUES) {
                this.cards.push(`${VALUES[value]}${SUITS[suit]}`)
            }
        }
        const assamblage = document.getElementById('decks');
       
    
        let i = 0;
        let j = 0;
        let k = 0;
        while (k < 4 ){
            while (i < SUITS.length) {
                assamblage.innerHTML += "<a>"
                
                i++;
                while (j < 13){
                    assamblage.innerHTML +='<img src="png/' + this.cards[i] + '.png.png" />'+ "&emsp;"
                   
                j++;
                
            k++;
    
                } 
            }
    
        }  
    }
    
    
  
        
    // shuffleAssembly () {
    //     const assembly = deal3()
    //     const assamblage = document.getElementById('decks');
       
    //     assamblage.innerHTML =" ";
       
    //     let i = 0;
    //     let j = 0;
    //     let k = 0;
    //     while (k < 4 ){
    //         while (i < SUITS.length) {
    //             assamblage.innerHTML += "<a>"
               
    //             i++;
    //             while (j < 4){
    //                 assamblage.innerHTML +='<img src="png/' + assembly[0*i+j] + '.png.png" />'+ "&emsp;"
          
    //             j++;
    //         k++;
    
    //     }   
    // }
    

    // }
  
    
 
    // JeuCommence {




    // }




}

function deal3(deck) {
    let i = 0;
    let cartes3 = []
    while (i < 3){
        cartes3.push(deck.pop())
        i++;
    }
    return cartes3
}
function afficher3() {
    deal3(deck);
    

}

function nouveauPaquet() {
    cards = []
    for (let suit in SUITS){
        for (let value in VALUES) {
            cards.push(`${VALUES[value]}${SUITS[suit]}`)
        }
    return cards    
        }
    }




let deck = new Paquet()
let deck2= deck
deal3(deck)
player.innerHTML = 







