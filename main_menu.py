import pygame

class MainMenu:
    def __init__(self):
        self.font_title = pygame.font.Font(None, 48)
        self.font_text = pygame.font.Font(None, 36)
        self.start_game_button = pygame.Rect(300, 200, 200, 50)
        self.quit_button = pygame.Rect(300, 300, 200, 50)
        self.start_game = False
        self.quit_game = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_game_button.collidepoint(event.pos):
                self.start_game = True
            elif self.quit_button.collidepoint(event.pos):
                self.quit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

        title_text = self.font_title.render("Главное меню", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(400, 100))
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, (255, 255, 255), self.start_game_button)
        start_text = self.font_text.render("Выбор уровня", True, (0, 0, 0))
        start_rect = start_text.get_rect(center=self.start_game_button.center)
        screen.blit(start_text, start_rect)

        pygame.draw.rect(screen, (255, 255, 255), self.quit_button)
        quit_text = self.font_text.render("Выход", True, (0, 0, 0))
        quit_rect = quit_text.get_rect(center=self.quit_button.center)
        screen.blit(quit_text, quit_rect)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    main_menu = MainMenu()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_menu.handle_event(event)

        main_menu.update()
        main_menu.draw(screen)

        if main_menu.start_game:
            print("Начало игры")
            main_menu.start_game = False
        elif main_menu.quit_game:
            print("Выход из игры")
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()