import pygame as pg
import sys
import Main


pg.init()
window = pg.display.set_mode((1100, 800))
pg.display.set_caption('LUNE')
bg = pg.image.load('background.png')
T = pg.image.load('Title.png')
font = pg.font.SysFont("Times New Roman, Arial", 40)
color = pg.Color('white')
text = font.render('click s to start!', True, color)


while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                Main.main()
                pg.quit()
                quit()
                sys.exit()
    pg.display.update()
    window.blit(bg, (0, 0))
    window.blit(T, (100, 100))
    window.blit(text, (200, 700))