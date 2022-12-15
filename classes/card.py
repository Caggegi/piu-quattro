from termcolor import colored

class Card:
    def __init__(self,color, value):
        self.color = color
        self.value = value
    
    def __str__(self):
        return (colored("\n\t"+str(self.value), self.color if self.color is not "special" else "white"))
    
    def playCard(self):
        print ("Hai giocato il ",self.value,self.color)
        #TODO play card backend