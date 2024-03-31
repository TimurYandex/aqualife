import pygame
from const import WIDTH, HEIGHT


class StartScreen:
    def __init__(self):
        self.font_title = pygame.font.Font(None, 48)
        self.font_text = pygame.font.Font(None, 36)
        self.start_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 200, 400,
                                        50)
        self.done = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(event.pos):
                self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                self.done = True

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((20, 90, 80))

        title_text = self.font_title.render("Рыбки", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
        screen.blit(title_text, title_rect)

        start_text1 = self.font_text.render(
                "Управление стрелками. Большие рыбки едят маленьких!", True,
                (255, 255, 255))
        start_rect1 = start_text1.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(start_text1, start_rect1)

        start_text2 = self.font_text.render(
                "ESC во время игры - выход в меню. С экранов выбора - выход "
                "из программы",
                True,
                (255, 255, 255))
        start_rect2 = start_text2.get_rect(
                center=(WIDTH / 2, HEIGHT / 2 + 100))
        screen.blit(start_text2, start_rect2)

        pygame.draw.rect(screen, (255, 255, 255), self.start_button)
        button_text = self.font_text.render("Главное меню", True, (0, 0, 0))
        button_rect = button_text.get_rect(center=self.start_button.center)
        screen.blit(button_text, button_rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
