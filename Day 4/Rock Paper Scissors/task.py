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


import random

three = [rock, paper,scissors]

result = random.randint(0,2)
comp = three[result]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
user_choice = three[user]

print("You choose:")
print(user_choice)
print("Computer choose:")
print(comp)

if user >= 3 or user < 0:
    print("You typed an invalid number. You lose!")
elif user == 0 and result == 2:
    print("You win!")
elif result == 0 and user == 2:
    print("You lose!")
elif result > user:
    print("You lose!")
elif user > result:
    print("You win!")
elif result == user:
    print("It's a draw!")

