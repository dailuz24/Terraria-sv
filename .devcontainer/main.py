import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ruthless Conquest - Python Edition")

clock = pygame.time.Clock()
game = Game(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()