import pygame as pg
import math
from CONSTANTS import *
import entities as ent

#Pygame initialization
pg.init()
mainDisplay = pg.display.set_mode(SCREEN_RES)

#Game elemtents
list_players = []
list_bullets = []

list_players.append(ent.Player(coord=(50,50)))
gameActive = True
if __name__ == "__main__":
    while gameActive:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                
        for player in list_players:
            mainDisplay.blit(player.image, player.rect)
        
        pg.display.update()