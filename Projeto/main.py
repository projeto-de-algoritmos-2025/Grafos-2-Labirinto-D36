import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game import Game

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu Jogo")
clock = pygame.time.Clock()

game = Game(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()
    game.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()