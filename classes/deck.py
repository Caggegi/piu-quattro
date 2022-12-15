import random
from classes.card import Card

class Deck:
    def __init__(self):
        self.deck = []
        for num in range(0,20):
            for color in ["red", "blue", "yellow", "green"]:
                card = Card(color, num%10)
                self.deck.append(card)
        for value in ["wild", "wild4"]:
            for n in range(0,4):
                card = Card("special", value)
                self.deck.append(card)
        for color in ["red", "blue", "yellow", "green"]:
            for n in range(0,2):
                cardr = Card(color, "reverse")
                cardd = Card(color, "draw2")
                cards = Card(color, "skip")
                self.deck.append(cardr)
                self.deck.append(cardd)
                self.deck.append(cards)
        self.shuffle()
    
    def new_round(self, exclude:list):
        if Len(self.deck) == 0:
            __init__()
            new_deck = (card for card in self.deck if card not in exclude)
            self.deck = new_deck

    def shuffle(self):
        random.shuffle(self.deck)
    
    def next_card(self):
        try:
            return self.deck.pop()
        except IndexError:
            raise NextCardException()


class NextCardException(BaseException):
    def __init__(self, message:str="No more card in this deck"):
        super().__init__(message)