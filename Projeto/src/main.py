import pygame
from game import Game
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


cols = (SCREEN_WIDTH - TOOL_PANEL_WIDTH) // CELL_SIZE

game = Game(screen, cols=cols)

running = True
while running:
    game.handle_events()
    game.draw()
    pygame.display.flip()
    clock.tick(60)