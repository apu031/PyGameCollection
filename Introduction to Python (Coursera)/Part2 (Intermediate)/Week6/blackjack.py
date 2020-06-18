# Mini-project #6 - Blackjack

# A simple interactive Blackjack game.

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_SmEMOR1Oz23CzYT.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
sound1 = simplegui.load_sound("https://dl.dropbox.com/s/cjjfjkzdp3s6ped/Joker%20-%20Laugh.mp3")
sound2 = simplegui.load_sound("https://dl.dropbox.com/s/dj9eh0qhnwm585r/Desperados%201.mp3")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = "Hit or stand ?"
score = 0
quitter = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        s = "Hand is " + str(self.hand)
        return s

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        temp_rank = []
        for objct in self.hand:
            hand_value += VALUES[objct.rank]
            temp_rank.append(objct.rank)

        if 'A' not in temp_rank:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
        # compute the value of the hand, see Blackjack video

    def draw(self, canvas, pos):
        canvas.draw_text("Total value = " + str(self.get_value()), [pos[0], pos[1] - 10], 30, "Yellow")
        i = 0
        for objct in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(objct.rank),
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(objct.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + i, pos[1] + CARD_CENTER[1]],
                              CARD_SIZE)
            i += 100


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append((suit, rank))

    def shuffle(self):
        # shuffle the deck
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        l1 = self.deck[-1][0]
        l2 = self.deck[-1][1]
        self.deck.pop()
        card = Card(l1, l2)
        return card

    def __str__(self):
        # return a string representing the deck
        s = "The deck is: " + str(self.deck)
        s += "\nLength of the deck is: " + str(len(self.deck))
        return s


player = Hand()
dealer = Hand()
deck = Deck()


# define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, quitter, score

    outcome = "Hit or stand ?"
    in_play = True

    sound1.rewind()
    sound2.rewind()

    if quitter:
        score -= 1

    player = Hand()
    dealer = Hand()

    deck = Deck()
    deck.shuffle()
    c1 = deck.deal_card()
    c2 = deck.deal_card()
    c3 = deck.deal_card()
    c4 = deck.deal_card()

    player.add_card(c1)
    player.add_card(c3)

    dealer.add_card(c2)
    dealer.add_card(c4)

    quitter = True


def hit():
    # replace with your code below
    global outcome, in_play, player, deck, score, quitter

    # if the hand is in play, hit the player
    if in_play:
        c5 = deck.deal_card()
        player.add_card(c5)

        if player.get_value() > 21:
            outcome = "You have busted. Press:\"Deal\" for new deal."
            score -= 1
            in_play = False
            quitter = False
            sound1.play()

    # if busted, assign a message to outcome, update in_play and score


def stand():
    # replace with your code below
    global outcome, in_play, player, dealer, deck, score, quitter

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        in_play = False
        quitter = False
        if player.get_value() <= 21:
            while dealer.get_value() < 17:
                dealer.add_card(deck.deal_card())

            if dealer.get_value() <= 21:
                if dealer.get_value() >= player.get_value():
                    outcome = "Dealer have won !!! Press:\"Deal\" for new deal."
                    score -= 1
                    sound1.play()
                else:
                    outcome = "You have won !!! Press:\"Deal\" for new deal."
                    score += 1
                    sound2.play()
            else:
                outcome = "Dealer has busted !!! Press:\"Deal\" for new deal."
                score += 1
                sound2.play()
    # assign a message to outcome, update in_play and score


def new_game():
    global score, quitter
    score = 0
    quitter = False
    deal()


def exit():
    sound1.rewind()
    sound2.rewind()
    frame.stop()


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play

    canvas.draw_text("Blackjack", [10, 60], 60, "Fuchsia")
    canvas.draw_text("Dealer", [10, 150], 30, "Navy")
    canvas.draw_text("Player", [10, 350], 30, "Navy")
    canvas.draw_text("Score:  " + str(score), [400, 150], 30, "Navy")
    canvas.draw_text(outcome, [200, 550], 30, "Orange")
    dealer.draw(canvas, [100, 200])
    player.draw(canvas, [100, 400])
    if in_play:
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index("A"),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index("C"))
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [100 + CARD_CENTER[0], 200 + CARD_CENTER[1]], CARD_SIZE)
        canvas.draw_line([50, 180], [300, 180], 40, "Green")


# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_label("", 200)
frame.add_label("Note: If you press deal before completing the round, you will lose point.", 200)
frame.add_label("", 200)
frame.add_label("If you really want to start a new deal without losing points, then press the \"New game\" button.",
                200)
frame.add_label("", 200)
frame.add_button("New Game", new_game, 200)
frame.add_label("", 200)
frame.add_button("Exit", exit, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric