# Implementation of classic arcade game Pong

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_TaTRaKGsnxkgYpm.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

# Importing necessary modules
import simplegui
import random

# Variables to create canvas
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# Variables to define the beginning position of the ball
LEFT = False
RIGHT = True

# Variables to show scores
score1 = 0
score2 = 0

# List to hold the position of the ball on the canvas and the velocity of the ball
ball_pos = [0, 0]
ball_vel = [0, 0]

# Variables to store the status of the displayed colors
ball_color = "Red"
paddle_color = "Green"
line_color = "White"
score_color = "White"

# Variables to show the winner
show_winner = False
left_winner = False

# Variables to create the paddle
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = 0
paddle2_pos = 0
paddle_height = 100
paddle_width = 18


# initialize ball_pos and ball_vel for new ball in the middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # These are lists
    global WIDTH, HEIGHT  # These are ints

    # Note: Suggested Random range for the velocity of the ball could not be implemented
    # Note: So, fixed velocity for the ball was implemented
    if direction:
        ball_vel[0] = 4  # random.randrange(120, 240)
        ball_vel[1] = -4  # random.randrange(60, 180)
        ball_pos[0] = WIDTH / 2 - 30
        ball_pos[1] = HEIGHT / 2
    else:
        ball_vel[0] = -4  # random.randrange(120, 240)
        ball_vel[1] = -4  # random.randrange(60, 180)
        ball_pos[0] = WIDTH / 2 + 30
        ball_pos[1] = HEIGHT / 2


# define event handlers

# To initialize a new game
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  # these are numbers
    global score1, score2  # these are ints
    global RIGHT, LEFT, show_winner, left_winner  # these are booleans
    global ball_color, paddle_color, line_color, score_color  # these are strings

    ball_color = "Red"
    paddle_color = "Green"
    line_color = "White"
    score_color = "White"
    show_winner = False
    left_winner = False

    score1 = 0
    score2 = 0

    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = 0
    paddle2_pos = 0

    # Randomly tossing the starting position of the ball for a new game
    direction = bool(random.randint(0, 1))
    spawn_ball(direction)


# To close the frame
def exit_game():
    frame.stop()


# To draw all the things on the canvas and some important logic calculations
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global ball_color, paddle_color, line_color, score_color, show_winner, left_winner

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, line_color)
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, line_color)
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, line_color)

    # updating ball linearly
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Checking the ambit of the ball
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # drawing the ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, ball_color, ball_color)

    # updating paddle's vertical position
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    # keeping paddles on the screen
    if paddle1_pos < 0:
        paddle1_pos = 0
    elif paddle1_pos + paddle_height > HEIGHT:
        paddle1_pos = HEIGHT - paddle_height

    if paddle2_pos < 0:
        paddle2_pos = 0
    elif paddle2_pos + paddle_height > HEIGHT:
        paddle2_pos = HEIGHT - paddle_height

        # drawing paddles
    canvas.draw_line([0, paddle1_pos], [0, paddle1_pos + paddle_height], paddle_width, paddle_color)
    canvas.draw_line([WIDTH, paddle2_pos], [WIDTH, paddle2_pos + paddle_height], paddle_width, paddle_color)

    # determining whether paddle and ball collide

    if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + paddle_height and ball_pos[0] >= (
            WIDTH - PAD_WIDTH) - BALL_RADIUS:
        # if the ball touches the paddle, velocity is increased by 10%
        ball_vel[0] = -ball_vel[0] * 1.1

    elif ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + paddle_height and ball_pos[
        0] <= PAD_WIDTH + BALL_RADIUS:
        # if the ball touches the paddle, velocity is incresed by 10%
        ball_vel[0] = -ball_vel[0] * 1.1

    elif ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        # if the ball misses the paddle, score is being increased on the opposite side
        # and the ball is spawned from the losing side
        score1 += 1
        RIGHT = False
        spawn_ball(RIGHT)

    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        # if the ball misses the paddle, score is being increased on the opposite side
        # and the ball is spawned from the losing side
        score2 += 1
        RIGHT = True
        spawn_ball(RIGHT)

    # drawing the scores
    canvas.draw_text(str(score1), (WIDTH / 2 - 40, 40), 50, score_color)
    canvas.draw_text(str(score2), (WIDTH / 2 + 25, 40), 50, score_color)

    # checking to turn off the display conditions, and setting up the winner variables
    if score1 == 10 and score2 < 10:
        ball_color = 'Black'
        paddle_color = 'Black'
        line_color = 'Black'
        score_color = 'Black'
        show_winner = True
        left_winner = True

    elif score2 == 10 and score1 < 10:
        ball_color = 'Black'
        paddle_color = 'Black'
        line_color = 'Black'
        score_color = 'Black'
        show_winner = True
        left_winner = False

    # showing the winner once it is found
    if show_winner:
        music.play()
        canvas.draw_text("Congratulations", (0, 150), 92, "Gold")
        if left_winner:
            canvas.draw_text("Left Side Won !!!", (90, 250), 60, "Gold")
        else:
            canvas.draw_text("Right Side Won !!!", (70, 250), 60, "Gold")

        canvas.draw_text("Press the buttons from the control pannel.", (140, 390), 20, "White")


# To perform the actions for moving the paddle
def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 10
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -10
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 10
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -10


# To perform the actions for moving the paddle
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

    # create frame


frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

frame.add_label("Instructions:")
frame.add_label("1. To Win the game, either one of you needs to have a 10 points !!!", 200)
frame.add_label("")
frame.add_label("2. Left player keys are 'w' = Upward, and 's' = downward", 200)
frame.add_label("")
frame.add_label("3. Right player keys are 'Upper Arrow' = Upward, and 'Lower Arrow' = downward", 200)
frame.add_label("")
frame.add_label("Enjoy the game !!!")
frame.add_label("")
frame.add_button("Restart!", new_game, 200)
frame.add_label("")
frame.add_button("Exit!", exit_game, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Loading music (Ref: Desperados 2: Music Clip)
music = simplegui.load_sound(
    "https://dl-web.dropbox.com/get/Desperados%201.mp3?_subject_uid=220055480&w=AABsaCLWEbsE4cGgEdqjYOs9quXBqcY1igby6BWbKC4yig")

# start frame
new_game()
frame.start()