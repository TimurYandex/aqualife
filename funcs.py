import math

def cart2pol(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = 180 * math.atan2(x, y) / math.pi
    return r, theta

def pol2cart(r, theta):
    y = r * math.cos(theta * math.pi / 180)
    x = r * math.sin(theta * math.pi / 180)
    return x, y
