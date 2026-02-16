# Rock-Paper-Scissors: Use dict for choices, loop 5 rounds with random (import random), track wins with set.
import random

choices= { 1:"Rock", 2:"Paper", 3:"Scissors"}

winner = set()   # track winner 

user_score = 0
computer_score = 0

print("--- Rock--Paper--Scissors---")

for round_n in range(1,6):    # loop for 5 rounds
    print(f"Round {round_n}")

#user input
    user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissor:- "))

    if user_choice not in choices:
        print("Invalid choice...!!!  Skip round")
        continue

# computer choice
computer_choices = random.randint(1,3)

print("You chose:", choices[user_choice])
print("Computer chose:", choices[computer_choices])

#game logic

if user_choice == computer_choices:
    print("It is a tie..!!!")
elif(
    (user_choice == 1 and computer_choices== 3)or
    (user_choice == 2 and computer_choices== 1)or
    (user_choice == 3 and computer_choices== 2)
):
    print("You win thw Game...🥳🥳🥳")
    user_score =+ 1
    winner.add("User")
else:
    print("Computer win this round...")
    computer_score += 1
    winner.add("computer")

#result
print("")
print("===Final Result===")
print("User Score:", user_score)
print("Computer score:", computer_score)

print("winner set:", winner)

if user_score > computer_score:
    print("Overall Winner is : User")
elif computer_score > user_score:
    print("Overall winner is : computer")
else:
    print("....TIE!!!!....")