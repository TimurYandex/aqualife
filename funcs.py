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


def noise(x):
    return random.random() * x / 30


def generate_rock_positions(w, h):
    s = min(w, h)
    r1 = s *4/5
    r2 = s * 4 / 7
    stones = []
    for i in (-1, 1):
        for j in (-1, 1):
            stones.append((i * (s / 2 + w / 2 + noise(s)) + w / 2,
                           j * (s / 2 + h / 2 + noise(s)) + h / 2,
                           r1 + noise(s), ((50 + noise(1000), 50 + noise(1000),
                                            50 + noise(1000)), BLACK)))
    for i in (-1, 1):
        for j in range(1, 5):
            stones.append((i * (s / 2 + w / 2 + noise(s)) + w / 2,
                           j * (h / 5 + noise(s)),
                           r2 + noise(s), ((50 + noise(1000), 50 + noise(1000),
                                           50 + noise(1000)), BLACK)))
    for j in (-1, 1):
        for i in range(1, 5):
            stones.append((i * (w / 5 + noise(s)),
                           j * (s / 2 + h / 2 + noise(s)) + h / 2,
                           r2 + noise(s), ((50 + noise(1000), 50 + noise(1000),
                                           50 + noise(1000)), BLACK)))
    return stones
