import pygame as pg
import sys

def get_fps():
    print(int(fps))


pg.init()
window = pg.display.set_mode((576, 1024))
pg.display.set_caption('LUNE')
clock = pg.time.Clock()

crashed = False

java_surface = pg.image.load('black paint.png')



while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            sys.exit()

    pg.display.update()
    clock.tick(120)
    fps = clock.get_fps()
    window.blit(bgw, (0, 0))



    window.blit(java_surface, (pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]))
    get_fps()




