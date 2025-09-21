import pygame
from settings import RED

class ToolPanel:
    def __init__(self, screen, icon_size, spacing, margin):
        self.screen = screen
        self.icon_size = icon_size
        self.spacing = spacing
        self.margin = margin

        self.tools = {
            "wall": "../assets/img/pencil.png",
            "eraser": "../assets/img/eraser.png",
            "water": "../assets/img/water.png",
            "rock": "../assets/img/rock.png",
            "sand": "../assets/img/sand.png",
        }

        self.mode_map = {
            "eraser": "grass",
            "wall": "wall",
            "water": "water",
            "rock": "rock",
            "sand": "sand"
        }

        self.icons = {}
        self.rects = {}
        y_pos = self.margin
        x_pos = self.margin

        for tool, path in self.tools.items():
            icon = pygame.image.load(path)
            icon = pygame.transform.scale(icon, (self.icon_size, self.icon_size))
            rect = icon.get_rect(topleft=(x_pos, y_pos))
            self.icons[tool] = icon
            self.rects[tool] = rect
            y_pos += self.icon_size + self.spacing

        self.active_mode = "wall" # wall é oo modo inicial

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for key, rect in self.rects.items():
                if rect.collidepoint(mouse_pos):
                    self.active_mode = key
                    return True
        return False

    def draw(self):
        for key, rect in self.rects.items():
            self.screen.blit(self.icons[key], rect.topleft)
            if self.active_mode == key:
                pygame.draw.rect(self.screen, RED, rect, 3)

    def get_active_mode_type(self):
        return self.mode_map.get(self.active_mode)