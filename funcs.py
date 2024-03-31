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
    r1 = s * 4 / 5
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


def generate_fish_fry_positions(w, h, fry_num, fish_num):
    fish_positions, fry_positions = [], []
    if fry_num:
        for i in range(fry_num):
            fry_positions.append((200, 150 + 10 * i))
        q1 = fish_num // 3
        q2 = fish_num // 3
        q3 = fish_num - q1 - q2
        for _ in range(q1):
            x = random.randint(w // 3, w)
            y = random.randint(0, h // 3)
            fish_positions.append((x, y))
        for _ in range(q2):
            x = random.randint(w // 3, w)
            y = random.randint(h // 3, h)
            fish_positions.append((x, y))
        for _ in range(q3):
            x = random.randint(0, w // 3)
            y = random.randint(h // 3, h)
            fish_positions.append((x, y))
    else:
        for _ in range(fish_num):
            x = random.randint(0, 3*w // 7)
            y = random.randint(0, 3*h // 7)
            bin_x = random.randint(0, 1) * 4 * w // 7
            bin_y = random.randint(0, 1) * 4 * h // 7
            fish_positions.append((x + bin_x, y + bin_y))
    return fish_positions, fry_positions
