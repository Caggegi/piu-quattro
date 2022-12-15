from classes.card import Card
from classes.deck import Deck
from classes.player import Player

class Game:
    deck = Deck()

    def __init__(self, n_players:int):
        print("\n\n\n\t\t\tThe game is starting\n\n\n")
        players = []
        for p in range(0, n_players):
            p_cards = []
            for c in range(0,7):
                p_cards.append(self.deck.next_card())
            players.append(Player(cards=p_cards))
            print(players[p])

game = Game(4)
