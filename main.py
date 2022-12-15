from classes.card import Card
from classes.deck import Deck
from classes.player import Player
import random

class Game:

    deck = Deck()
    players = []

    def __init__(self, n_players:int=2):
        print("\n\n\n\t\t\tThe game is starting\n\n\n")
        if(n_players > 16):
            print("\nNon possono partecipare più di 16 giocatori\n")
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

    def gameover(player:Player, score:int=0, error:bool=False):
        print("GameOver")
        if error is True:
            print("Si è verificato un errore!\n\n")
        else:
            #player.score += score
            pass

game = Game(16)