import random
from src.card import Card
class Deck:
    SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]
    CARD_NAMES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Joker", "Queen", "King"]

    def __init__(self):
        self.cards = []
        self.__initialize_deck()

    def __initialize_deck(self):

        for suit in self.SUITS:

            for name in self.CARD_NAMES:
                self.cards.append(Card(suit, name))


    def pick_card(self):
        #if no more cards, start new deck
        if len(self.cards) == 0:
            self.__initialize_deck()

        #remove random card
        return self.cards.pop(random.randrange(len(self.cards)))


