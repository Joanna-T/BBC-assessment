from src.constants import MAX_NUMBER

class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.status = "PLAYING"

    def add_to_hand(self,card):

        self.cards.append(card)

        self.__calculate_score()


    def stand(self):
        self.status = "STANDING"

    def print_hand(self):
        for card in self.cards:
            print(card, end=" ")
        print("\n")

    def print_score(self):
        if self.score == -1:
            print("INVALID SCORE - BUST")
        else:
            print("MAXIMUM SCORE = " + str(self.score))
        
        print("\n")

    def __calculate_score(self):
        total_score = 0
        ace_counter = 0

        for card in self.cards:
            if card.value == 0:
                ace_counter += 1
                continue
            total_score += card.value
        
        #score goes over 21 without aces
        if total_score > MAX_NUMBER:
            self.score = -1
            self.status = "BUST"


        #no aces and total score is less than or equal to 21
        if total_score <= MAX_NUMBER and ace_counter == 0:
            self.score = total_score

        #calculate maximum value that be gained with the aces
        if total_score <= MAX_NUMBER and ace_counter > 0:
            difference = MAX_NUMBER - total_score

            # there can only one ace with value of 11 
            # when the difference between score so far and 21 is greater than this
            if difference < 11 and ace_counter <= difference:
                self.score = ace_counter + total_score

            elif difference >= 11 and ace_counter - 1 + 11 <= difference:
                self.score = ace_counter - 1 + 11 + total_score

            elif difference >= 11 and ace_counter <= difference and ace_counter - 1 + 11 > difference:
                self.score = ace_counter + total_score
            #score is greater than 21
            else:
                self.score = -1
                self.status = "BUST"



            


            
            
