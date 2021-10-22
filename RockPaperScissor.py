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

game_images=[rock,paper,scissors]

user_input=int(input("Type 0 for Rock, 1 for paper, 2 for scissors\n"))
print(game_images[user_input])

import random
computer_choice=random.randint(0,2)
print("Computer Choice :")
print(game_images[computer_choice])


if user_input==0 and computer_choice==0:
  print("Draw")
elif user_input==0 and computer_choice==1:
  print("You lose")
elif user_input==0 and computer_choice==2:
  print("You won")
elif user_input==1 and computer_choice==0:
  print("You won")
elif user_input==1 and computer_choice==1:
  print("Draw")
elif user_input==1 and computer_choice==2:
  print("You lose")
elif user_input==2 and computer_choice==0:
  print("You lose")
elif user_input==2 and computer_choice==1:
  print("You won")
elif user_input==2 and computer_choice==2:
  print("Draw")
else:
  print("Please provide a valid input between 0 to 2")