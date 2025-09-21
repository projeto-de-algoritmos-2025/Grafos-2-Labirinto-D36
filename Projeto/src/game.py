import pygame
from grid import Grid
from toolbar import ToolPanel
from settings import *
from pathfinder import dijkstra

class Game:
    def __init__(self, screen, cols):
        self.screen = screen
        self.cols = cols
        self.grid = Grid(ROWS, cols, CELL_SIZE, TOOL_PANEL_WIDTH) 
        self.tool_panel = ToolPanel(screen, ICON_SIZE, SPACING, MARGIN)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            self.tool_panel.handle_event(event)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Executando o algoritmo de Dijkstra...")
                    self.grid.path = []
                    self.grid.visited_nodes = set()
                    path, visited = dijkstra(self.grid, self.grid.start_node, self.grid.end_node)
                    self.grid.path = path
                    self.grid.visited_nodes = visited
                    if path:
                        print(f"Caminho encontrado com {len(path)} passos!")
                    else:
                        print("Não foi possível encontrar um caminho.")
                if event.key == pygame.K_c:
                    self.grid.path = []
                    self.grid.visited_nodes = set()
                    print("Caminho e visualização limpos.")

        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            mouse_pos = pygame.mouse.get_pos()

            if mouse_pos[0] > TOOL_PANEL_WIDTH:
                col = (mouse_pos[0] - TOOL_PANEL_WIDTH) // CELL_SIZE
                row = mouse_pos[1] // CELL_SIZE
                
                if 0 <= row < ROWS and 0 <= col < self.cols:
                    mode_type = self.tool_panel.get_active_mode_type()
                    self.grid.update(row, col, mode_type)

    def draw(self):
        self.screen.fill(WHITE)
        self.grid.draw(self.screen)
        self.tool_panel.draw()