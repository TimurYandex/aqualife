import pygame
from const import EAT_FISH_EVENT, LOSE_FRY_EVENT


class Counter:
    def __init__(self, duration=20):
        self.font = pygame.font.Font(None, 36)
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.score_count = 0
        self.game_over = False

    def update(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        if elapsed_time >= self.duration:
            self.game_over = True

    def handle_event(self, event):
        # Отладка на кликах:
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     self.score_count += 1
        if event.type == EAT_FISH_EVENT:
            self.score_count += 1
        if event.type == LOSE_FRY_EVENT:
            self.score_count -= 1

    def draw(self, surface):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        time_text = self.font.render(f"Время: {elapsed_time}", True,
                                     (255, 255, 255))
        score_text = self.font.render(f"Счет: {self.score_count}", True,
                                      (255, 255, 255))
        surface.blit(time_text, (200, 10))
        surface.blit(score_text, (surface.get_width() - 200, 10))


    def get_time(self):
        return (pygame.time.get_ticks() - self.start_time) // 1000

    def is_game_over(self):
        return self.game_over

    def get_score_count(self):
        return self.score_count

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.score_count = 0
        self.game_over = False


if __name__ == "__main__":
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Мое приложение")

    score_counter = Counter(duration=30)  # Длительность 30 секунд

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            score_counter.handle_event(event)

        score_counter.update()
        screen.fill((0,0,0))

        score_counter.draw(screen)

        if score_counter.is_game_over():
            print(f"Финальный счет: {score_counter.get_score_count()}")
            running = False

        pygame.display.flip()

    pygame.quit()
