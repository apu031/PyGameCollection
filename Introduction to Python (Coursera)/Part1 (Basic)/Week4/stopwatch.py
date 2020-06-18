# template for "Stopwatch: The Game"

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_L62YisLKKPm2dXe.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

# Importing Modules
import simplegui

# define global variables

# For having a 0.1 second interval in calling the time function
interval = 100

# Time at any moment
phase = 0

# Marker of clicking stop
stopage = True

# Coordinates for printing hitting status [x, y]
x = 0
y = 0

# Coordinates for the canvas size
width = 400
height = 400

# Taking A, and D of format A:BC.D to print in the middle
A = 0
D = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    # Importing global A, and D to facilitate in printing in the middle
    global A
    global D
    A = t // 600
    BCD = t % 600
    BC = BCD // 10
    B = BC // 10
    C = BC % 10
    D = BCD % 10

    # Returning the main string format to be displayed
    return str(A) + ":" + str(B) + str(C) + "." + str(D)


# Function to check if complete second has been hit or not
def won_or_missed_check(D):
    global x, y
    y += 1

    # Checking if the tenth of second is zero or not
    if D == 0:
        x += 1


# Function for displaying hitting status
def displaying_hitting_status():
    return str(x) + "/" + str(y)


# define event handlers for buttons; "Start", "Stop", "Reset"

# For running the watch
def start():
    # Setting the stopage marker as False so that stop can give proper value
    global stopage
    stopage = False

    # Starting the timer function
    timer.start()


# For halting the watch
def stop():
    # Stopping the timer function
    timer.stop()

    global stopage

    # Checking if consequtive stop buttons have been clicked or not
    if not stopage:
        # Setting the stopage marker as True to avoid consequtive hitting values
        stopage = True

        # Calling the function to check the hitting status
        won_or_missed_check(D)


# Fuction to reset the whole game
def reset():
    # Stopping the timer function
    timer.stop()

    # Resetting the rest of the global variables
    global phase, x, y, stopage
    phase = 0
    x = 0
    y = 0
    stopage = True


# Function to exit the game
def exit():
    frame.stop()


# define event handler for timer with 0.1 sec interval
def increment_of_phase():
    # Increasing the time with repeated creation of timer
    global phase
    phase += 1


# define draw handler
def draw(canvas):
    # Printing the A:BC.D format in the middle of the canvas
    canvas.draw_text(format(phase), [width / 2 - 75 - len(str(A)) * 10, height / 2], 64, "Silver")

    # Printing the hitting status at the top right corner of the canvas
    canvas.draw_text(displaying_hitting_status(), [width - 150, height - 360], 44, "Gold")


# create frame
frame = simplegui.create_frame("STOP WATCH", width, height)

# register event handlers
frame.add_button("Start", start, 150)
frame.add_label("")
frame.add_button("Stop", stop, 150)
frame.add_label("")
frame.add_button("Reset", reset, 150)
frame.add_label("")
frame.add_button("Exit The Game", exit, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, increment_of_phase)

# start frame
frame.start()

# Thanks for evaluating the code