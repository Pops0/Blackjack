############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# from art import logo
# from art import cross
# from replit import clear
import random
import math

# print(logo)
cards = [2,4,10]
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# User interface
# --------------------------------------------------------------

total_hits = 2
first_card = random.choice(cards)
second_card = random.choice(cards)
user_score = first_card + second_card
user_hand = [first_card, second_card]
stop_game = False
promt = f"\nYour cards are: {user_hand}. Your current score is: {user_score}"
if user_score >= 18:
  cards[0] = 1
# --------------------------------------------------------------
  
# Dealer's interface
# --------------------------------------------------------------

first_card_dealer = random.choice(cards)
second_card_dealer = random.choice(cards)
dealer_score = first_card_dealer + second_card_dealer
dealer_hand = [first_card_dealer, second_card_dealer]
dealer_promt = f"\nThe dealer's cards are: {dealer_hand}. Your current score is: {dealer_score}"
print(promt)
print(dealer_promt)
if dealer_score >= 17:
  cards[0] = 1
# --------------------------------------------------------------
card_request = input("\nDo you want to Hit or pass?: ")

def end_game():
    global stop_game
    stop_game = True

def promt_check():
  if total_hits > 0:
    return True
  elif total_hits == 0:
    return False

def read_var():
    global user_score
    global new_user_score

def hit_action(): 
  global total_hits
  #global new_user_score
  total_hits -= 1
  new_card = random.choice(cards)
  user_hand.append(new_card)
  new_user_score = user_score + new_card
  display()
  return(new_user_score)
  
def hit_dealer_action(): 
  global total_hits_dealer
  global dealer_user_score
  total_hits_dealer -= 1
  dealer_card = random.choice(cards)
  dealer_hand.append(dealer_card)
  dealer_user_score = dealer_score + dealer_card
  display()
  return(dealer_user_score)

def display():
  check_winner()
  promt = f"Your cards are: {user_hand}. Your current score is: {new_user_score}"
  print(promt)
  print(dealer_promt)
  # print(f"Total hits: {total_hits}")
  card_request = input("Do you want to Hit or pass? : ").lower()
  check()

def check():
  if stop_game == True:
    print("Thank you for playing!")
    exit()
  elif (promt_check() == True) and (card_request == "hit" or card_request == "pass"):
    read_var()
    check_winner()
    hit_action()
  elif promt_check() == False:
    print("You can't hit anymore")
    # pass function
  elif card_request == "Pass":
    print("Passed")
    # pass function
  elif card_request != "hit" or card_request != "pass":
     # clear()
     # print(cross)
     print("PLEASE TYPE EITHER 'HIT' OR 'PASS'")

def check_winner():
  if user_score == 21:
    print("You win!!!")
    end_game()
    check()
  elif new_user_score == 21:
    print("You win!!!")
    end_game()
    check()
  elif new_user_score >= 22:
    print("Bust!")
    end_game()
    check()
  elif dealer_score == 21:
    print("You lose!")
    end_game()
    check()
  elif dealer_score >= 22:
    print("You win!")
    end_game()
    check()
  elif dealer_score == 21 and new_user_score == 21:
    print("It's a DUEL!")
    end_game()
  check()
  
check()

