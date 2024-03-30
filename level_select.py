import pygame
import json


class LevelSelect:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.levels = []
        self.load_levels()
        self.selected_level = None

    def load_levels(self):
        with open("levels_data.json", "r", encoding='utf8') as file:
            data = json.load(file)
            for level_data in data["levels"]:
                level = {
                    "name": level_data["name"],
                    "completed": level_data["completed"],
                    "fish": level_data["fish"],
                    "size": level_data["size"],
                    "fry": level_data["fry"],
                    "velocity": level_data["velocity"],
                    "button": pygame.Rect(100, 100 + len(self.levels) * 100,
                                          400, 50)
                }
                self.levels.append(level)

    def save_levels(self):
        data = {"levels": []}
        for level in self.levels:
            level_data = {
                "name": level["name"],
                "completed": level["completed"],
                "fish": level["fish"],
                "size": level["size"],
                "fry": level["fry"],
                "velocity": level["velocity"]
            }
            data["levels"].append(level_data)
        with open("levels_data.json", "w", encoding='utf8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, level in enumerate(self.levels):
                if level["button"].collidepoint(event.pos):
                    if i == 0 or self.levels[i - 1]["completed"]:
                        self.selected_level = level["name"]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))

        for i, level in enumerate(self.levels):
            color = (255, 255, 255) if i == 0 or self.levels[i - 1][
                "completed"] else (128, 128, 128)
            pygame.draw.rect(screen, color, level["button"])
            level_text = self.font.render(level["name"], True, (0, 0, 0))
            level_rect = level_text.get_rect(center=level["button"].center)
            screen.blit(level_text, level_rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
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
