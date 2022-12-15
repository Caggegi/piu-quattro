from classes.card import Card
from classes.deck import Deck, NextCardException
from classes.player import Player
import random

MAX_PLAYERS_N = 8

class Game:

    deck = Deck()
    players = []

    def __init__(self, n_players:int=2):
        print("\n\n\n\t\t\tThe game is starting\n\n\n")
        if(n_players > MAX_PLAYERS_N):
            print("\nPlayers limit reached (max 8 people)\n")
            self.gameover(error=True)
            return
        self.players = []
        for p in range(0, n_players):
            p_cards = []
            for c in range(0,7):
                p_cards.append(self.deck.next_card())
            self.players.append(Player(
                cards=p_cards, 
                name=
                    random.choice(Player.objectives)+" "+
                    random.choice(Player.animals)
                )
            )
            print(self.players[p])

    def gameover(player:Player, score:int=0):
        pass