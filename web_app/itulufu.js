
function play() {
    window.location.href = "page2.html";
  }
const SUITS = ['♦','♣','♥','♠']
const VALUES = ['A','3','4','5','6','7','J','Q','K']
const POiNTS_FIN_PARTIE = { '3':0,'4':0,'5':0,'6':0,'Q':2,'J':3,'K':4,'7':10,"A":11 }
const POINTS_CARTES_JEU = { '3':3,'4':4,'5':5,'6':6,'Q':7,'J':8,'K':9,'7':10,"A":11 }

var pile;
var mainJoeur;
var mainJoeurc1;
var mainJoeurc2;
var mainJoeurc3;

var mainOrdi;
var carteReference;

var paquet = nouveauPaquet()

window.onload = function() {
    nouveauPaquet();
    shuffle();
    debutJeu();

}
function nouveauPaquet() {
    paquet = []
    for (let suit in ['♦','♣','♥','♠'] ){
        for (let value in ['A','3','4','5','6','7','J','Q','K']) {
            paquet.push(`${VALUES[value]}${SUITS[suit]}`)
        }
    
        }
    return paquet
    }

function getValue (card){
    let info = card.split("");
    let valeur = info[0];
    if (isNaN(valeur)){
        if (valeur == "A"){
            return 11;    
        } else if (valeur == "K"){
            return 10;
        } else if (valeur == "J"){
            return 9;
        } else if (valeur == "Q"){
            return 8; 
        } else if (valeur == "7"){
            return 10;
    }
    return parseInt(valeur);
    }


pass
}
function shuffle() {
    let newPaquet = [];
    let newHalf1 = paquet.slice(0,18);
    let newHalf2 = paquet.slice(18,36);
    let i = 0;
    while (i < 18){
        newPaquet.push(newHalf1[i]);
        newPaquet.push(newHalf2[i]);
        i++;
    }
    
    paquet = newPaquet
    return paquet

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
function playComputer(main){
    card = main.pop()
    return card
}

function distribuer3(){
    i=0
    while (i<3){
        let card = deal3(paquet)
        cardImg.innerHTML += ""
        for(let j=0; j<3;j++){
            cardImg.innerHTML +='<img src="png/'+ card[i] +'.png.png"/>';
            i++;

        }        

    }
}

    

// function playJouer(main) {
//     main = document.getElementByID('carte_gauche').addEventListener('click',(move))
// }

// function move(){
//     choix = mainJoeur.pop()
//     document.getElementById.
// }



function debutJeu() {

    let card_bak = document.querySelector("#deck");
    card_bak.innerHTML= "<img src=back.png />'";

    let cardImg = document.querySelector("#player");
    let card_reference = document.querySelector('#itulufu');
    
    let mainJoeur =  document.querySelector("#player");
    let mainJoeurc1 =  document.querySelector('#playerC1');
    let mainJoeurc2 =  document.querySelector('#playerC2');
    let mainJoeurc3 =  document.querySelector('#playerC3');

    mainJoeurc1 = paquet.pop();
    
    mainJoeurc2 = paquet.pop();
    mainJoeurc3 = paquet.pop();


    
    mainJoeurc1.innerHTML +='<img src="png/'+ mainJoeurc1 +'.png.png"/>';
    mainJoeurc2.innerHTML +='<img src="png/'+ mainJoeurc2 +'.png.png"/>';
    mainJoeurc3.innerHTML +='<img src="png/'+ mainJoeurc3 +'.png.png"/>';

    
    mainJoeur = deal3(paquet)
    i=0
    while (i<3){
        let card = mainJoeur
        cardImg.innerHTML += ""
        for(let j=0; j<3;j++){
            cardImg.innerHTML +='<img src="png/'+ card[i] +'.png.png"/>';
            i++;

        }        

    } 
    mainOrdi = deal3(paquet)

    carteReference = paquet.pop();
    card_reference.innerHTML+='<img src="png/'+ carteReference +'.png.png"/>';

    
   
 
    
    


  
 



}
  
