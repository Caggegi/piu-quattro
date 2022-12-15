import random
from classes.card import Card

class Deck:
    def __init__(self):
        self.deck = []
        for num in range(0,10):
            for color in ["red", "blue", "yellow", "green"]:
                card = Card(color, num)
                self.deck.append(card)
        for value in ["wild", "wild4"]:
            for n in range(0,6):
                card = Card("special", value)
                self.deck.append(card)
        for color in ["red", "blue", "yellow", "green"]:
            for n in range(0,6):
                cardr = Card(color, "reverse")
                cardd = Card(color, "draw2")
                self.deck.append(cardr)
                self.deck.append(cardd)
        self.shuffle()
    
    def new_round(self, exclude:list):
        if Len(self.deck) == 0:
            __init__()
            new_deck = (card for card in self.deck if card not in exclude)
            self.deck = new_deck

    def shuffle(self):
        random.shuffle(self.deck)
    
    def next_card(self):
        return self.deck.pop()