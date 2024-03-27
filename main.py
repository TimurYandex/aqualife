import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN

from const import WIDTH, HEIGHT, FISH_START_SIZE,PINK
from fish import Player, Fish, all_sprites

# Создание экрана
pygame.init()
# Установка размеров окна
size = width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
# Установка FPS
FPS = 50
# Создание игрока
player = Player(screen.get_rect().centerx, screen.get_rect().centery, FISH_START_SIZE)


# Загрузка уровня ??


def terminate():
    pygame.quit()
    sys.exit()


for _ in range(2):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = random.randint(0, FISH_START_SIZE)
    fish = Fish(x, y, radius)

clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            print("KEYDOWN in main")
    # Обновление всех спрайтов
    all_sprites.update()

    # Отрисовка изменений
    screen.fill(PINK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

terminate()
