import random
import sys


cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_again = False

while play_again == False:

    # Assigning random cards.
    user= [0,0]
    computer= [0,0]

    total_points_user = 0
    total_points_computer = 0

    user[0] = int(random.choice(cards))
    user[1] = int(random.choice(cards))

    computer[0] = int(random.choice(cards))
    computer[1] = int(random.choice(cards))
    
    def play_again_function():
        another_game=input("Would you like to play another game? Type 'y' or 'n': ")
        if another_game == 'y':
          play_again = False
          return
          
        else:
          play_again = True
          return
          


    # Detecting when user has blackjack.
    for i in user:
        total_points_user += i
        
    # Detecting when computer has blackjack.
    for i in computer:
        total_points_computer += i

    if total_points_computer == 21:
        print("Computer wins! ")
        sys.exit()

    elif total_points_user == 21 and total_points_computer != 21:
        print("User wins! ")
        sys.exit()

            
        print(total_points_computer)
        print(total_points_user)

        # Check if ace is > 21
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


    # Revealing first card from computer to the user.

    print(f"The card from computer is {computer[0]}")

    # Asking if the user wants another card
    another_card = True
    while another_card == True:
      choice_another_card = input(f"Your points are {total_points_user}.  Do you want another card? Type 'y' or 'n': ")

      if choice_another_card == 'y':
        new_card_user = int(random.choice(cards))
        user.append(new_card_user)
        total_points_user = 0 # we make the points 0  in order to count them again
        for i in user:
          total_points_user += i
        print(f"Your points are {total_points_user}\n")
        if total_points_user > 21:
            print(f"Your points are {total_points_user} so, you lost the game.\n")
      else:
        print("OK. You don't want new cards.")
        another_card = False


    # Computer playing

    while total_points_computer < 16:
      new_card_computer = int(random.choice(cards))
      computer.append(new_card_computer)
      total_points_computer = 0 # we make the points 0  in order to count them again
      for i in computer:
        total_points_computer += i
      
    if total_points_computer > 21 and total_points_user > 21:
      print("It's a daw\n")
      print(f"Your points are: {total_points_user}")
      print(f"Computer points are: {total_points_computer}\n")
      play_again_function()
    elif total_points_computer > 21 and total_points_user < 21:
      print("It's a victory for the user! \n")
      print(f"Your points are: {total_points_user}")
      print(f"Computer points are: {total_points_computer}\n")
      play_again_function()
    elif total_points_computer < 22 and total_points_computer > total_points_user:
      print("It's a victory for computer\n")
      print(f"Your points are: {total_points_user}")
      print(f"Computer points are: {total_points_computer}\n")
      play_again_function()
    elif total_points_user < 22 and total_points_user > total_points_computer:
      print("It's a victory for the user\n")
      print(f"Your points are: {total_points_user}")
      print(f"Computer points are: {total_points_computer}\n")
      play_again_function()
    elif total_points_user == total_points_computer:
      print("It's a draw.")
      print(f"Your points are: {total_points_user}")
      print(f"Computer points are: {total_points_computer}\n")
      play_again_function()
    elif total_points_user >21:
      print("You lose.")
      print(f"Your points are: {total_points_user}")
      print(f"Computer points are: {total_points_computer}\n")
      play_again_function()





