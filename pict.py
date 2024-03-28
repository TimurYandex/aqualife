import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

circle_radius = 2 * WIDTH // 3
circle1_pos = (0, -100)
circle2_pos = (600, -100)
circle5_pos = (300, -350)
circle3_pos = (150, 300)
circle4_pos = (450, 300)
circle6_pos = (350, 400)

# Создаем поверхности для кругов
circle1 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle3 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle4 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle5 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle6 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# хвостик
pygame.draw.circle(circle1, "yellow", circle1_pos, circle_radius)
pygame.draw.circle(circle2, WHITE, circle2_pos, circle_radius)
pygame.draw.circle(circle5, WHITE, circle5_pos, circle_radius)
tail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
tail_surface.blit(circle1, (0, 0))
tail_surface.blit(circle2, (0, 0), None, special_flags=pygame.BLEND_RGBA_MULT)
tail_surface.blit(circle5, (0, 0), None, special_flags=pygame.BLEND_RGBA_SUB)

# тело
pygame.draw.circle(circle3, "red", circle3_pos, 2 * circle_radius // 3)
pygame.draw.circle(circle4, WHITE, circle4_pos, 2 * circle_radius // 3)
body_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
body_surface.blit(circle3, (0, 0))
body_surface.blit(circle4, (0, 0), None, special_flags=pygame.BLEND_RGBA_MULT)

# рыбка
fish_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
# fish_surface.fill("green")
fish_surface.blit(tail_surface, (0, 0))
fish_surface.blit(tail_surface, (100, 200))
fish_surface.blit(body_surface, (0, 0))

# глаз
pygame.draw.circle(fish_surface, "white", circle6_pos, circle_radius // 15)
pygame.draw.circle(fish_surface, "black", circle6_pos, circle_radius // 30)

running = True
alpha = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    alpha += 1
    # alpha = 45

    moving_right = alpha % 360 - 180 < 0
    flipped = pygame.transform.flip(fish_surface, True, False)
    if moving_right:
        rotated = pygame.transform.rotate(fish_surface, alpha)
    else:
        rotated = pygame.transform.rotate(flipped, alpha)
    cos_alpha = math.cos(alpha % 90 * math.pi / 180)
    sin_alpha = math.sin(alpha % 90 * math.pi / 180)
    dx = ((cos_alpha + sin_alpha) / 2 - 0.5) * WIDTH
    dy = ((cos_alpha + sin_alpha) / 2 - 0.5) * WIDTH
    screen.blit(rotated, (-dx, -dy))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
