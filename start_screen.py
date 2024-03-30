import pygame


class StartScreen:
    def __init__(self):
        self.font_title = pygame.font.Font(None, 48)
        self.font_text = pygame.font.Font(None, 36)
        self.start_button = pygame.Rect(200, 400, 400, 50)
        self.done = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(event.pos):
                self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

        title_text = self.font_title.render("Рыбки", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(400, 200))
        screen.blit(title_text, title_rect)

        start_text = self.font_text.render(
            "Управление стрелками, Esc - выход в меню", True,
            (255, 255, 255))
        start_rect = start_text.get_rect(center=(400, 300))
        screen.blit(start_text, start_rect)

        pygame.draw.rect(screen, (255, 255, 255), self.start_button)
        button_text = self.font_text.render("Главное меню", True, (0, 0, 0))
        button_rect = button_text.get_rect(center=self.start_button.center)
        screen.blit(button_text, button_rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    start_screen = StartScreen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            start_screen.handle_event(event)

        start_screen.update()
        start_screen.draw(screen)

        if start_screen.done:
            print("Переход к главному меню")
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
