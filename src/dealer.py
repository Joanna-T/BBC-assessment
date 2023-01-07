#from hand import Hand
from src.deck import Deck

# dealer is given ownership of drawing and dealing cards, as well as score evaluation
class Dealer:
    STAND_POINT = 17

    def __init__(self):
        self.game_over = False
        self.cards = []
        self.score = 0
        self.deck = Deck()

    def deal_opening_hand(self, players):
        # deal cards to self
        dealer_card_one = self.deck.pick_card()
        dealer_card_two = self.deck.pick_card()
     
        self.add_to_hand(dealer_card_one)
        self.add_to_hand(dealer_card_two)

        # deal cards to players
        for i in range(len(players)):
        
            self.hit_player(players[i])
            self.hit_player(players[i])

            if players[i].score == 21 and self.score < 21:
                players[i].status = "NATURAL"
                print("Player " + str(i + 1) + " has reached a natural")
            elif players[i].score == 21 and self.score == 21:
                players[i].status = "TIE"
                print("Player " + str(i + 1) + " has tied with the dealer")

        #dealer has achieved score of 21, all players with scores less than this have lost
        if self.score == 21:
            self.game_over = True
            self.announce_results(players)

       

    def add_to_hand(self, card):
        self.cards.append(card)

        if card.name == "Ace" and self.STAND_POINT - self.score >= 11:
            self.score += 11
        elif card.name == "Ace" and self.STAND_POINT - self.score < 11:
            self.score += 1
        else:
            self.score += card.value

    
    def evaluate_score(self, players):
        if self.score <= 21 and self.score >= self.STAND_POINT:
            self.game_over = True
            self.announce_results(players)
        if self.score > 21:
            self.game_over = True
            self.announce_dealer_bust(players)

    
    def announce_results(self, players):
        for i in range(len(players)):
            if players[i].status == "STANDING" or players[i].status == "PLAYING":
                if players[i].score < self.score:
                    print ("Player " + str(i + 1) + " has not beaten the dealer.")
                elif players[i].score > self.score:
                    print ("Player " + str(i + 1) + " has beaten the dealer.")
                else:
                    print ("Player " + str(i + 1) + " has tied with the dealer.")
            if players[i].status == "BUST":
                print ("Player " + str(i + 1) + " has not beat the dealer.")

    def announce_dealer_bust(self, players):
        print("The dealer has bust, the following players have beaten the dealer:")
        for i in range(len(players)):
            if players[i].status == "STANDING" or players[i].status == "NATURAL":
                print(str(i + 2), end=" ")
        print("\n")


    def draw_cards_until_stand_or_bust(self):
        while self.score < 17:
            card = self.deck.pick_card()
            self.add_to_hand(card)

        print("The dealer has a final score of " + str(self.score))
            

    def hit_player(self, player):
        card = self.deck.pick_card()
        player.add_to_hand(card)


    def __repr__(self):
        return "Dealer score is " + str(self.score)