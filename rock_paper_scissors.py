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
import random

image = [rock, paper, scissors]
player_choice = int(input("What is your choice? 1.Rock 2.Paper 3.Scissors: "))
cpu_choice = random.randint(1, 3)

# Player 
if player_choice == 1:
  print("Your choice is Rock!")
  print(image[player_choice - 1])

if player_choice == 2:
  print("Your choice is Paper!")
  print(image[player_choice - 1])

if player_choice == 3:
  print("Your choice is Scissors!")
  print(image[player_choice - 1])

# CPU
if cpu_choice == 1:
  print("CPU choice is Rock!")
  print(image[cpu_choice - 1])

elif cpu_choice == 2:
  print("CPU choice is Paper!")
  print(image[cpu_choice - 1])

else:
  print("CPU choice is Scissors!")
  print(image[cpu_choice - 1])

# Check winner
# Player winning conditions
if player_choice == 1 and cpu_choice == 3:
  print("Player wins!")
elif player_choice == 2 and cpu_choice == 1:
  print("Player wins!")
elif player_choice == 3 and cpu_choice == 2:
  print("Player wins!")
# CPU winning conditions
elif player_choice == 1 and cpu_choice == 2:
  print("Computer wins!")
elif player_choice == 3 and cpu_choice == 2:
  print("Computer wins!")
elif player_choice == 3 and cpu_choice == 1:
  print("Computer wins!")
elif player_choice == cpu_choice:
  print("It is a draw!")
else:
  print("You enter an invalid input, you lose!")
