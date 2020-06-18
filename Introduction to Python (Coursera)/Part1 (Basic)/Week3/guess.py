# Code for GUESS THE NUMBER game

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_rxmFqO3WF3SBm7J.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

import simplegui
import math
import random

# Declaring global variables
secret_number = 100
n = 0
chances = 0


# helper function to start and restart the game
def new_game():
    # Checking which action to perforn
    if n == 10:
        range1000()
    else:
        range100()


# define event handlers for control panel
def range100():
    # Letting function to import global variables
    global secret_number, chances, n

    # Setting range
    high = 100
    low = 0

    # Putting random values 0, 1, 2, ..., 99
    secret_number = random.randrange(low, high)

    # Setting up chances
    n = int(math.ceil(math.log(high - low + 1) / math.log(2)))
    chances = n

    # Printing New game information
    print
    "\nNew Game!!! Range is from 0 to 100"

    # Printing the number of remaining chances
    print
    "Number of remaining chances is ", chances


def range1000():
    # Letting function to import global variables
    global secret_number, chances, n

    # Setting range
    high = 1000
    low = 0

    # Putting random values 0, 1, 2, ..., 999
    secret_number = random.randrange(low, high)

    # Setting up chances
    n = int(math.ceil(math.log(high - low + 1) / math.log(2)))
    chances = n

    # Printing New game information
    print
    "\nNew Game!!! Range is from 0 to 1000"

    # Printing the number of remaining chances
    print
    "Number of remaining chances is ", chances


def input_guess(guess):
    # Checking if the input was an integer
    try:
        guessed_number = int(guess)
    except:
        # Throughing exception without terminating the program
        print
        "\nINVALID INPUT !!! Try again !!!\n"
        return new_game()

    # Printing the input number
    print
    "\nGuess was ", guessed_number

    # Reducing the value of chances
    global chances
    chances -= 1

    # Printing the number of remaining chances
    print
    "Number of remaining chances is ", chances

    # Checking the winning and losing condition
    if chances == 0 and secret_number != guessed_number:
        print
        "You have lost the game."
        print
        "\nThe number was ", secret_number
        print
        "Try again."
        return new_game()
    elif secret_number == guessed_number:
        print
        "Correct!"
        return new_game()
    elif secret_number < guessed_number:
        print
        "Lower!"
    else:
        print
        "Higher!"


# create frame
frame = simplegui.create_frame("GUESS THE NUMBER!", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter Your Guess", input_guess, 200)

# call new_game
new_game()

# Thanks for evaluating