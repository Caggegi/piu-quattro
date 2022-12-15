import random

class Player:

    objectives = ["crazy", "quick", "lazy","happy","joy","kinetic","big","little","strong","weak","hungry","angry","cute"]
    animals = ["cat", "dog", "parrot","gorilla","dolphin","cheeta","fox","shark","giraffe","narwal","whale","bee","beever"]

    score = 0

    def __init__(self, cards:list, name:str):
        self.name = name
        self.hand = cards

    def __str__(self):
        cards = ""
        for card in self.hand:
            cards = cards+str(card)
        return "\n-------------------\nname: "+self.name+"\nscore:"+str(self.score)+"\ncards:"+cards+"\n"