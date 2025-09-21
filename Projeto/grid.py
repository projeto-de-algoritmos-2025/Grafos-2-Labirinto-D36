import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (200, 200, 200)

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.mode = "pencil"  # "pencil" ou "eraser"

    def set_mode(self, mode):
        if mode in ["pencil", "eraser"]:
            self.mode = mode

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        col = mouse_pos[0] // self.cell_size
        row = mouse_pos[1] // self.cell_size

        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.mode == "pencil":
                self.grid[row][col] = 1  # parede
            elif self.mode == "eraser":
                self.grid[row][col] = 0  # vazio

    def draw(self, screen):
        # desenha a grid
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                color = BLACK if self.grid[row][col] == 1 else WHITE
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRAY, rect, 1)
