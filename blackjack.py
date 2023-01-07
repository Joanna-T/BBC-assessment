from src.hand import Hand
from src.dealer import Dealer
#from src.constants import MAX_NUMBER


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
        

    



    #########################################old solution
    # dealer = Dealer()
    # player_one = Hand()
    # player_two = Hand()

    # players = [player_one,player_two]

    # dealer.deal_opening_hand(players)

    #######################################old solution
    # deck = Deck()

    # player_hands = [Hand()]

    # print ("######################################")
    # print ("Welcome to this game of mini blackjack")
    # print ("######################################")

    # print("\n")
    # print("Player 1 has been added")
    # print("\n")

    # #add new players
    # while True:
    #     new_player = input("Would you like to add another player? Type Y for yes or N for no.")

    #     if new_player.lower() == "y":
    #         player_hands.append(Hand())
    #         print("Player " + str(len(player_hands) + " added."))
    #     elif new_player.lower() == "n":
    #         break
    #     else:
    #         print("Please enter a valid argument.")
    # print("\n")
    # print("##########")
    # print("Game Start")
    # print("##########")
    # print("\n")

    # #keep track of players who are still playing
    # valid_players = len(player_hands)
    
    # #execute the interactive portion of the game 
    # #each player draws cards until they bust or choose to stand
    # while valid_players > 0:

    #     for i in range(len(player_hands)):

    #         current_player = player_hands[i]

    #         if current_player.playing:

    #             print("Player " + str(i + 1) + "'s turn.")
                
    #             #keep checking for valid input
    #             while True:

    #                 move = input("Would you like to hit or stand? Type HIT to hit or STAND to stand.")

    #                 if move.lower() == "hit":

    #                     new_card = deck.pick_card()
    #                     print ("New card value is " + str(new_card))
    #                     current_player.add_to_hand(new_card)
    #                     print("Your new hand is:")
    #                     current_player.print_hand()
    #                     current_player.print_score()

    #                     if not current_player.playing:
    #                         valid_players -= 1
    #                     break

    #                 elif move.lower() == "stand":

    #                     print("You have chosen to stand with the following stats:")
    #                     current_player.print_score
    #                     current_player.playing = False
    #                     valid_players -= 1
    #                     break

    #                 else:
    #                     print("Please enter a valid argument.")


    # #dealer draws until a value of 17 or higher is reached
    # print("\n")
    # print("Drawing dealer cards...")
    # print("\n")

    # dealer_score = 0
    # while dealer_score < 17:

    #     new_card = deck.pick_card()
    #     if new_card == "ACE":
    #         if dealer_score - MAX_NUMBER >= 11:
    #             dealer_score += 11
    #         else:
    #             dealer_score += 1
    #     else:
    #         dealer_score += new_card
    
    # if dealer_score > 21:
    #     print( "Dealer has bust, all players win.")

    # else:
    #     print("GAME RESULTS")
    #     print("\n")
    #     for i in range(len(player_hands)):
    #         player_score = player_hands[i].score
    #         if player_score <= 21 and player_score > dealer_score:
    #             print("Player " + str(i + 1) + " has beat the dealer")
    #         if player_score == dealer_score:
    #             print("Player " + str(i + 1) + " has tied with the dealer")
    #         else:
    #             print("Player " + str(i + 1) + " has not beaten the dealer")


    

if __name__ == '__main__':
    play()
