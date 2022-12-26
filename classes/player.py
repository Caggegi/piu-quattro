import random
from classes.card import Card

class Player:
    score = 0

    def __init__(self, cards:list[Card], name:str):
        self.name = name
        self.hand = cards

    def __str__(self):
        cards = ""
        for card in self.hand:
            cards = cards+str(card)
        return "\n-------------------\nname: "+self.name+"\nscore:"+str(self.score)+"\ncards:"+cards+"\n"

    def playCard(self, card:Card, last:Card):
        if last.color == card.color:
            card.playCard()
            self.hand.remove(card)
            return card
        elif card.color == "z":
            self.hand.remove(card)
            print("Scegli il nuovo colore: ")
            card.color=input()
            card.playCard()
            return card
        else:
            return last
    
    def sortHand(self):
        self.hand.sort(key=lambda x: x.color, reverse=False)
