from termcolor import colored

class Card:
    def __init__(self,color, value):
        self.color = color
        self.value = value
    
    def __str__(self):
        return (colored(" "+str(self.value), self.color if self.color is not "z" else "white"))
    
    def playCard(self):
        print ("Hai giocato il ",self.color,self.value)
        #TODO play card backend