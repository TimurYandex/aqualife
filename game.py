import random
from pygame import mixer
from fish import Player, Fish, Rock, Ball
import pygame
from const import WIDTH, HEIGHT, FISH_START_SIZE, PINK, LIGHTBLUE, LEVEL1
from sprite_groups import SpriteGroups
from funcs import generate_rock_positions

groups = SpriteGroups()
all_sprites, rocks, fishes, player = groups.get_groups()


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.all_sprites = all_sprites
        self.rocks = rocks
        self.fishes = fishes
        self.score = 0
        self.game_over = False
        self.level = None
        self.start_ambient_music()


    def start_ambient_music(self):
        mixer.music.load("./data/guitar1.wav")
        mixer.music.set_volume(0.1)
        mixer.music.play(loops=-1)

    def stop_ambient_music(self):
        self.ambient_channel.stop()

    def load_level(self, level_select):
        # Загрузка уровня из файла
        self.level = level_select
        for level in self.level.levels:
            if level["name"] == level_select.selected_level:
                fish_num = level["fish"]
                max_fish_size = level["size"]
                # fry_num = level["fry"]
                # velocity = level["velocity"]

        # Создание спрайтов рыб и камней на основе данных уровня
        for i in range(1, fish_num):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            radius = random.randint(FISH_START_SIZE // 3,
                                    max_fish_size * FISH_START_SIZE)
            Fish(x, y, radius)
        rock_position = generate_rock_positions(WIDTH, HEIGHT)
        for pos in rock_position:
            Rock(*pos)

        # Создание игрока
        Player(WIDTH / 2, HEIGHT / 2, FISH_START_SIZE)


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        self.all_sprites.update()
        if len(player) == 1:
            self.score = player.sprites()[0].score
        else:
            self.score = -1
            self.game_over = True
        if len(self.fishes) == 1:
            self.game_over = True

    def finalize(self):
        for sprite in self.all_sprites:
            sprite.kill()
        self.score = 0
        self.game_over = False
        self.level = None

    def draw(self, screen):
        screen.fill(LIGHTBLUE)  # Синий фон
        self.all_sprites.draw(screen)

        # Отрисовка счета игрока
        pygame.display.flip()

    def run(self, screen):
        while not self.game_over:
            for event in pygame.event.get():
                self.handle_event(event)
            self.update()
            self.draw(screen)
            self.clock.tick(60)


if __name__ == "__main__":
    from level_select import LevelSelect
    pygame.init()
    mixer.init()
    test_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game()
    game.load_level(LevelSelect(LEVEL1))
    game.run(test_screen)
    mixer.quit()
    pygame.quit()
