import pygame
from grid import Grid
from toolbar import ToolPanel
from settings import *

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

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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