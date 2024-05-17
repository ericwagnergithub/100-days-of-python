import random
print("Rock, Paper, Scissors!")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

computer_choice = random.randint(0,2)

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

ascii_list = [rock, paper, scissors]

print(ascii_list[player_choice])

print("\n Computer chose: \n")
print(ascii_list[computer_choice])


if player_choice == computer_choice:
    print("It is a tie.")
if player_choice == 0 and computer_choice == 1:
    print("You lose.")
if player_choice == 1 and computer_choice == 2:
    print("You lose.")
if player_choice == 2 and computer_choice == 0:
    print("You lose.")

else:
    print("You Win!")