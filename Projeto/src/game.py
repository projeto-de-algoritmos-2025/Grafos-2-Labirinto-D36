import pygame
from grid import Grid
from toolbar import ToolPanel
from settings import *
from pathfinder import dijkstra
from alert_dialog import AlertDialog
import os
print(os.getcwd())


class Game:
    def __init__(self, screen, cols):
        
        self.screen = screen
        self.cols = cols
        self.grid = Grid(ROWS, cols, CELL_SIZE, TOOL_PANEL_WIDTH) 
        self.tool_panel = ToolPanel(screen, ICON_SIZE, SPACING, MARGIN)
        self.alert_dialog = AlertDialog(self.screen, instructions_text, "Entendi!", 800, 600)
        self.alert_dialog.active = True

    def show_msg(self, msg):
        self.alert_dialog = AlertDialog(self.screen, msg, "OK", 400, 180)
        self.alert_dialog.active = True
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.alert_dialog.active:
                self.alert_dialog.handle_event(event)
                continue
            
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
                        self.show_msg(f"Caminho encontrado com {len(path)} passos!")
                    else:
                        self.show_msg("Não foi possível encontrar um caminho.")

                if event.key == pygame.K_c:
                    self.grid.path = []
                    self.grid.visited_nodes = set()
                    self.show_msg("A visualização do caminho foi limpa!")

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

        if self.alert_dialog.active:
            self.alert_dialog.draw()