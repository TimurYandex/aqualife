import pygame

# Собственные события
EAT_FISH_EVENT = pygame.USEREVENT + 1
LOSE_FRY_EVENT = pygame.USEREVENT + 2

# Размеры
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
del screen
FISH_START_SIZE = 40
FRY_START_SIZE = 20

# Скорости
MAX_SPEED = 6
MIN_SPEED = 0.5
FPS = 50

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 200, 200)
RED = (255, 0, 0)
GREEN = (20, 100, 20)
BROWN = (50, 20, 10)
LIGHTBLUE = (120, 150, 255)
YELLOW = (255, 255, 0)
TEAL = (20, 90, 80)

# Ускорения
DECELERATION = 0.005
ACCELERATION = 0.3

LEVEL1 = "1: Останься последней рыбкой!"
LEVEL2 = "2: Съешь хоть одну и проживи 20 секунд!"
LEVEL3 = "3: Съешь хоть одну и защити мальков 30 секунд!"
