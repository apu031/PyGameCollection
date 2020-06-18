# implementation of card game - Memory
# A simgple interactive IQ checking game with interactive music.
# If you are a fan of CardCaptor anime like me, you would enjoy playing the game.

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_i1HmrwqhNFciqFy.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

import simplegui
import random

# Loading sound and images (Copyright - Sound from Desperados2 and Cards are from Cardcaptor Sakura)
sound1 = simplegui.load_sound("https://www.dropbox.com/s/du6tohvysycvz1b/CardCaptorThemeSong.mp3?dl=1")
sound2 = simplegui.load_sound("https://www.dropbox.com/s/dbdr33hthnu8upk/Magical%20Chim.mp3?dl=1")
sound3 = simplegui.load_sound("https://www.dropbox.com/s/f9qns2mho0hwaad/Tsuku.mp3?dl=1")
windy = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/a/ac/ClowWindy.jpg/revision/latest?cb=20181209182000")
mirror = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/e/ec/ClowMirror.jpg/revision/latest?cb=20181211074413")
wood = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/e/e8/ClowWood.jpg/revision/latest?cb=20181209185223")
firery = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/1/12/ClowFirey.jpg/revision/latest?cb=20181210180715")
rturn = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/2/22/ClowReturn.jpg/revision/latest?cb=20181210164558")
light = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/6/66/ClowLight.jpg/revision/latest?cb=20181209150109")
watery = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/5/55/ClowWatery.jpg/revision/latest?cb=20181210150329")
time = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/6/62/ClowTime.jpg/revision/latest?cb=20181209145939")
clow = simplegui.load_image(
    "https://vignette.wikia.nocookie.net/ccs/images/7/7b/CCS_Clow_Card.jpg/revision/latest?cb=20181211221838")
last_pic = simplegui.load_image(
    "https://static2.cbrimages.com/wordpress/wp-content/uploads/2019/08/Sakura-and-Syaoran-Li-e1566328642828.png?q=50&fit=crop&w=740&h=370")

# global variables
CARD_WIDTH = 1830
CARD_HEIGHT = 4096

card = [windy, firery, light, watery, time, mirror, rturn, wood, windy, firery, light, watery, time, mirror, rturn,
        wood]
index = list(range(16))
pos = [0, 0]
flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
permanent_flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check = []
ind = []
flip_counter = 0
turns = 0
matching = 0
show = False


# helper function to initialize globals
def new_game():
    global pos, flag, index, card, flip_counter, ind, check, permanent_flag, turns, matching, show, label
    flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    permanent_flag = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pos = [0, 0]
    check = []
    ind = []
    random.shuffle(card)
    random.shuffle(index)
    flip_counter = 0
    turns = 0
    matching = 0
    show = False
    label.set_text("Turns = " + str(turns))
    label.get_text()
    sound1.play()


def exit_game():
    sound1.rewind()
    sound2.rewind()
    sound3.rewind()
    frame.stop()


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global check, ind, flip_counter, turns, matching, show, label
    if pos[0] > 185 and pos[0] < 335 and pos[1] > 35 and pos[1] < 210 and flag[0] == 0 and permanent_flag[0] == 0:
        turns += 1
        flip_counter += 1
        flag[0] = 1
        ind.append(0)
        check.append(card[index[0]])
    if pos[0] > 185 + 160 and pos[0] < 335 + 160 and pos[1] > 35 and pos[1] < 210 and flag[1] == 0 and permanent_flag[
        1] == 0:
        turns += 1
        flip_counter += 1
        flag[1] = 1
        ind.append(1)
        check.append(card[index[1]])
    if pos[0] > 185 + 2 * 160 and pos[0] < 335 + 2 * 160 and pos[1] > 35 and pos[1] < 210 and flag[2] == 0 and \
            permanent_flag[2] == 0:
        turns += 1
        flip_counter += 1
        flag[2] = 1
        ind.append(2)
        check.append(card[index[2]])
    if pos[0] > 185 + 3 * 160 and pos[0] < 335 + 3 * 160 and pos[1] > 35 and pos[1] < 210 and flag[3] == 0 and \
            permanent_flag[3] == 0:
        turns += 1
        flip_counter += 1
        flag[3] = 1
        ind.append(3)
        check.append(card[index[3]])

    if pos[0] > 185 and pos[0] < 335 and pos[1] > 35 + 180 and pos[1] < 210 + 180 and flag[4] == 0 and permanent_flag[
        4] == 0:
        turns += 1
        flip_counter += 1
        flag[4] = 1
        ind.append(4)
        check.append(card[index[4]])
    if pos[0] > 185 + 160 and pos[0] < 335 + 160 and pos[1] > 35 + 180 and pos[1] < 210 + 180 and flag[5] == 0 and \
            permanent_flag[5] == 0:
        turns += 1
        flip_counter += 1
        flag[5] = 1
        ind.append(5)
        check.append(card[index[5]])
    if pos[0] > 185 + 2 * 160 and pos[0] < 335 + 2 * 160 and pos[1] > 35 + 180 and pos[1] < 210 + 180 and flag[
        6] == 0 and permanent_flag[6] == 0:
        turns += 1
        flip_counter += 1
        flag[6] = 1
        ind.append(6)
        check.append(card[index[6]])
    if pos[0] > 185 + 3 * 160 and pos[0] < 335 + 3 * 160 and pos[1] > 35 + 180 and pos[1] < 210 + 180 and flag[
        7] == 0 and permanent_flag[7] == 0:
        turns += 1
        flip_counter += 1
        flag[7] = 1
        ind.append(7)
        check.append(card[index[7]])

    if pos[0] > 185 and pos[0] < 335 and pos[1] > 35 + 2 * 180 and pos[1] < 210 + 2 * 180 and flag[8] == 0 and \
            permanent_flag[8] == 0:
        turns += 1
        flip_counter += 1
        flag[8] = 1
        ind.append(8)
        check.append(card[index[8]])
    if pos[0] > 185 + 160 and pos[0] < 335 + 160 and pos[1] > 35 + 2 * 180 and pos[1] < 210 + 2 * 180 and flag[
        9] == 0 and permanent_flag[9] == 0:
        turns += 1
        flip_counter += 1
        flag[9] = 1
        ind.append(9)
        check.append(card[index[9]])
    if pos[0] > 185 + 2 * 160 and pos[0] < 335 + 2 * 160 and pos[1] > 35 + 2 * 180 and pos[1] < 210 + 2 * 180 and flag[
        10] == 0 and permanent_flag[10] == 0:
        turns += 1
        flip_counter += 1
        flag[10] = 1
        ind.append(10)
        check.append(card[index[10]])
    if pos[0] > 185 + 3 * 160 and pos[0] < 335 + 3 * 160 and pos[1] > 35 + 2 * 180 and pos[1] < 210 + 2 * 180 and flag[
        11] == 0 and permanent_flag[11] == 0:
        turns += 1
        flip_counter += 1
        flag[11] = 1
        ind.append(11)
        check.append(card[index[11]])

    if pos[0] > 185 - 160 and pos[0] < 335 - 160 and pos[1] > 35 + 90 and pos[1] < 210 + 90 and flag[12] == 0 and \
            permanent_flag[12] == 0:
        turns += 1
        flip_counter += 1
        flag[12] = 1
        ind.append(12)
        check.append(card[index[12]])
    if pos[0] > 185 - 160 and pos[0] < 335 - 160 and pos[1] > 35 + 3 * 90 and pos[1] < 210 + 3 * 90 and flag[
        13] == 0 and permanent_flag[13] == 0:
        turns += 1
        flip_counter += 1
        flag[13] = 1
        ind.append(13)
        check.append(card[index[13]])

    if pos[0] > 185 + 4 * 160 and pos[0] < 335 + 4 * 160 and pos[1] > 35 + 90 and pos[1] < 210 + 90 and flag[
        14] == 0 and permanent_flag[14] == 0:
        turns += 1
        flip_counter += 1
        flag[14] = 1
        ind.append(14)
        check.append(card[index[14]])

    if pos[0] > 185 + 4 * 160 and pos[0] < 335 + 4 * 160 and pos[1] > 35 + 3 * 90 and pos[1] < 210 + 3 * 90 and flag[
        15] == 0 and permanent_flag[15] == 0:
        turns += 1
        flip_counter += 1
        flag[15] = 1
        ind.append(15)
        check.append(card[index[15]])

    if flip_counter == 2 and check[0] == check[1]:
        sound2.play()
        permanent_flag[ind[0]] = 1
        permanent_flag[ind[1]] = 1
        matching += 1

    if flip_counter == 3:
        flip_counter = 1
        flag[ind[0]] = 0
        flag[ind[1]] = 0
        if len(ind) > 1:
            ind.pop(0)
            ind.pop(0)
        if len(check) > 1:
            check.pop(0)
            check.pop(0)

    if matching == 8:
        show = True
        sound3.play()

    label.set_text("Turns = " + str(turns))
    label.get_text()


# cards are logically 50x100 pixels in size
def draw(canvas):
    global flag, permanent_flag, turns
    canvas.draw_text(str(turns), (1000, 80), 100, "Red")
    if flag[0] or permanent_flag[0]:
        canvas.draw_image(card[index[0]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 160, 124), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100 + 160, 124),
                          (150, 175))
    if flag[1] or permanent_flag[1]:
        canvas.draw_image(card[index[1]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 2 * 160, 124), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100 + 2 * 160, 124),
                          (150, 175))
    if flag[2] or permanent_flag[2]:
        canvas.draw_image(card[index[2]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 3 * 160, 124), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100 + 3 * 160, 124),
                          (150, 175))
    if flag[3] or permanent_flag[3]:
        canvas.draw_image(card[index[3]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 4 * 160, 124), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100 + 4 * 160, 124),
                          (150, 175))

    if flag[4] or permanent_flag[4]:
        canvas.draw_image(card[index[4]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 160, 124 + 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100 + 160, 124 + 180),
                          (150, 175))
    if flag[5] or permanent_flag[5]:
        canvas.draw_image(card[index[5]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 2 * 160, 124 + 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 2 * 160, 124 + 180), (150, 175))
    if flag[6] or permanent_flag[6]:
        canvas.draw_image(card[index[6]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 3 * 160, 124 + 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 3 * 160, 124 + 180), (150, 175))
    if flag[7] or permanent_flag[7]:
        canvas.draw_image(card[index[7]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 4 * 160, 124 + 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 4 * 160, 124 + 180), (150, 175))

    if flag[8] or permanent_flag[8]:
        canvas.draw_image(card[index[8]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 160, 124 + 2 * 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 160, 124 + 2 * 180), (150, 175))
    if flag[9] or permanent_flag[9]:
        canvas.draw_image(card[index[9]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 2 * 160, 124 + 2 * 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 2 * 160, 124 + 2 * 180), (150, 175))
    if flag[10] or permanent_flag[10]:
        canvas.draw_image(card[index[10]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 3 * 160, 124 + 2 * 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 3 * 160, 124 + 2 * 180), (150, 175))
    if flag[11] or permanent_flag[11]:
        canvas.draw_image(card[index[11]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 4 * 160, 124 + 2 * 180), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 4 * 160, 124 + 2 * 180), (150, 175))

    if flag[12] or permanent_flag[12]:
        canvas.draw_image(card[index[12]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100, 124 + 90), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100, 124 + 90),
                          (150, 175))
    if flag[13] or permanent_flag[13]:
        canvas.draw_image(card[index[13]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100, 124 + 3 * 90), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100, 124 + 3 * 90),
                          (150, 175))

    if flag[14] or permanent_flag[14]:
        canvas.draw_image(card[index[14]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 5 * 160, 124 + 90), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT), (100 + 5 * 160, 124 + 90),
                          (150, 175))
    if flag[15] or permanent_flag[15]:
        canvas.draw_image(card[index[15]], (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 5 * 160, 124 + 3 * 90), (150, 175))
    else:
        canvas.draw_image(clow, (CARD_WIDTH / 2, CARD_HEIGHT / 2), (CARD_WIDTH, CARD_HEIGHT),
                          (100 + 5 * 160, 124 + 3 * 90), (150, 175))

    if show:
        canvas.draw_image(last_pic, (740 / 2, 370 / 2), (740, 370), (1100 / 2, 600 / 2), (1100, 600))
        canvas.draw_text("You are the new CardCaptor", (100, 580), 80, "Yellow")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 1100, 600)
frame.add_button("Reset", new_game)
frame.add_label("")
label = frame.add_label("Turns = 0")
frame.add_label("")
frame.add_label("Enjoy the game !!! \n The sounds uploaded from the dropbox might not play properly.")
frame.add_label("")
frame.add_button("Exit", exit_game)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric