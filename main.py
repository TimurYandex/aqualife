import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, RESIZABLE, VIDEORESIZE
from const import WIDTH, HEIGHT, FISH_START_SIZE, PINK, LIGHTBLUE, FPS

from main_menu import MainMenu
from level_select import LevelSelect
from game import Game
from game_over import GameOver
from start_screen import StartScreen


def main():
    pygame.init()
    # Установка размеров окна
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    main_menu = MainMenu()
    level_select = LevelSelect()
    game = Game()
    game_over = GameOver()
    start_screen = StartScreen()

    # Создание экрана
    current_screen = start_screen
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            current_screen.handle_event(event)

        current_screen.update()
        current_screen.draw(screen)

        if current_screen == start_screen and start_screen.done:
            current_screen = main_menu
            start_screen.done = False
        elif current_screen == main_menu and main_menu.quit_game:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        elif current_screen == main_menu and main_menu.start_game:
            current_screen = level_select
            main_menu.start_game = False
        elif current_screen == level_select and level_select.selected_level:
            game.load_level(level_select)
            current_screen = game
        elif current_screen == game and game.game_over:
            game_over.set_score(game.score)
            if game_over.score > 0:
                for level in level_select.levels:
                    if level["name"] == level_select.selected_level:
                        level["completed"] = True
                level_select.save_levels()
            level_select.selected_level = None
            game.finalize()
            current_screen = game_over
        elif current_screen == game_over and game_over.restart:
            current_screen = level_select
            game_over.restart = False

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
