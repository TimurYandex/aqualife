import random

import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

from const import RED, GREEN, DECELERATION, ACCELERATION

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
fishes = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(all_sprites)
        self.color = RED
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)


class Rock(Ball):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(rocks)


class Fish(Ball):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.speedx = 1
        self.speedy = 1
        self.acceleration = ACCELERATION
        self.deceleration = DECELERATION
        self.centerp = self.rect.center
        self.add(fishes)

    def additional_check(self):
        self.centerp = self.rect.center
        ...

    def handle_collisions(self):
        collided_rocks = pygame.sprite.spritecollide(self, rocks, False,
                                                     pygame.sprite.collide_mask)
        if collided_rocks:
            for rock in collided_rocks:
                # Вычисляем вектор отскока
                bounce_vector = pygame.math.Vector2(
                        self.rect.center) - pygame.math.Vector2(
                        rock.rect.center)
                bounce_vector.normalize_ip()

                # Изменяем вектор скорости рыбки
                self.speedx = bounce_vector.x * abs(
                        self.speedx) + self.speedx * (0.1 + random.random())
                self.speedy = bounce_vector.y * abs(
                        self.speedy) + self.speedy * (0.1 + random.random())

    def update(self):
        self.additional_check()
        self.rect = self.rect.move(self.speedx, self.speedy)
        self.handle_collisions()

        # Здесь вы можете добавить логику ограничения рыбки в пределах
        # игрового мира


class Player(Fish):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = GREEN
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

    def additional_check(self):
        super().additional_check()
        # Обработка замедления
        speed_x = self.speedx ** 2
        speed_y = self.speedy ** 2
        if speed_x > 0:
            self.speedx -= self.deceleration * self.speedx
        if speed_y > 0:
            self.speedy -= self.deceleration * self.speedy

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.speedy -= self.acceleration
        if keys[K_DOWN]:
            self.speedy += self.acceleration
        if keys[K_LEFT]:
            self.speedx -= self.acceleration
        if keys[K_RIGHT]:
            self.speedx += self.acceleration

    def handle_collisions(self):
        super().handle_collisions()
        contacted_fishes = pygame.sprite.spritecollide(self, fishes, False,
                                                       pygame.sprite.collide_mask)
        if contacted_fishes:
            for fish in contacted_fishes:
                if self is not fish:
                    fish.kill()


class Fry(Fish):
    pass


class Enemy(Fish):
    pass


class Features:
    def __init__(self):
        self.main_color = pygame.Color("blue")
        self.second_color = pygame.Color("red")
        self.fearless = False
        self.hungry = True
