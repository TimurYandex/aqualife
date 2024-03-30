import math
import random
from const import *


def cart2pol(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = 180 * math.atan2(x, y) / math.pi
    return r, theta


def pol2cart(r, theta):
    y = r * math.cos(theta * math.pi / 180)
    x = r * math.sin(theta * math.pi / 180)
    return x, y


def generate_color(intention=None):
    if not intention:
        color1 = RED
        color2 = BLACK
    elif intention == "rock":
        color1 = BROWN
        color2 = BLACK
    elif intention == "fish":
        color1 = (random.randint(150, 250), random.randint(50, 200),
                  random.randint(50, 150))
        color2 = (random.randint(0, 50), random.randint(200, 250),
                  random.randint(100, 250))
    elif intention == "player":
        color1 = RED
        color2 = YELLOW
    return color1, color2


