import pygame as pg
import sys

# global variable
gravity = 0.01
movement = 0

def get_fps():
    fps = clock.get_fps()
    print(int(fps))


pg.init()
window = pg.display.set_mode((1100, 800))
pg.display.set_caption('LUNE')
clock = pg.time.Clock()

# bg-----------------------------------------------------------------------------------------------------
bg_surface = pg.image.load('background.png').convert()
# moon_surface--------------------------------------------------------------------------------------------
moon_surface = pg.image.load('moon_surface.png').convert()
# the rocket----------------------------------------------------------------------------------------------


class Player():
    rocket_surface = pg.image.load('Rocket.png').convert()
    # get rect
    rocket = rocket_surface.get_rect(center=(550, 400))
    def __init__(self):
        pass



crashed = False


player = Player()


while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            sys.exit()

    pg.display.update()
    clock.tick(120)
    movement += gravity
    Player.rocket.centery += movement
    #blit
    window.blit(bg_surface, (0, 0))     #background
    window.blit(Player.rocket_surface, Player.rocket)
    window.blit(moon_surface, (0, 770))     #moon_surface





    get_fps()




