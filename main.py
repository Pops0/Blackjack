############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from art import logo
from art import cross
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

round = 0
dealer_round = 0
user_hand = []
user_score = 0
dealer_hand = []
dealer_score = 0
should_resume = True
dealer_stand = False


def dealer():
    global dealer_hand
    global dealer_score
    global dealer_round
    global dealer_stand
    dealer_round += 1
    if dealer_score < 17:
        if dealer_round == 1:
            dealer_card_one = [random.choice(cards)]
            dealer_card_two = []
            dealer_card_one.extend(dealer_card_two)
            dealer_hand = dealer_card_one
            dealer_score = sum(dealer_hand)
        elif dealer_round == 2:
            dealer_card_two = [random.choice(cards)]
            dealer_hand.extend(dealer_card_two)
            dealer_score = sum(dealer_hand)
        elif dealer_round == 3:
            dealer_card_three = [random.choice(cards)]
            dealer_hand.extend(dealer_card_three)
            dealer_score = sum(dealer_hand)
        elif dealer_round == 4:
            print("Round 4 dealer, checkWinner()")
    elif dealer_score >= 17:
        print(
            f"The dealer STANDS, their hand consisting of:{dealer_hand}. Their score of {dealer_score}.")
        dealer_stand = True
        checkWinner()


def ask():
    global user_hand
    global user_score
    global dealer_score
    global dealer_score
    global should_resume
    print(logo)
    query = input("\n\nDo you want to hit or stand?: ").lower()
    def checkAce():
        if user_score > 17:
            cards[0] = 1
            print("DBG ACE ALTERED")
    if query == 'hit':
        global round
        round += 1
        checkAce()
        if round == 1:
            card_one = [random.choice(cards)]
            card_two = [random.choice(cards)]
            card_one.extend(card_two)
            user_hand = card_one
            user_score = sum(user_hand)
            print(
                f"\nYour hand currently consists of:{user_hand}. Your score of {user_score}.")
            dealer()
            print(
                f"The dealer's hand currently consists of:{dealer_hand}. Their score total is {dealer_score}.")
            checkWinner()
        elif round == 2:
            card_three = [random.choice(cards)]
            user_hand.extend(card_three)
            user_score = sum(user_hand)
            print(
                f"\nYour hand currently consists of: {user_hand}. Your score of {user_score}.")
            dealer()
            print(
                f"The dealer's hand currently consists of:{dealer_hand}. Their score total is {dealer_score}.")
            checkWinner()
        elif round == 3:
            card_four = [random.choice(cards)]
            user_hand.extend(card_four)
            user_score = sum(user_hand)
            print(
                f"\nYour hand currently consists of: {user_hand}. Your score of {user_score}.")
            dealer()
            print(
                f"The dealer's hand currently consists of:{dealer_hand}. Their score total is {dealer_score}.")
            checkWinner()
        elif round == 4:
            print("Round 4, faulty")
    elif query == 'stand':
        print(
            f"\nYour hand currently consists of: {user_hand}. Your score of {user_score}.")
        if dealer_stand == False:
            dealer()
            print(
                f"The dealer's hand currently consists of:{dealer_hand}. Their score total is {dealer_score}.")
        elif dealer_stand == True:
            dealer()
    else:
        print(cross)
        print("Please type either 'hit' or 'stand'")
        ask()


def endGame():
    global should_resume
    should_resume = False
    print("Thank you for playing")
    exit()


def checkWinner():
    if user_score == 21 and dealer_score == 21:
        print("It's a DUAL")
        endGame()
    elif user_score == 21:
        print("You WIN!!!😁")
        endGame()
    elif user_score >= 22:
        print("Bust!😥")
        endGame()
    elif dealer_score == 21:
        print("You lose!😥")
        endGame()
    elif dealer_score >= 22:
        print("You WIN!!!😁")
        endGame()
    elif dealer_stand == True and user_score > dealer_score:
        print("You WIN!!!😁")
        endGame()
    elif dealer_stand == True and user_score < dealer_score:
        print("You lose!😥")
        endGame()
    elif dealer_stand == True and user_score == dealer_score:
        print("Standoff!")
        endGame()
    else:
        ask()


while should_resume == True:
    print("DBG should resume == True")
    ask()
