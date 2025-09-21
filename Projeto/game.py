import pygame
from grid import Grid
from settings import WHITE

class Game:
    def __init__(self, screen, rows=20, cols=20, cell_size=30):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        self.grid = Grid(rows, cols, cell_size)

        icon_size = 50
        spacing = 10

        # posições iniciais do lápis e borracha
        x_pos = screen.get_width() - icon_size - 10  # 10px de margem da borda direita
        y_pos = 10  

        # lápis
        self.pencil_icon = pygame.image.load("assets/img/pencil.png")
        self.pencil_icon = pygame.transform.scale(self.pencil_icon, (icon_size, icon_size))
        self.pencil_rect = self.pencil_icon.get_rect(topleft=(x_pos, y_pos))

        # borracha
        y_pos += icon_size + spacing
        self.eraser_icon = pygame.image.load("assets/img/eraser.png")
        self.eraser_icon = pygame.transform.scale(self.eraser_icon, (icon_size, icon_size))
        self.eraser_rect = self.eraser_icon.get_rect(topleft=(x_pos, y_pos))

        self.state = "draw"

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                print("Mouse clicado em:", mouse_pos)
                print("Pencil rect:", self.pencil_rect)
                print("Eraser rect:", self.eraser_rect)

                if self.pencil_rect.collidepoint(mouse_pos):
                    self.grid.set_mode("pencil")
                    print("Modo lápis ativado")
                elif self.eraser_rect.collidepoint(mouse_pos):
                    self.grid.set_mode("eraser")
                    print("Modo borracha ativado")

        mouse_pos = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()
        col = mouse_pos[0] // self.cell_size
        row = mouse_pos[1] // self.cell_size

        if 0 <= row < self.rows and 0 <= col < self.cols:
            if buttons[0]:  # botão esquerdo pressionado
                if self.grid.mode == "pencil":
                    self.grid.grid[row][col] = 1
                elif self.grid.mode == "eraser":
                    self.grid.grid[row][col] = 0



    def draw(self):
        # tela brancha
        self.screen.fill(WHITE)

        # grid
        self.grid.draw(self.screen)

        # ícones de apagar e desenhar
        self.screen.blit(self.pencil_icon, self.pencil_rect.topleft)
        self.screen.blit(self.eraser_icon, self.eraser_rect.topleft)
