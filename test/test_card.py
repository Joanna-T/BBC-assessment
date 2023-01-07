import unittest
from src.card import Card


class CardTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        pass

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_correct_values_attributed_to_cards(self):  
        card_one = Card("Heart", "Ace")
        card_two = Card("Heart", "Two")
        card_three = Card("Heart", "Three")
        card_four = Card("Heart", "Four")
        card_five = Card("Heart", "Five")
        card_six = Card("Heart", "Six")
        card_seven = Card("Heart", "Seven")
        card_eight = Card("Heart", "Eight")
        card_nine = Card("Heart", "Nine")
        card_ten = Card("Heart", "Ten")
        card_joker = Card("Heart", "Joker")
        card_queen = Card("Heart", "Queen")
        card_king = Card("Heart", "King")

        self.assertEqual(card_one.value, 0)
        self.assertEqual(card_two.value, 2)
        self.assertEqual(card_three.value, 3)
        self.assertEqual(card_four.value, 4)
        self.assertEqual(card_five.value, 5)
        self.assertEqual(card_six.value, 6)
        self.assertEqual(card_seven.value, 7)
        self.assertEqual(card_eight.value, 8)
        self.assertEqual(card_nine.value, 9)
        self.assertEqual(card_ten.value, 10)
        self.assertEqual(card_joker.value, 10)
        self.assertEqual(card_queen.value, 10)
        self.assertEqual(card_king.value, 10)


    


if __name__ == '__main__':
    unittest.main()
