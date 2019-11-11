import time
import random

print("Rock paper scissors by Alex Simpson.")
time.sleep(2)
print("Okay, best of 3, let's go!")

rps = ['rock', 'paper', 'scissors']

win = 0
lose = 0


def initialize():
    global randomn
    global win
    global lose
    randomn = random.randint(0, 2)
    if win >= 3:
        print("Congratulations! You won!")
        time.sleep(6)
        request = input("Would you like to play again? ")
        if request == "yes" or request == "y":
            win = 0
            lose = 0
            initialize()
        elif request == "no" or request == "n":
            print("Thank you for playing!")
            return
        else:
            print("That's not a relevant answer to my question. Thanks for playing!")
            return
    if lose >= 3:
        print("I win, better luck next time!")
        request = input("Would you like to play again? ")
        if request == "yes" or request == "y":
            win = 0
            lose = 0
            initialize()
        elif request == "no" or request == "n":
            print("Thank you for playing!")
            return
        else:
            print("That's not a relevant answer to my question. Thanks for playing!")
            return
    if randomn == 0:  # Rock
        rock()
    elif randomn == 1:  # Paper
        paper()
    elif randomn == 2:  # Scissors
        scissors()

    # uinput = input("Rock, paper or scissors!?: ")


def rock():
    # print("Launching rock function.")
    uinput = input("Rock, paper or scissors!?: ")
    if uinput == rps[0]:  # Rock
        print("Draw!")
        initialize()
    elif uinput == rps[1]:  # Paper
        print("Agh, I chose rock...")
        global win
        win += 1
        initialize()
    elif uinput == rps[2]:  # Scissors
        print("I chose rock, I win!")
        global lose
        lose += 1
        initialize()
    elif uinput == "quit":
        print("Thank you!")
    else:
        print("Come on, choose something relevant to what we're doing here...")
        initialize()


def paper():
    # print("Launching paper function.")
    uinput = input("Rock, paper or scissors!?: ")
    if uinput == rps[0]:  # Rock
        print("I chose paper, I win!")
        global lose
        lose += 1
        initialize()
    elif uinput == rps[1]:  # Paper
        print("Draw!")
        initialize()
    elif uinput == rps[2]:  # Scissors
        print("Agh, I chose paper...")
        global win
        win += 1
        initialize()
    elif uinput == "quit":
        print("Thank you!")
    else:
        print("Come on, choose something relevant to what we're doing here...")
        initialize()


def scissors():
    # print("Launching scissors function.")
    uinput = input("Rock, paper or scissors!?: ")
    if uinput == rps[0]:  # Rock
        print("Agh, I chose scissors...")
        global win
        win += 1
        initialize()
    elif uinput == rps[1]:  # Paper
        print("I chose scissors, I win!")
        global lose
        lose += 1
        initialize()
    elif uinput == rps[2]:  # Scissors
        print("Draw!")
        initialize()
    elif uinput == "quit":
        print("Thank you!")
    else:
        print("Come on, choose something relevant to what we're doing here...")
        initialize()


initialize()
