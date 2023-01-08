from src.hand import Hand
from src.dealer import Dealer


def play():
    print ("######################################")
    print ("Welcome to this game of mini blackjack")
    print ("######################################")

    player_hands = [Hand()]

    print("\n")
    print("Player 1 has been added")
    print("\n")

    #add new players
    while True:
        new_player = input("Would you like to add another player? Type Y for yes or N for no.")

        if new_player.lower() == "y":
            player_hands.append(Hand())
            print("Player " + str(len(player_hands)) + " added.")
        elif new_player.lower() == "n":
            break
        else:
            print("Please enter a valid argument.")

    print("\n")
    print("##########")
    print("Game Start")
    print("##########")
    print("\n")

    dealer = Dealer()

    print("Dealing the opening hand...")
    dealer.deal_opening_hand(player_hands)

    if dealer.game_over:
        print ("Game concluded")
        return

    # commence game
    for i in range(len(player_hands)):

        if player_hands[i].status == "PLAYING":
            print("\n\nPlayer " + str(i + 1) + "'s turn. Your hand is the following: ")
            player_hands[i].print_hand()
            player_hands[i].print_score()
            while player_hands[i].status == "PLAYING":

                move = input("Would you like to hit or stand? Type HIT to hit or STAND to stand.")

                if move.lower() == "hit":
                    dealer.hit_player(player_hands[i])
                    player_hands[i].print_hand()
                    player_hands[i].print_score()

                elif move.lower() == "stand":
                    player_hands[i].stand()

                else:
                    print("Please enter a valid argument")
    


    dealer.draw_cards_until_stand_or_bust()

    dealer.evaluate_score(player_hands)
        


    

if __name__ == '__main__':
    play()
