import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def play():
  weapon_list = [paper, rock, scissors]
  computer_selection = random.randint(0, 2)

  try:
    player_selection = int(input("Let's play Rock-Paper-Scissor.\nType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
  except ValueError:
    player_selection = int(input("Please input correct number.\nType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
  
  if player_selection > len(weapon_list):
    player_selection = int(input("Please input correct number.\nType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
  else:
    computer_weapon = weapon_list[computer_selection]
    player_weapon = weapon_list[player_selection]

  print(f"You pick:\n{player_weapon}\nComputer pick:\n{computer_weapon}")

  if player_selection == computer_selection:
    print("Draw")
  elif player_selection == 0 and computer_selection == 2:
    print("You win")
  elif player_selection == 1 and computer_selection == 0:
    print("You win")
  elif player_selection == 2 and computer_selection == 1:
    print("You win")
  else:
    print("You lose")

  retry = input("Do you want to play again? Type 'y' or 'n': ")
  
  if retry != 'y':
    print("Game Over.")
  else:
    play()

play()