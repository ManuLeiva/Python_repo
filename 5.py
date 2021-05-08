#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Number")
print("I'm thinking for a number between 1 and 100")
chose_dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guess_the_number():
  attempts = 0
  you_won = False
  while you_won == False:
    number_guessed = int(input("Please, guess a number: \n"))
    print(type(number_guessed))
    if number_guessed == random_number:
      print("You win! Congratulations!")
      you_won = True
    elif number_guessed != random_number:
      print("It is not correct. ")
      attempts +=1
      if attempts == guesses:
        print("You've lost.")
        you_won = True
      


if chose_dificulty == 'easy':
  guesses = 10
  random_number = random.randint(1, 100)
  print(random_number)
  guess_the_number()

elif chose_dificulty == 'hard':
  guesses = 5
  random_number = random.randint(1, 100)
  print(random_number)
  print(type(random_number))
  guess_the_number()