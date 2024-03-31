import random
from pygame import mixer
from fish import Player, Fish, Rock, Fry
import pygame
from const import WIDTH, HEIGHT, FISH_START_SIZE, PINK, LIGHTBLUE, LEVEL1, \
    EAT_FISH_EVENT, LOSE_FRY_EVENT
from sprite_groups import SpriteGroups
from funcs import generate_rock_positions, generate_fish_fry_positions
from ScoreCounter import Counter

groups = SpriteGroups()
all_sprites, rocks, fishes, player, fries = groups.get_groups()


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.all_sprites = all_sprites
        self.rocks = rocks
        self.fishes = fishes
        self.fries = fries
        self.score = 0
        self.game_over = False
        self.goto_menu = False
        self.level = None
        self.start_ambient_music()
        self.ambient_sound = mixer.Sound("data/sound/Ambient.wav")
        self.death_sound = mixer.Sound("data/sound/Death.wav")
        self.win_sound = mixer.Sound("data/sound/Win.wav")
        self.ambient_channel = mixer.find_channel(True)
        self.ambient_sound.set_volume(0.3)
        self.counter = None

    def start_counter(self, duration):
        self.counter = Counter(duration)

    def start_ambient_sound(self):
        self.ambient_channel.play(self.ambient_sound, loops=-1)

    def stop_ambient_sound(self):
        self.ambient_channel.stop()

    def start_ambient_music(self):
        mixer.music.load("data/sound/guitar1.wav")
        mixer.music.set_volume(0.1)
        mixer.music.play(loops=-1)

    def load_level(self, level_select):
        # Загрузка уровня из файла
        self.level = level_select
        for level in self.level.levels:
            if level["name"] == level_select.selected_level:
                fish_num = level["fish"]
                max_fish_size = level["size"]
                fry_num = level["fry"]
                velocity = level["velocity"]
                duration = level["duration"]

        # Создание спрайтов рыб и камней на основе данных уровня

        fish_positions, fry_positions = generate_fish_fry_positions(WIDTH,
                                                                    HEIGHT,
                                                                    fry_num,
                                                                    fish_num)
        for pos in fish_positions:
            radius = random.randint(FISH_START_SIZE // 2,
                                    max_fish_size * FISH_START_SIZE)
            Fish(*pos, radius, velocity)
        for pos in fry_positions:
            Fry(*pos, 0, velocity)
        rock_positions = generate_rock_positions(WIDTH, HEIGHT)
        for pos in rock_positions:
            Rock(*pos)

        # Создание игрока
        Player(WIDTH / 2, HEIGHT / 2, FISH_START_SIZE, velocity)

        # Запуск таймера и счетчика
        self.start_counter(duration)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.goto_menu = True
        self.counter.handle_event(event)

    def update(self):
        self.all_sprites.update()
        if len(player) == 1:  # игрок жив
            self.score = player.sprites()[0].score
            # когда игрок жив, возможны варианты окончания:
            # 1. время кончилось,
            # тогда победа при положительном счете, иначе поражение
            # 2. время еще есть, но он одинок либо с мальками,
            # тогда победа при положительном счете, иначе поражение
            if self.counter.is_game_over():
                if self.score > 0:
                    self.win_sound.play()
                else:
                    self.death_sound.play()
                self.game_over = True
            elif (len(self.fishes) == 1  # игрок остался совсем один
                  # или игрок остался только со своими мальками
                  or len(self.fishes) == len(self.fries) + len(player)):
                if self.score > 0:
                    self.win_sound.play()
                else:
                    self.death_sound.play()
                self.game_over = True
            else:  # Игра продолжается!
                self.game_over = False
        else:  # игрок съеден
            self.score = -100
            self.death_sound.play()
            self.game_over = True
        self.counter.update()

    def finalize(self):
        for sprite in self.all_sprites:
            sprite.kill()
        self.score = 0
        self.game_over = False
        self.goto_menu = False
        self.level = None
        self.counter.reset()

    def draw(self, screen):
        screen.fill(LIGHTBLUE)  # Синий фон
        self.all_sprites.draw(screen)

        # Отрисовка счета игрока
        self.counter.draw(screen)
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
