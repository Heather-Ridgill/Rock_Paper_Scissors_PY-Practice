# Human playing against a computer

import random

wins = 0
ties = 0
losses = 0
print("Welcome to Rock, Paper, Scissors!")
print("Win: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")

computer = random.randint(1,3)
user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))

while not user == 9:
    #When user chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer choser rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...computer wins :( ")
            losses += 1
        else:
            print("Computer chose scissors...you win! :) ")
            wins += 1

    #When user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock..you win! :) ")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        else:
            print("Computer chose scissors...computer wins :( ")
            losses += 1

    #When user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...computer wins :( ")
            losses += 1
        elif computer == 2:
            print("Computer choser paper...you win! :) ")
            wins += 1
        else:
            print("Computer chose scissors...tie!")
            ties += 1
    else:
        print("Invalid Selection. Please try again.")

    #Updates Stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    #Prompting user to make another selection
    print("Please choose to continue...")

    computer = random.randint(1,3)
    user = int(input("[1] Rock [2] Paper [3] Scissors [4] Quit\n"))



            
