import pygame as pg
import sys

def get_fps():
    print(int(fps))


pg.init()
window = pg.display.set_mode((1100, 800))
pg.display.set_caption('LUNE')
clock = pg.time.Clock()

# bg-----------------------------------------------------------------------------------------------------
bg_surface = pg.image.load('background.png').convert()

crashed = False





while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            sys.exit()

    pg.display.update()
    clock.tick(120)
    window.blit(bg_surface, (0, 0))
    fps = clock.get_fps()



    get_fps()




