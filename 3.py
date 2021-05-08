import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Assigning random cards.
user= [0,0]
computer= [0,0]

user[0] = int(random.choice(cards))
user[1] = int(random.choice(cards))

computer[0] = int(random.choice(cards))
computer[1] = int(random.choice(cards))

total_user = 0
total_computer = 0
# Checking total points

def total_points_and_blackjack(total_points_user,total_points_computer):
    for i in user:
      total_points_user += i
      return

    for i in computer:
      total_points_computer += i
      return

    if total_points_computer == 21:
      print("BlackJack! Computer wins")
    elif total_points_user == 21:
      print ("BlackJack! User wins")
    elif total_points_computer == total_user:
      print ("Draw")

# Creating function to check if ace is > 21
def ace_count():
  if user[0] == 11 or user[1] ==11 and total_user > 21:
    if user[0] == 11:
      user[0] = 1
    elif user[1] == 11:
      user[1] = 1
  if computer[0] == 11 or computer[1] ==11 and total_computer > 21:
    if computer[0] == 11:
      computer[0] = 1
    elif computer[1] == 11:
      computer[1] = 1

# 	Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.

def game_ends(user_score, computer_score):
  if user_score > 21:
    print(f"Total score for the user is {user_score}. Computer wins")
  
  elif user_score == 21:
    print(f"Total score for the user is {user_score}. User wins") 
  
  elif computer_score == 21:
    print("Computer wins")


# Using function to check if ace is > 21
ace_count()

# Revealing card from computer
print(f"The card from computer is {computer[0]}")
print(f"Your cards are: {user}")
# Checking if the game should end
game_ends(total_user, total_computer)

# Asking if the user wants another card
choice_another_card = input("Do you want another card? Type 'y' or 'n': ")

if choice_another_card == 'y':
  another_card = True
else:
  another_card = False

while another_card == True:
    new_card = random.choice(cards)
    user.append(new_card)
    print(user)
    total_points_and_blackjack(total_user,total_computer)
    choice_another_card = input("Do you want another card? Type 'y' or 'n': ")
    if choice_another_card == 'y':
      another_card = True
    else:
      another_card = False

def computer_play():
  total_points_and_blackjack(total_user,total_computer)
  print(total_computer)
  new_total_computer = total_computer
  while new_total_computer < 16:
    new_card_computer = random.choice(cards)
    computer.append(new_card_computer)
    for i in computer:
      new_total_computer +=i

computer_play()
total_points_and_blackjack(total_user,total_computer)
if total_user > total_computer:
  print(f"User wins with {total_user} points and the computer has {total_computer}")
  print(f"user has {user} cards, and computer has {computer} cards")
elif total_computer > total_user:
  print(f"Computer wins with {total_computer} points and the user has {total_user}")
  print(f" has {user} cards, and computer has {computer} cards")
elif total_computer == total_user:
  print("Draw")