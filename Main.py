import pygame as pg
import sys
import random

# global variable
gravity = 0.1
movement = 0
power = 3
screen_shake = 0
sky_offset = [0, 0]
ground_offset = [0, 770]

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


# sound----------------------------------------------------------------------------------------------
enginesound = pg.mixer.Sound('enginefire.wav')

class Player():
    rocket_surface = pg.image.load('Rocket.png').convert()
    # get rect
    rocket = rocket_surface.get_rect(center=(550, 400))

    def __init__(self, life):
        self.life = life


crashed = False
fule_OK = True
player = Player(100)

while not crashed:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            sys.exit()
        if fule_OK == True:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    movement = 0
                    player.life -= 5
                    movement -= power
                    screen_shake = 20
                    enginesound.play(0, 0, 1)



    pg.display.update()
    clock.tick(120)
    movement += gravity
    player.rocket.centery += movement

    if player.life <= 0:
        print('燃料耗尽')
        fule_OK = False

    if screen_shake > 0:
        screen_shake -= 1

    if screen_shake:
        sky_offset[0] = random.randint(0, 8) - 4
        sky_offset[1] = random.randint(0,10) - 4
        ground_offset[0] = random.randint(0, 4) - 8
        ground_offset[1] = random.randint(770, 775) - 2


    # blit
    window.blit(bg_surface, sky_offset)  # background
    window.blit(Player.rocket_surface, Player.rocket)
    window.blit(moon_surface, ground_offset)  # moon_surface
    #get_fps()
