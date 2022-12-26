from classes.card import Card
from classes.deck import Deck, NextCardException
from classes.player import Player
import random

MAX_PLAYERS_N = 8


class Game:

    deck = Deck()
    players = []
    last = deck.next_card()
    index = 0
    coeff = 1


    def __init__(self, n_players: int = 2):
        print("\n\n\n\t\t\tThe game is starting\n\n\n")
        if (n_players > MAX_PLAYERS_N):
            print("\nPlayers limit reached (max 8 people)\n")
            self.gameover(error=True)
            return
        self.players = []
        file = open("assets/animals.txt", "r")
        animals = file.readlines()
        file.close()
        file = open("assets/adjectives.txt", "r")
        adjectives = file.readlines()
        file.close()
        for p in range(0, n_players):
            p_cards = []
            for c in range(0, 7):
                p_cards.append(self.deck.next_card())
            self.players.append(Player(
                cards=p_cards,
                name=random.choice(adjectives)+" " +
                random.choice(animals)
            )
            )

    def gameover(self, player: Player, score: int):
        print(player.name+" ha vinto "+str(score)+" punti\n\n")

    def giveCard(self):
        try:
            return self.deck.next_card()
        except NextCardException:
            exclude = []
            for p in players:
                for c in p.hand:
                    exclude.append(c)
            self.deck.new_round(exclude)
            return self.deck.next_card()

    def play(self):
        while (True):
            print(self.last)
            skipped = False
            actual_p = self.players[self.index % len(self.players)]
            actual_p.sortHand()
            if any(x.color == self.last.color for x in actual_p.hand) or any(x.color == "z" for x in actual_p.hand):
                print(actual_p)
                choice = input()
                self.last = actual_p.playCard(actual_p.hand[int(choice)], self.last)
                played = self.last
            else:
                newCard = self.giveCard()
                actual_p.hand.append(newCard)
                print(actual_p)
                if newCard.color == self.last.color or newCard.color == "z":
                    print("vuoi giocarla? (y/N): ")
                    choice = input()
                    if choice == "y":
                        self.last = actual_p.playCard(newCard, self.last)
                    else:
                        skipped = True
                        print("turno skippato 1")
                else:
                    skipped = True
                    print("turno skippato 2")
            if not skipped:
                if self.last.value == "skip":
                    self.index = self.index+self.coeff
                elif self.last.value == "draw2":
                    for x in range(0, 2):
                        self.players[(self.index+self.coeff) %
                                     len(self.players)].hand.append(self.giveCard())
                    self.index+self.coeff
                elif self.last.value == "wild4":
                    for x in range(0, 4):
                        self.players[(self.index+self.coeff) %
                                     len(self.players)].hand.append(self.giveCard())
                    self.index+self.coeff
                elif self.last.value == "reverse":
                    self.coeff = self.coeff*(-1)
            if (len(actual_p.hand)) == 0:
                self.gameover(actual_p, 200)
                break
            self.index = self.index+self.coeff
