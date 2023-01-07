import unittest
from src.dealer import Dealer
from src.hand import Hand
from src.card import Card


class DealerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.dealer = Dealer()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_dealing_opening_hand_gives_players_two_cards(self):  # any method beginning with 'test' will be run by unittest
        player_array = [Hand(), Hand()]

        self.dealer.deal_opening_hand(player_array)

        self.assertEqual(len(player_array[0].cards), 2)
        self.assertEqual(len(player_array[1].cards), 2)

    def test_dealing_opening_hand_draws_two_cards_for_dealer(self):
        player_array = [Hand(), Hand()]

        self.dealer.deal_opening_hand(player_array)

        self.assertEqual(len(self.dealer.cards), 2)
        self.assertGreater(self.dealer.score, 0)

    def test_adding_to_dealer_hand_increases_score(self):
        self.dealer.add_to_hand(Card("Heart", "Ace"))

        self.assertEqual(self.dealer.score, 11)

    def test_drawing_cards_to_reaches_value_more_than_or_equal_to_17(self):
        self.dealer.draw_cards_until_stand_or_bust()

        self.assertGreaterEqual(self.dealer.score, 17)

    def test_correct_results_announced_if_dealer_is_bust(self):
        self.dealer.score = 25



if __name__ == '__main__':
    unittest.main()
