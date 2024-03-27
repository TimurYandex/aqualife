import pygame

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

from const import RED, GREEN, DECELERATION, ACCELERATION

all_sprites = pygame.sprite.Group()


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
    pass


class Fish(Ball):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.speedx = 1
        self.speedy = 1
        self.acceleration = ACCELERATION
        self.deceleration = DECELERATION

    def additional_check(self):
        ...

    def update(self):
        self.additional_check()
        self.rect = self.rect.move(self.speedx, self.speedy)

        # Здесь вы можете добавить логику ограничения рыбки в пределах
        # игрового мира


class Player(Fish):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = GREEN
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

    def additional_check(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            print("KEYDOWN in fish")
            self.speedy -= self.acceleration
        if keys[K_DOWN]:
            self.speedy += self.acceleration
        if keys[K_LEFT]:
            self.speedx -= self.acceleration
        if keys[K_RIGHT]:
            self.speedx += self.acceleration
        speed = self.speedx ** 2 + self.speedy ** 2
        if speed > 0:
            if self.speedx > 0:
                self.speedx -= self.deceleration
            if self.speedx < 0:
                self.speedx += self.deceleration
            if self.speedy > 0:
                self.speedy -= self.deceleration
            if self.speedy < 0:
                self.speedy += self.deceleration


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
