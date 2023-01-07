import unittest
from src.deck import Deck
from src.card import Card


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self): 
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_drawing_a_card_works(self):
        card = self.deck.pick_card()

        self.assertEqual(len(self.deck.cards), 51)
        self.assertIsInstance(card,Card)

    def test_new_deck_added_when_all_cards_are_drawn(self):
        for i in range(53):
            self.deck.pick_card()

        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 51) # new deck only created when a request for a card is issued, so 51 cards are present

    


if __name__ == '__main__':
    unittest.main()
