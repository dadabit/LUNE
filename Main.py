import pygame as pg
import sys
import random


def get_fps():
    fps = clock.get_fps()
    print(int(fps))


def consolelog(out):
    print(out)


pg.init()
window = pg.display.set_mode((1100, 800))
pg.display.set_caption('LUNE')
clock = pg.time.Clock()

# bg-----------------------------------------------------------------------------------------------------
bg_surface = pg.image.load('background.png').convert()
# moon_surface--------------------------------------------------------------------------------------------
moon_surface = pg.image.load('moon_surface.png').convert()
#astroid---------------------------------------------------------------------------------------------------
asto_surface = pg.image.load('astroid.png').convert()

# sound----------------------------------------------------------------------------------------------
enginesound = pg.mixer.Sound('enginefire.wav')
explosionsound = pg.mixer.Sound('explosion.wav')


class Player():
    rocket_surface = pg.image.load('Rocket.png').convert()
    # get rect
    rocket = rocket_surface.get_rect(center=(550, 400))

    def __init__(self, life):
        self.life = life


class Particles:
    def __init__(self):
        self.parti_list = []

    def emit(self):
        if self.parti_list:
            self.delete_parti()
            for particle in self.parti_list:
                particle[0][1] += particle[2]
                particle[1] -= 0.2
                pg.draw.circle(window, pg.Color('white'), particle[0], int(particle[1]))

    def add(self):
        posx = Player.rocket[0] + 25
        posy = Player.rocket[1] + 40
        radius = 10
        direction = random.randint(1, 2)
        self.parti_list.append([[posx, posy], radius, direction])

    def delete_parti(self):
        particle_copy = [particle for particle in self.parti_list if particle[1] > 0]
        self.parti_list = particle_copy

class Astroid:
    def __init__(self, xspeed, yspeed):
        self.astroList = []
        self.xs = xspeed
        self.ys = yspeed

    def move(self):
        if self.astroList:
            self.delll()
            for astro in self.astroList:
                astro[0][0] += astro[1][0]
                astro[0][1] += astro[1][1]
                window.blit(asto_surface, (astro[0][0], astro[0][1]))

    def add(self):
        speed = [self.xs, self.ys]
        posx = 0
        posy = player.rocket[1]
        self.astroList.append([[posx, posy], speed])

    def delll(self):
        pass

player = Player(100)

def main():
    # global variable
    gravity = 0.1
    movement = 0
    power = 7
    screen_shake = 0
    sky_offset = [0, 0]
    ground_offset = [0, 770]

    crashed = False
    fule_OK = True

    particle1 = Particles()
    astroid1 = Astroid(7, 0.1)

    PARTICLEEVENT = pg.USEREVENT + 1
    ASTROIDEVENT = pg.USEREVENT + 2
    pg.time.set_timer(PARTICLEEVENT, 100)
    pg.time.set_timer(ASTROIDEVENT, 900)

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
                if event.type == PARTICLEEVENT:
                    particle1.add()
            if event.type == ASTROIDEVENT:
                astroid1.add()


        pg.display.update()
        clock.tick(120)
        movement += gravity
        player.rocket.centery += movement

        if player.life <= 0:
            consolelog('燃料耗尽')
            fule_OK = False

        if player.rocket[1] >= ground_offset[1]:
            explosionsound.play()
            pg.time.wait(900)
            pg.quit()
            quit()
            sys.exit()

        if screen_shake > 0:
            screen_shake -= 1

        if screen_shake:
            sky_offset[0] = random.randint(0, 8) - 4
            sky_offset[1] = random.randint(0, 10) - 4
            ground_offset[0] = random.randint(0, 4) - 4
            ground_offset[1] = random.randint(770, 775) - 4

        # blit

        window.blit(bg_surface, sky_offset)  # background
        window.blit(Player.rocket_surface, Player.rocket)
        particle1.emit()
        astroid1.move()

        window.blit(moon_surface, ground_offset)  # moon_surface
        get_fps()


main()