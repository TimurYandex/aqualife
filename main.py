import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN

from const import WIDTH, HEIGHT, FISH_START_SIZE,PINK,LIGHTBLUE
from fish import Player, Fish, Rock, all_sprites

# Создание экрана
pygame.init()
# Установка размеров окна
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
# Установка FPS
FPS = 100
# Создание игрока
player = Player(screen.get_rect().centerx, screen.get_rect().centery, FISH_START_SIZE)


# Загрузка уровня ??

for i in range(1,10):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = random.randint(FISH_START_SIZE//2, 2*FISH_START_SIZE)
    Fish(x, y, radius)


for i in range(1,10):
    x = random.randint(0, WIDTH//5)*i
    y = HEIGHT + 1000
    radius = random.randint(1000, 1100)
    Rock(x, y, radius)

for i in range(1,10):
    x = random.randint(0, WIDTH//5)*i
    y = -1000
    radius = random.randint(1000, 1100)
    Rock(x, y, radius)

for i in range(1,10):
    y = random.randint(0, HEIGHT//5)*i
    x = WIDTH + 1000
    radius = random.randint(1000, 1100)
    Rock(x, y, radius)

for i in range(1,10):
    y = random.randint(0, HEIGHT//5)*i
    x = - 1000
    radius = random.randint(1000, 1100)
    Rock(x, y, radius)



clock = pygame.time.Clock()
running = True

def terminate():
    pygame.quit()
    sys.exit()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    # Обновление всех спрайтов
    all_sprites.update()

    # Отрисовка изменений
    screen.fill(LIGHTBLUE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

terminate()
