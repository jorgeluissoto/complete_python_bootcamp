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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_user = random.randint(0, 2)

print(game_images[user])

print("Computer Chose:")

print(game_images[computer_user])

if user == computer_user:
        print("Draw")
elif user == 0 and computer_user ==1:
        print("You Lose")
elif user == 0 and computer_user ==2:
        print("You Won!")
elif user == 1 and computer_user ==0:
        print("You Win")
elif user == 1 and computer_user ==2:
        print("You Lose!")
elif user == 2 and computer_user ==1:
        print("You Won")
elif user == 2 and computer_user ==0:
        print("You Lose!")