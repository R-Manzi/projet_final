function jouer() {
    window.location.href = "/jouer";
  }

const SUITS = ['♦','♣','♥','♠']
const VALUES = ['A','3','4','5','6','7','J','Q','K']

class Paquet {
constructor(cards = nouveauPaquet()) {
this.cards = cards 
}


get fullCartes() {
    return this.cards.length

}
get halfCartes () {
    return this.cards.length /2

}
}

function deal(deck){
    var card = Math.floor(Math.random()*this.cards.length); // https://stackoverflow.com/questions/39967891/dealing-cards-from-a-deck-and-removing-the-cards-from-an-array
    return deck.splice(card, 1);
  }
var pulledCard = deal(deckNames)


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
    deck.assamblage()
    deck2.shuffleAssembly(deck)
    







distribution (){
    this.cards = []
    for (let suit in SUITS){
        for (let value in VALUES) {
            this.cards.push(`${VALUES[value]}${SUITS[suit]}`)
        }
    }
  const assamblage = document.getElementById('decks');
        const pile_cartes = document.getElementById(' derriere')
        const cartes_joeurs = document.getElementById('player')
        const cartes_ref = document.getElementById('itulufu')
        pile_cartes.innerHTML ='<img src="/back.png"/>'+ "&emsp;"
        cartes_joeurs.innerHTML =" ";
       cartes_ref.innerHTML =" ";

       let partie = False
       while ( partie ){
        while (i < SUITS.length) {
            assamblage.innerHTML += "<a>"
            assamblage_2.innerHTML += "<a>"
            assamblage_3.innerHTML += "<a>"
            assamblage_4.innerHTML += "<a>"
            i++;
            while (j < 3){
                pile_cartes +='<img src="png/' + this.cards[0*i+j] + '.png.png" />'+ "&emsp;"
                assamblage_2.innerHTML +='<img src="png/' + this.cards[3*i+j] + '.png.png" />'+ "&emsp;"  
            j++;
            
        k++;

            } 
        }