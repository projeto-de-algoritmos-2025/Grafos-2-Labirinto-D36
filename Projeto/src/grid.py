import pygame
from settings import *
import os

try:
    ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')
except NameError:
    ASSETS_PATH = os.path.join(os.path.abspath('.'), '..', 'assets')

FALLBACK_COLORS = {
    "grass": (255, 255, 255),
    "sand": (244, 164, 96),
    "rock": (139, 137, 137),
    "water": (30, 144, 255),
    "wall": (0, 0, 0)
}

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
            "water": load_sprite([
                os.path.join(ASSETS_PATH, "sprites/water/water1.png"),
                os.path.join(ASSETS_PATH, "sprites/water/water2.png"),
                os.path.join(ASSETS_PATH, "sprites/water/water3.png"),
            ], is_list=True)
        }
        
        default_sprite = self.sprites["grass"]
        self.grid = [[{"type": "grass", "sprite": default_sprite, "frame_index": 0} for _ in range(cols)] for _ in range(rows)]

    def update(self, row, col, mode_type):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            cell = self.grid[row][col]
            if mode_type == "start":
                if self.start_node:
                    r, c = self.start_node
                    self.grid[r][c]["type"] = "grass"
                    self.grid[r][c]["sprite"] = self.sprites["grass"]
                self.start_node = (row, col)
                return 
            elif mode_type == "end":
                if self.end_node:
                    r, c = self.end_node
                    self.grid[r][c]["type"] = "grass"
                    self.grid[r][c]["sprite"] = self.sprites["grass"]
                self.end_node = (row, col)
                return 
            
            cell["type"] = mode_type
            cell["sprite"] = self.sprites.get(mode_type)
            cell["frame_index"] = 0

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_timer > self.animation_speed:
            self.animation_timer = current_time
            for row_data in self.grid:
                for cell in row_data:
                    if isinstance(cell["sprite"], list):
                        cell["frame_index"] = (cell["frame_index"] + 1) % len(cell["sprite"])

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
                    if isinstance(sprite, list):
                        frame = sprite[cell["frame_index"]]
                        screen.blit(pygame.transform.scale(frame, rect.size), rect.topleft)
                    else:
                        screen.blit(pygame.transform.scale(sprite, rect.size), rect.topleft)
                else:
                    fallback_color = FALLBACK_COLORS.get(cell["type"], BLACK)
                    pygame.draw.rect(screen, fallback_color, rect)

                overlay = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
                if (row, col) in self.visited_nodes and (row, col) not in self.path:
                    overlay.fill((200, 200, 200, 100)) 
                if (row, col) in self.path:
                    overlay.fill((255, 255, 0, 150))
                if (row, col) == self.start_node:
                    overlay.fill((0, 255, 0, 180)) 
                if (row, col) == self.end_node:
                    overlay.fill((255, 0, 0, 180)) 
                screen.blit(overlay, rect.topleft)
                pygame.draw.rect(screen, GRAY, rect, 1)