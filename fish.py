import random

from funcs import cart2pol, pol2cart, generate_color
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.math import Vector2
from pict import *
from const import RED, DECELERATION, ACCELERATION, WIDTH, MAX_SPEED, MIN_SPEED

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
fishes = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(all_sprites)
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect((0, 0), (2 * radius, 2 * radius))
        self.mask = pygame.mask.from_surface(self.image)
        self._color = generate_color()
        self._position = Vector2(x, y)
        self._size = 2 * radius
        self.draw()
        self.position = self._position

    def draw(self):
        radius = self._size / 2
        pygame.draw.circle(self.image, self.color[0], (radius, radius), radius)
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position
        self.rect.center = new_position

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color
        self.draw()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.center = self._position


class Rock(Ball):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = generate_color("rock")
        self.add(rocks)


class Fish(Ball):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.acceleration = ACCELERATION
        self.deceleration = DECELERATION
        self._color = generate_color("fish")
        self.fish_image = draw_fish(2 * radius, self._color)
        self._speed = Vector2()
        self.fear = Vector2()
        self.greed = Vector2()
        self.add(fishes)

    def draw(self):
        self.fish_image = draw_fish(self._size, self.color)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if isinstance(new_speed, Vector2):
            self._speed = new_speed
        else:
            raise ValueError("Speed must be a pygame.math.Vector2 instance")
        if self._speed.length() < self._speed.epsilon:
            self._speed = MIN_SPEED * Vector2(random.random(),
                                              random.random()).normalize()

        if self._speed.length() > MAX_SPEED:
            self._speed.scale_to_length(MAX_SPEED)

    def additional_check(self):
        small = []
        big = []
        self.greed = self.fear = Vector2()
        for fish in fishes:
            if fish != self:
                direction = Vector2(fish.position) - Vector2(self.position)
                if fish.size >= self.size:
                    big.append(direction)
                else:
                    small.append(direction)
        if small:
            for tasty in sorted(small, key=lambda x: x.length())[:3]:
                self.greed += tasty.normalize()
        if big:
            for scare in sorted(big, key=lambda x: x.length())[:3]:
                self.fear -= scare.normalize()
        ...

    def rock_collisions(self):
        collided_rocks = pygame.sprite.spritecollide(self, rocks, False,
                                                     pygame.sprite.collide_mask)
        if collided_rocks:
            bounce_vector = Vector2()
            for rock in collided_rocks:
                # Вычисляем вектор отскока
                bounce = Vector2(self.position) - Vector2(rock.position)
                bounce.normalize_ip()
                bounce_vector += bounce
                # выходим немножко из всех камней
                self.position += bounce

            # Вычисляем величину проекции скорости на нормаль
            speed_norm = abs(self.speed.dot(bounce_vector))

            # Обновляем скорость рыбки для отражения
            self.speed += 2 * speed_norm * bounce_vector

    def fish_collisions(self):
        contacted_fishes = pygame.sprite.spritecollide(self, fishes, False,
                                                       pygame.sprite.collide_mask)
        if contacted_fishes:
            for fish in contacted_fishes:
                if fish != self and self.size >= fish.size:
                    fish.kill()
                    self.size *= 1.1

    def handle_collisions(self):
        self.rock_collisions()
        self.fish_collisions()

    def decelerate(self):
        self.speed /= (1 + self.speed.length() * self.deceleration)

    def accelerate(self):
        try:
            self.speed = self.speed.slerp(self.fear + self.greed, 0.02)
        except ValueError:
            self.speed *= 1.01
        ...

    def update(self):
        self.decelerate()
        self.accelerate()
        self.handle_collisions()
        self.additional_check()
        r, alpha = cart2pol(self.speed.x, self.speed.y)
        self.image = rotate_fish(self.fish_image, alpha)
        self.mask = pygame.mask.from_surface(self.image)
        self.position += self.speed


class Player(Fish):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self._color = generate_color("player")
        self.draw()

    def additional_check(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.speed.y -= self.acceleration
        if keys[K_DOWN]:
            self.speed.y += self.acceleration
        if keys[K_LEFT]:
            self.speed.x -= self.acceleration
        if keys[K_RIGHT]:
            self.speed.x += self.acceleration

    def accelerate(self):
        ...

    def handle_collisions(self):
        super().handle_collisions()


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
