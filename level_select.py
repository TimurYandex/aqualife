import pygame
import json
from const import WIDTH, HEIGHT


class LevelSelect:
    def __init__(self, default=None):
        self.font = pygame.font.Font(None, 36)
        self.levels = []
        self.load_levels()
        self.selected_level = default
        self._selected = 0

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, s):
        self.change_selection(s)

    def load_levels(self):
        with open("data/levels_data.json", "r", encoding='utf8') as file:
            data = json.load(file)
            for level_data in data["levels"]:
                level = {
                    "name": level_data["name"],
                    "completed": level_data["completed"],
                    "fish": level_data["fish"],
                    "size": level_data["size"],
                    "fry": level_data["fry"],
                    "velocity": level_data["velocity"],
                    "duration": level_data["duration"],
                    "button": pygame.Rect(WIDTH / 2 - 350,
                                          100 + len(self.levels) * 100,
                                          700, 50)
                }
                self.levels.append(level)

    def reset_completed(self):
        for level in self.levels:
            level["completed"] = False

    def save_levels(self):
        data = {"levels": []}
        for level in self.levels:
            level_data = {
                "name": level["name"],
                "completed": level["completed"],
                "fish": level["fish"],
                "size": level["size"],
                "fry": level["fry"],
                "velocity": level["velocity"],
                "duration": level["duration"]
            }
            data["levels"].append(level_data)
        with open("data/levels_data.json", "w", encoding='utf8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def change_selection(self, s=None):
        if s is not None:
            for i, level in enumerate(self.levels):
                if i == s:
                    if i == 0 or self.levels[i - 1]["completed"]:
                        self._selected = i

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, level in enumerate(self.levels):
                if level["button"].collidepoint(event.pos):
                    if i == 0 or self.levels[i - 1]["completed"]:
                        self.selected_level = level["name"]
                        self.selected = i
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.key == pygame.K_UP:
                self.selected -= 1
            elif event.key == pygame.K_DOWN:
                self.selected += 1
            elif event.key == pygame.K_RETURN:
                for i, level in enumerate(self.levels):
                    if i == self.selected:
                        self.selected_level = level["name"]

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((20, 90, 80))

        for i, level in enumerate(self.levels):
            color = (255, 255, 255) if i == 0 or self.levels[i - 1][
                "completed"] else (128, 128, 128)
            pygame.draw.rect(screen, color, level["button"], 0, 8)
            if i == self.selected:
                pygame.draw.rect(screen, (55, 155, 255),
                                 pygame.Rect(level["button"]).inflate(8, 8), 8,
                                 8)
            level_text = self.font.render(level["name"], True, (0, 0, 0))
            level_rect = level_text.get_rect(center=level["button"].center)
            screen.blit(level_text, level_rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    level_select = LevelSelect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            level_select.handle_event(event)

        level_select.update()
        level_select.draw(screen)

        if level_select.selected_level:
            print(f"Выбран уровень: {level_select.selected_level}")
            level_select.selected_level = None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
