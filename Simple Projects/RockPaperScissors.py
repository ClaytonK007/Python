import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Select your choice choice:\n1. Rock\n2. Paper\n3. Scissors\n4. Exit")
    choice = int(input("Enter choice your choice: "))

    while choice > 4 or choice < 1:
        choice = int(input("Please select correct option: "))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"
    else:
        break

    print("Your choice is: ", choice_name)
    print("Now its the computers turn to choose...")

    com_choice = random.randint(1, 3)

    if com_choice == 1:
        com_choice_name = "Rock"
    elif com_choice == 2:
        com_choice_name = "Paper"
    else:
        com_choice_name = "Scissors" 

    print("Computers choice is: ", com_choice_name)
    print(choice_name, "vs", com_choice_name)

    if choice == com_choice:
        result = "Draw"
    elif (choice == 1 and com_choice == 2) or (com_choice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 2 and com_choice == 3) or (com_choice == 2 and choice == 3):
        result = "Scissors"
    elif (choice == 1 and com_choice == 3) or (com_choice == 1 and choice == 3):
        result = "Rock"

    if result == "Draw":
        print("<==DRAW==>")
    elif result == choice_name:
        print("<==YOU WIN!!!==>")
    else:
        print("<==COMPUTER WINS.==>")

    print("Do you want to play again? Y/N:")
    ans = input().lower()
    if ans == "n":
        break 

print("Thank you for playing :)")