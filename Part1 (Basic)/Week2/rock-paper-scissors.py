# Rock-paper-scissors-lizard-Spock template

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_5U1TfquE7155pMR.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# importing random module to implement randrange()
import random


# helper functions

def name_to_number(name):
    # Converts the input into all upper case letters
    name = name.upper()

    # Assigning respective number corresponding to each string
    if name == "ROCK":
        return 0
    elif name == "SPOCK":
        return 1
    elif name == "PAPER":
        return 2
    elif name == "LIZARD":
        return 3
    elif name == "SCISSORS":
        return 4
    else:
        return "Error: Invalid Input !!!"


def number_to_name(number):
    # Returning corresponded string to the respective number
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Invalid number! Check the random.randrange() function"


def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print
    ""

    # print out the message for the player's choice
    print
    "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print
    "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    diff_comp2player = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if diff_comp2player == 1 or diff_comp2player == 2:
        print
        "Computer wins!"
    elif diff_comp2player == 3 or diff_comp2player == 4:
        print
        "Player wins!"
    else:
        print
        "Player and computer tie!"


# testing my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# Thanks for evaluating !!!

