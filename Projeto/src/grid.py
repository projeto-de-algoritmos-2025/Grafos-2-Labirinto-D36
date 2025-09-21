import pygame
from settings import *
import os

try:
    ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')
except NameError:
    ASSETS_PATH = os.path.join(os.path.abspath('.'), '..', 'assets')


def load_sprite(path, is_list=False):
    try:
        if is_list:
            sprites = []
            for file_path in path:
                sprites.append(pygame.image.load(file_path).convert_alpha())
            return sprites
        else:
            return pygame.image.load(path).convert_alpha()
    except FileNotFoundError:
        print(f"AVISO: Arquivo de sprite não encontrado em '{path}'")
        return None

class Grid:
    def __init__(self, rows, cols, cell_size, offset_x):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.offset_x = offset_x
        self.animation_timer = 0
        self.animation_speed = 300 
        self.start_node = None
        self.end_node = None
        self.path = []
        self.visited_nodes = set()

        self.sprites = {
            "grass": load_sprite(os.path.join(ASSETS_PATH, "sprites/grass/grass.png")),
            "sand": load_sprite(os.path.join(ASSETS_PATH, "sprites/sand/sand.png")),
            "rock": load_sprite(os.path.join(ASSETS_PATH, "sprites/rock/rock.png")),
            "wall": load_sprite(os.path.join(ASSETS_PATH, "sprites/wall/wall.png")),
            "water": load_sprite(os.path.join(ASSETS_PATH, "sprites/water/water.png")),
            "start": load_sprite(os.path.join(ASSETS_PATH, "sprites/flags/init.png")),
            "end": load_sprite(os.path.join(ASSETS_PATH, "sprites/flags/finish.png")),
            "passos": load_sprite(os.path.join(ASSETS_PATH, "sprites/passos/passos.png")),
        }
        
        self.grid = [[{"type": "grass", "sprite": self.sprites["grass"], "frame_index": 0} for _ in range(cols)] for _ in range(rows)]

    def update(self, row, col, mode_type):
        if mode_type is None:
            return
        
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        if mode_type == "start":
            if self.start_node:
                r, c = self.start_node
                self.grid[r][c]["type"] = "grass"
                self.grid[r][c]["sprite"] = self.sprites.get("grass")
            self.start_node = (row, col)
        elif mode_type == "end":
            if self.end_node:
                r, c = self.end_node
                self.grid[r][c]["type"] = "grass"
                self.grid[r][c]["sprite"] = self.sprites.get("grass")
            self.end_node = (row, col)

        if mode_type == "eraser":
            if (row, col) in [self.start_node, self.end_node]:
                return
            self.grid[row][col]["type"] = "grass"
            self.grid[row][col]["sprite"] = self.sprites.get("grass")
            return
        
        cell = self.grid[row][col]
        cell["type"] = mode_type
        cell["sprite"] = self.sprites.get(mode_type)

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * self.cell_size + self.offset_x,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                
                cell = self.grid[row][col]
                sprite = cell["sprite"]
                
                if sprite:
                    screen.blit(pygame.transform.scale(sprite, rect.size), rect.topleft)
                else:
                    fallback_color = FALLBACK_COLORS.get(cell["type"], BLACK)
                    pygame.draw.rect(screen, fallback_color, rect)

                overlay = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
                if (row, col) in self.path:
                    if (cell["type"] != "start" and cell["type"] != "end"):
                        screen.blit(pygame.transform.scale(self.sprites["passos"], rect.size), rect.topleft)
                        overlay.fill((200, 200, 200, 100)) 
                if (row, col) in self.visited_nodes and (row, col) not in self.path:
                    overlay.fill((200, 200, 200, 100)) 
                
                screen.blit(overlay, rect.topleft)

                #pygame.draw.rect(screen, GRAY, rect, 1)