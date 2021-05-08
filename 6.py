# from game_data import data
# from art import logo
# from art import vs
import random
# from replit import clear
# print(logo)
random_numberA = int(random.randint(0,49))
random_numberB = int(random.randint(0,49))

followersA = data[random_numberA]["follower_count"]
followersB = data[random_numberB]["follower_count"]

repeat_again = True

def user_A():
  
  nameA = (data[random_numberA]["name"])
  descriptionA = (data[random_numberA]["description"])
  countryA = (data[random_numberA]["country"])
  print(f"Compare A: {nameA}, {descriptionA}, {countryA}\n")
  

def user_B():
  
  nameB = (data[random_numberB]["name"])
  descriptionB = (data[random_numberB]["description"])
  countryB = (data[random_numberB]["country"])
  print(f"Compare B: {nameB}, {descriptionB}, {countryB}\n")
  
counter = 0

while repeat_again == True:
  user_A()

  print(vs)

  user_B()

  user_choice = input("Who has more followers? Type 'A' or 'B': ")
  

  if user_choice == 'A' and followersA>followersB:
    counter += 1
    print(f"You're right! Score {counter}")
    followersB = data[random_numberB]["follower_count"]
    repeat_again = True

  elif user_choice == 'B' and followersA>followersB:
    counter += 0
    # clear()
    # print(logo)
    print(f"You're wrong! Your final score is {counter}")
    repeat_again = False

  elif user_choice == 'A' and followersA<followersB:
    # clear()
    counter += 0
    # print(logo)
    print(f"You're wrong! Your final score is {counter}")
    repeat_again = False

  elif user_choice == 'B' and followersA<followersB:
    counter += 1
    print(logo)
    print(f"You're right! Current score {counter}")
    followersB = followersA
    repeat_again = True


