# program template for Spaceship
# An interactive spaceship game, where you get points destroy the ricerocks without being hit by them.

# CodeSkulptor URL: http://www.codeskulptor.org/#user47_P67BNn0mx7GwxJ0.py

__author__ = "Apu Islam"
__copyright__ = "Copyright (c) 2016 Apu Islam"
__credits__ = ["Apu Islam"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Apu Islam"

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
start = False
maximum_rocks = 10
rock_group = set([])
missile_group = set([])
explosion_group = set([])


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def shoot(self, missile_group):
        boom_pos = [0, 0]
        boom_pos[0] = self.pos[0] + self.radius * math.cos(self.angle)
        boom_pos[1] = self.pos[1] + self.radius * math.sin(self.angle)
        boom_vel = [0, 0]
        boom_vel[0] = self.vel[0] + 5 * math.cos(self.angle)
        boom_vel[1] = self.vel[1] + 5 * math.sin(self.angle)

        missile_group.add(Sprite(boom_pos, boom_vel, 0, 0, missile_image, missile_info, missile_sound))

    def draw(self, canvas):
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + 90, self.image_center[1]], self.image_size, self.pos,
                              self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        if self.thrust:
            Forward = angle_to_vector(self.angle)
            self.vel[0] = Forward[0] * 6
            self.vel[1] = Forward[1] * 6

        else:
            self.vel[0] *= .99
            self.vel[1] *= .99


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def collision(self, obj):
        distance = dist(self.pos, obj.pos)
        if distance < self.radius + obj.radius:
            return True
        else:
            return False

    def draw(self, canvas):
        # canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        if self.animated:
            canvas.draw_image(self.image,
                              [self.image_center[0] + (self.age * self.image_size[0]), self.image_center[1]],
                              self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % 800
        self.pos[1] = (self.pos[1] + self.vel[1]) % 600


def draw(canvas):
    global time, rock_group, lives, missile_group, score

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("Lives = " + str(lives), [10, 30], 30, "White")
    canvas.draw_text("Score = " + str(score), [660, 30], 30, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    # update ship
    my_ship.update()

    if group_collision(rock_group, my_ship):
        lives -= 1
        explosion_sound.play()
        if lives == 0:
            reset()

    if group_group_collision(rock_group, missile_group):
        score += 1
        explosion_sound.play()

    if start == False:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())
        soundtrack.rewind()

    # initialize ship and two sprites


my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)


# timer handler that spawns a rock
def rock_spawner():
    global maximum_rocks, rock_group, WIDTH, HEIGHT, asteroid_image, asteroid_info, start
    pos = [0, 0]
    vel = [0, 0]
    angle_vel = random.choice([0.1, 0.2, 0.3]) / 2.0
    pos[0] = random.randint(0, 800)
    pos[1] = random.randint(0, 600)
    vel[0] = random.randint(-3, 3)
    vel[1] = random.randint(-3, 3)
    if len(rock_group) < maximum_rocks and start:
        if (dist(pos, my_ship.pos) > (40 + my_ship.radius + 50)):
            rock_group.add(Sprite(pos, vel, 0, angle_vel, asteroid_image, asteroid_info))


def process_sprite_group(rock_group, canvas):
    for rocks in list(rock_group):
        rocks.update()
        rocks.draw(canvas)
        rocks.age += 1
        if rocks.age >= rocks.lifespan:
            rock_group.remove(rocks)


def group_collision(rock_group, obj):
    for rocks in list(rock_group):
        if rocks.collision(obj):
            explosion_group.add(Sprite(rocks.pos, [0, 0], 0, 0, explosion_image,
                                       explosion_info, explosion_sound))
            rock_group.remove(rocks)
            return True
    return False


def group_group_collision(rock_group, missile_group):
    for missile in list(missile_group):
        if group_collision(rock_group, missile):
            missile_group.remove(missile)
            return True
    return False


def keydown(key):
    global missile_group
    if key == simplegui.KEY_MAP['left']:
        my_ship.angle_vel -= 0.1

    if key == simplegui.KEY_MAP['right']:
        my_ship.angle_vel += 0.1

    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust = True
        ship_thrust_sound.play()

    if key == simplegui.KEY_MAP['space']:
        my_ship.shoot(missile_group)
        missile_sound.play()


def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.angle_vel = 0
    if key == simplegui.KEY_MAP['right']:
        my_ship.angle_vel = 0

    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust = False
        ship_thrust_sound.rewind()


def reset():
    global score, lives, time, rock_group, missile_group, explosion_group, my_ship, start
    score = 0
    lives = 3
    time = 0
    start = False
    rock_group = set([])
    missile_group = set([])
    explosion_group = set([])
    my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)


def started(pos):
    global start, WIDTH, HEIGHT
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inside_x = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inside_y = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if start == False and inside_x and inside_y:
        start = True
        soundtrack.play()


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
frame.set_mouseclick_handler(started)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()