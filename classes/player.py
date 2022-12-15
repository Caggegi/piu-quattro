import random

class Player:
    batti = ["AMO","ATE","BALENO","BECCO","BILE","BILITA","CARNE","CHIAPPE","CODA","COFFA","CULO","CUORE","FALCE","FIACCA","FIANCO","FOLLE","FONDO","FREDO","GIA","LANA","LARDO","LASTRA","LOCCHIO","LOGLIO","LORO","MA","MANI","MARE","MAZZA","ME","MENTO","MURO","PALI","PALLE","PALO","PANNI","PENNA","PISTA","PORTA","RAME","SCOPA","SEGOLA","SOFFIA","SPIAGGIA","SPOLVERO","STA","STERO","STI","STINA","STRADA","SUOCERA","TACCO","TAPPETO","TICCIA","TO","TOIO","TORE","TURE"]
    objectives = ["crazy", "quick", "lazy","happy","joy","kinetic","big","little","strong","weak","hungry","angry","cute"]
    animals = ["cat", "dog", "parrot","gorilla","dolphin","cheeta","fox","shark","giraffe","narwal","whale","bee","beever"]
    #def __init__(self, name=((random.choice(objectives))+" "+(random.choice(animals)))):
    def __init__(self, cards:list, name = "BATTI"+random.choice(batti).lower()):
        self.name = name
        self.hand = cards

    def __str__(self):
        cards = ""
        for card in self.hand:
            cards = cards+str(card)
        return "\n-------------------\nname: "+self.name+"\ncards:"+cards+"\n"