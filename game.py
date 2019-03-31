# author: Tim Eichinger
# version: 1.0

import random

# The 3 options to choose in the game
options = ["SCISSOR", "STONE", "PAPER"]


# Intro
def printintro():
    print("\n********************************************")
    print("**     WELCOME TO SCISSORS-STONE-PAPER    **")
    print("********************************************\n")


# Starts the game and checks whether the user entered a valid move-number.
# If that is okay, the method checkwinner() is called.
def getusername():
    while True:
        username = input("* Please enter your name: ")
        if username != "":
            break

    print(f"* Your username is: {username}")
    print("\n* Let's start the game! {0:SCISSOR, 1:STONE, 2:PAPER}")

    return username


# starts the game by getting the move from the player.
# And then calls the method checkwinner() for getting the result.
def startgame(username):
    while True:
        usermove = input(f"\n* {username}, please enter your move-number: ")
        if usermove == "0" or usermove == "1" or usermove == "2":
            break

    aimovenum = random.randint(0, 3)
    usermovenum = int(usermove)
    checkwinner(usermove, usermovenum, aimovenum)
    checkforplayagain(username)


# Checks whether the AI or the User has won the game.
def checkwinner(usermove, usermovenum, aimovenum):
    print("\n------------------------------------------")
    if str(aimovenum) == usermove:
        print("* It's a draw!")
        printgameresult(usermovenum, aimovenum)
    elif usermovenum == 0 and aimovenum == 1:
        print("* AI  won!")
        printgameresult(usermovenum, aimovenum)
    elif usermovenum == 0 and aimovenum == 2:
        print("* You  won!")
        printgameresult(usermovenum, aimovenum)
    elif usermovenum == 1 and aimovenum == 0:
        print("* You  won!")
        printgameresult(usermovenum, aimovenum)
    elif usermovenum == 1 and aimovenum == 2:
        print("* AI  won!")
        printgameresult(usermovenum, aimovenum)
    elif usermovenum == 2 and aimovenum == 0:
        print("* AI  won!")
        printgameresult(usermovenum, aimovenum)
    elif usermovenum == 2 and aimovenum == 1:
        print("* You  won!")
        printgameresult(usermovenum, aimovenum)
    print("-----------------------------------------\n")


# prints the result of the game. Especially which move the players have chosen.
def printgameresult(usermovenum, aimovenum):
    print(f"* You chose {options[usermovenum]} and the AI chose {options[aimovenum]}")


# checks if the user wants to play again
def checkforplayagain(username):
    playagain = input("* Do you want to play again? ([Y]Yes , [N]No): ")
    if playagain == "Y":
        startgame(username)
    elif playagain == "N":
        endgame()
    else:
        checkforplayagain(username)


# prints a text when the game ended.
def endgame():
    print("* Thanks for playing with me :)")


if __name__ == '__main__':
    printintro()
    startgame(getusername())
