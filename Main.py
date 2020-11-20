import pygame
import sys

pygame.init()
window = pygame.display.set_mode((576, 1024))
pygame.display.set_caption('LUNE')
clock = pygame.time.Clock()

crashed = False

java_surface = pygame.image.load('OIP.xxoNYARhgoSrOw6GuCzE9AHaGQ.jpeg')


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()

    pygame.display.update()
    clock.tick(120)



    window.blit(java_surface, (0, 0))



