import pygame
from settings import *
import os

def load_icon(path):
    try:
        return pygame.image.load(path)
    except FileNotFoundError:
        print(f"AVISO: Arquivo de ícone não encontrado em '{path}'")
        return None

class ToolPanel:
    def __init__(self, screen, icon_size, spacing, margin):
        self.screen = screen
        self.icon_size = icon_size
        self.spacing = spacing
        self.margin = margin
        self.active_mode = "wall" 

        assets_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')

        self.tools = {
            "wall": os.path.join(assets_path, "pencil.png"),
            "eraser": os.path.join(assets_path, "eraser.png"),
            "start": os.path.join(assets_path, "start.jpg"),
            "end": os.path.join(assets_path, "end.jpg"),
            "water": os.path.join(assets_path, "water.png"),
            "rock": os.path.join(assets_path, "rock.png"),
            "sand": os.path.join(assets_path, "sand.png"),
        }

        self.mode_map = {
            "eraser": "grass",
            "wall": "wall",
            "start": "start",
            "end": "end",
            "water": "water",
            "rock": "rock",
            "sand": "sand"
        }

        self.icons = {}
        self.rects = {}
        y_pos = self.margin
        x_pos = (TOOL_PANEL_WIDTH - self.icon_size) / 2 
        for tool, path in self.tools.items():
            icon = load_icon(path)
            if icon:
                icon = pygame.transform.scale(icon, (self.icon_size, self.icon_size))
                rect = icon.get_rect(topleft=(x_pos, y_pos))
                self.icons[tool] = icon
                self.rects[tool] = rect
                y_pos += self.icon_size + self.spacing

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for key, rect in self.rects.items():
                if rect.collidepoint(mouse_pos):
                    self.active_mode = key
                    print(f"Modo ativado: {self.active_mode}")
                    return True
        return False

    def draw(self):
        panel_rect = pygame.Rect(0, 0, TOOL_PANEL_WIDTH, SCREEN_HEIGHT)
        pygame.draw.rect(self.screen, (230, 230, 230), panel_rect)

        for key, rect in self.rects.items():
            self.screen.blit(self.icons[key], rect.topleft)
            if self.active_mode == key:
                pygame.draw.rect(self.screen, RED, rect, 3)

    def get_active_mode_type(self):
        return self.mode_map.get(self.active_mode)