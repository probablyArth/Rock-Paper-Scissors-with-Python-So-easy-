import random

print("""---------------------------------Rock Paper Scissors------------------------
1. Rock
2. Paper
3. Scissors""")

user_choice = int(input('Choose your choice.'))

if user_choice > 3 or user_choice < 1:
    user_choice = input('Please give an valid choice.')

if user_choice == 1:
    user_choice_name = 'Rock'
elif user_choice == 2:
    user_choice_name = "Paper"
else:
    user_choice_name = "Scissors"

print("User's choice is " + user_choice_name)

comp_choice = random.randint(1, 3)
if comp_choice == 1:
    comp_choice_name = "Rock"
elif comp_choice == 2:
    comp_choice_name = "Paper"
else:
    comp_choice_name = "Scissors"

print("Computer's choice is " + comp_choice_name)
print(user_choice_name + ' V\S ' + comp_choice_name)

if (user_choice ==  1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
    result = 'Paper'
    print(result + 'wins!')
elif (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 2):
    result = "Scissors"
    print(result + 'wins!')
else:
    result = "Rock"
    print(result + 'wins!')

if user_choice_name == result:
    winner = 'User'
else:
    winner = "Computer"
print(winner + 'wins')