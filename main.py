from random import choice
from curses import wrapper


def userChoice():
    user = input("Hello, welcome to Rock Paper Scissors! Please pick one.")
    return user


def computerChoice():
    objects = ['rock', 'paper', 'scissors']
    computer = choice(objects)
    return computer


def rockChoice():
    computer = computerChoice()
    if computer.lower() == "rock":
        print("We tied!")
    if computer.lower() == "paper":
        print("You lost!")
    elif computer.lower() == "scissors":
        print("You won!")


def scissorsChoice():
    computer = computerChoice()
    if computer.lower() == "scissors":
        print("We tied!")
    if computer.lower() == "rock":
        print("You lost!")
    elif computer.lower() == "paper":
        print("You won!")


def paperChoice():
    computer = computerChoice()
    if computer.lower() == "paper":
        print("We tied!")
    if computer.lower() == "scissors":
        print("You lost!")
    elif computer.lower() == "rock":
        print("You won!")


def gameOver():
    playAgain = input("Do you want to play again? Click any button to continue, or click 'N' to exit.")
    if playAgain.lower() == "n":
        quit()


def play():
    while True:
        computer = computerChoice()
        user = userChoice()
        computerChoice()
        if user.lower() == "rock":
            rockChoice()
            gameOver()
        elif user.lower() == "scissors":
            scissorsChoice()
            gameOver()
        elif user.lower() == "paper":
            paperChoice()
            gameOver()
        else:
            print("That's not a valid input, please try again!")
            break


def main():
    while True:
        play()


main()

# if computer == user:
#   print("I picked {} and you picked {}".format(computer, user))
