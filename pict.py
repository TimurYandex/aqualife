import pygame
import sys
import math
from const import WHITE


# тестовый код для разработки внешнего вида, этот файл можно запускать
# отдельно, но он предназначен для импорта двух функций


def draw_fish(size, color1, color2):
    size12 = size / 12
    circle_radius = 8 * size12
    circle1_pos = (0, -2 * size12)
    circle2_pos = (size, -2 * size12)
    circle5_pos = (6 * size12, -7 * size12)
    circle3_pos = (3 * size12, 6 * size12)
    circle4_pos = (9 * size12, 6 * size12)
    circle6_pos = (7 * size12, 8 * size12)
    # Создаем поверхности для кругов
    circle1 = pygame.Surface((size, size), pygame.SRCALPHA)
    circle2 = pygame.Surface((size, size), pygame.SRCALPHA)
    circle3 = pygame.Surface((size, size), pygame.SRCALPHA)
    circle4 = pygame.Surface((size, size), pygame.SRCALPHA)
    circle5 = pygame.Surface((size, size), pygame.SRCALPHA)
    circle6 = pygame.Surface((size, size), pygame.SRCALPHA)
    # хвостик
    pygame.draw.circle(circle1, color2, circle1_pos, circle_radius)
    pygame.draw.circle(circle2, WHITE, circle2_pos, circle_radius)
    pygame.draw.circle(circle5, WHITE, circle5_pos, circle_radius)
    tail_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    tail_surface.blit(circle1, (0, 0))
    tail_surface.blit(circle2, (0, 0), None,
                      special_flags=pygame.BLEND_RGBA_MULT)
    tail_surface.blit(circle5, (0, 0), None,
                      special_flags=pygame.BLEND_RGBA_SUB)
    # тело
    pygame.draw.circle(circle3, color1, circle3_pos, 2 * circle_radius / 3)
    pygame.draw.circle(circle4, WHITE, circle4_pos, 2 * circle_radius / 3)
    body_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    body_surface.blit(circle3, (0, 0))
    body_surface.blit(circle4, (0, 0), None,
                      special_flags=pygame.BLEND_RGBA_MULT)

    # рыбка
    fish_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    # fish_surface.fill("green")
    fish_surface.blit(tail_surface, (0, 0))
    fish_surface.blit(tail_surface, (2 * size12, 4 * size12))
    fish_surface.blit(body_surface, (0, 0))

    # глаз
    pygame.draw.circle(fish_surface, "white", circle6_pos, circle_radius / 15)
    pygame.draw.circle(fish_surface, "black", circle6_pos, circle_radius / 30)

    return fish_surface


def rotate_fish(fish_surface, alpha):
    moving_right = alpha % 360 - 180 < 0
    rect = fish_surface.get_rect()
    flipped = pygame.transform.flip(fish_surface, True, False)
    if moving_right:
        rotated = pygame.transform.rotate(fish_surface, alpha)
    else:
        rotated = pygame.transform.rotate(flipped, alpha)
    cos_alpha = math.cos(alpha % 90 * math.pi / 180)
    sin_alpha = math.sin(alpha % 90 * math.pi / 180)
    dx = ((cos_alpha + sin_alpha) / 2 - 0.5) * rect.width
    dy = ((cos_alpha + sin_alpha) / 2 - 0.5) * rect.width
    rotated_fish = pygame.Surface(rect.size, pygame.SRCALPHA)
    rotated_fish.blit(rotated, (-dx, -dy))
    return rotated_fish


# тестовый код для разработки внешнего вида, этот файл можно запускать отдельно
if __name__ == "__main__":

    SIZE = 600, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    fish_surface = draw_fish(250, (100, 150, 180), (200, 50, 80))

    running = True
    alpha = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        alpha += 5
        # alpha = 45
        a_fish = rotate_fish(fish_surface, alpha)
        screen.blit(a_fish, (SIZE[0] // 4, SIZE[0] // 4))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
