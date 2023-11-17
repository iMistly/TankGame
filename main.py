import pygame as pg
from CONSTANTS import *
import entities as ent
from physics import *
from event_handler import *

#Pygame initialization
pg.init()
mainDisplay = pg.display.set_mode(SCREEN_RES)
eventHandler = EventHandler(mainDisplay)

#Game elemtents
list_players = []
list_bullets = []

list_players.append(ent.Player(coord = (50,50), controls=[pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_q]))
list_players.append(ent.Player(coord = (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50), controls=[pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_q]))
list_players[1].angle = 180
gameActive = True
if __name__ == "__main__":
    while gameActive:
        # ticks per seconds
        pg.time.Clock().tick(60)
        # stuff to update every tick
        mainDisplay.fill(pg.color.Color('black'))
        keys = pg.key.get_pressed()
        events = pg.event.get()

        # event handling
        eventHandler.listen(events, keys)
        player_control_process(list_players, list_bullets, keys)
        update_bullets(list_bullets)

        update_screen(mainDisplay, list_players, list_bullets)
        pg.display.update()