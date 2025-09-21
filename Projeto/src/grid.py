import pygame
from settings import BLACK, GRAY, CELL_SIZE

class Grid:
    def __init__(self, rows, cols, cell_size, offset_x):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.offset_x = offset_x
        self.animation_timer = 0
        self.animation_speed = 1000 # tá em ms

        self.sprites = {
            "grass": pygame.image.load("../assets/sprites/grass/grass.png"),
            "sand": pygame.image.load("../assets/sprites/sand/sand.png"),
            "rock": pygame.image.load("../assets/sprites/rock/rock.png"),
            "water": [
                pygame.image.load("../assets/sprites/water/water1.png"),
                pygame.image.load("../assets/sprites/water/water2.png"),
                pygame.image.load("../assets/sprites/water/water3.png"),
            ]
        }
        self.grid = [[{"type": "grass", "sprite": self.sprites["grass"], "frame_index": 0} for _ in range(cols)] for _ in range(rows)]

    def update(self, row, col, mode_type):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            cell = self.grid[row][col]
            
            sprite_map = {
                "sand": self.sprites["sand"],
                "rock": self.sprites["rock"],
                "water": self.sprites["water"],
                "grass": self.sprites["grass"]
            }

            cell["type"] = mode_type
            cell["sprite"] = sprite_map.get(mode_type)
            cell["frame_index"] = 0

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_timer > self.animation_speed:
            self.animation_timer = current_time
            for row in range(self.rows):
                for col in range(self.cols):
                    cell = self.grid[row][col]
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

                if cell["type"] == "wall":
                    pygame.draw.rect(screen, BLACK, rect)
                else:
                    if cell["sprite"]:
                        if isinstance(cell["sprite"], list):
                            frame = cell["sprite"][cell["frame_index"]]
                            screen.blit(pygame.transform.scale(frame, (self.cell_size, self.cell_size)), rect.topleft)
                        else:
                            screen.blit(pygame.transform.scale(cell["sprite"], (self.cell_size, self.cell_size)), rect.topleft)

                pygame.draw.rect(screen, GRAY, rect, 1)