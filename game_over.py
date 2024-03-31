import pygame
from const import WIDTH, HEIGHT


class GameOver:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.time = 0
        self.restart_button = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2, 200, 50)
        self.restart = False

    def set_score(self, score):
        self.score = score

    def set_time(self, time):
        self.time = time

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_button.collidepoint(event.pos):
                self.restart = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                self.restart = True

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((10, 50, 40))

        message = "УРОВЕНЬ ПРОЙДЕН"
        game_over_text = self.font.render(message, True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(
                center=(WIDTH / 2, HEIGHT / 2 - 100))
        screen.blit(game_over_text, game_over_rect)

        score_text = self.font.render(
                f"Счет: {self.score}      Время: {self.time}",
                True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))
        screen.blit(score_text, score_rect)

        pygame.draw.rect(screen, (255, 255, 255), self.restart_button)
        restart_text = self.font.render("Еще!", True, (0, 0, 0))
        restart_rect = restart_text.get_rect(center=self.restart_button.center)
        screen.blit(restart_text, restart_rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    game_over = GameOver()
    game_over.set_score(100)  # Установка тестового счета

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_over.handle_event(event)

        game_over.update()
        game_over.draw(screen)

        if game_over.restart:
            print("Перезапуск игры")
            game_over.restart = False
            game_over.set_score(0)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
