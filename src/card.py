class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
        self.value = -1
        self.__determine_value()
    
    def __determine_value(self):
        if self.name == "Ace":
            self.value = 0
        if self.name == "Two":
            self.value = 2
        if self.name == "Three":
            self.value = 3
        if self.name == "Four":
            self.value = 4
        if self.name == "Five":
            self.value = 5
        if self.name == "Six":
            self.value = 6
        if self.name == "Seven":
            self.value = 7
        if self.name == "Eight":
            self.value = 8
        if self.name == "Nine":
            self.value = 9
        if self.name == "Ten":
            self.value = 10
        if self.name == "Joker":
            self.value = 10
        if self.name == "Queen":
            self.value = 10
        if self.name == "King":
            self.value = 10

    def __repr__(self):
        return self.name + " of " + self.suit