import pygame


class SpriteGroups:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.all_sprites = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()
        self.fishes = pygame.sprite.Group()
        self.player = pygame.sprite.Group()

    def get_groups(self):
        return self.all_sprites, self.rocks, self.fishes, self.player
