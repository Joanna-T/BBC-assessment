import unittest
from src.hand import Hand
from src.card import Card


class HandTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.hand = Hand()


    def tearDown(self):  # this method will be run after each tests
        pass

    def test_cards_in_opening_hand(self):  
        card_one = Card("Hearts", "Nine")
        card_two = Card("Diamonds", "Ten")

        self.hand.add_to_hand(card_one)
        self.hand.add_to_hand(card_two)

        self.assertEqual(len(self.hand.cards), 2)
    
    def test_hand_hit_score_evaluation(self):
        # example card
        card_one = Card("Hearts", "Three")

        self.hand.add_to_hand(card_one)

        self.assertEqual(self.hand.score, 3)

    def test_score_evaluation_after_standing(self):
        # example card
        card_one = Card("Hearts", "Three")

        self.hand.add_to_hand(card_one)

        self.hand.stand()

        self.assertEqual(self.hand.status, "STANDING") 
        self.assertEqual(self.hand.score, 3)
    
    def test_valid_hand_if_score_is_less_than_21(self):
        # example cards to total value to less than 21
        card_one = Card("Hearts", "Four")
        card_two = Card("Hearts", "Five")
        card_three = Card("Hearts", "Ace") 

        self.hand.add_to_hand(card_one)
        self.hand.add_to_hand(card_two)
        self.hand.add_to_hand(card_three)

        self.assertNotEqual(self.hand.score, -1) # indicates valid score
        self.assertEqual(self.hand.status, "PLAYING") 

    def test_invalid_hand_if_score_more_than_21(self):
        # example cards to total value to more than 21
        card_one = Card("Hearts", "King")
        card_two = Card("Hearts", "Queen")
        card_three = Card("Hearts", "Joker")

        self.hand.add_to_hand(card_one)
        self.hand.add_to_hand(card_two)
        self.hand.add_to_hand(card_three)

        self.assertEqual(self.hand.score, -1) # indicates invalid score
        self.assertEqual(self.hand.status, "BUST")

    def test_score_is_21_when_hand_has_king_and_ace(self):
        # king and ace cards
        card_one = Card("Hearts", "King")
        card_two = Card("Hearts", "Ace") 

        self.hand.add_to_hand(card_one)
        self.hand.add_to_hand(card_two)

        self.assertEqual(self.hand.score, 21)

    def test_score_is_21_when_hand_has_king_queen_and_ace(self):
        # king, ace and queen
        card_one = Card("Spades", "King")
        card_two = Card("Spades", "Ace") 
        card_three = Card("Spades", "Queen")

        self.hand.add_to_hand(card_one)
        self.hand.add_to_hand(card_two)
        self.hand.add_to_hand(card_three)

        self.assertEqual(self.hand.score, 21)

    def test_score_21_when_hand_has_nine_and_two_aces(self):
        # 9 and two aces
        card_one = Card("Spades", "Nine")
        card_two = Card("Spades", "Ace")
        card_three = Card("Spades", "Ace")

        self.hand.add_to_hand(card_one)
        self.hand.add_to_hand(card_two)
        self.hand.add_to_hand(card_three)

        self.assertEqual(self.hand.score, 21)
    


if __name__ == '__main__':
    unittest.main()
