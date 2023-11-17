import pygame as pg
from CONSTANTS import *
from global_vars import *
import entities as ent
from event_handler import EventHandler

#Pygame initialization
pg.init()
handler = EventHandler(mainDisplay)

list_players.append(ent.Player(coord = (SCREEN_WIDTH-50, SCREEN_HEIGHT-50), controls=[pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_q]))
list_players.append(ent.Player(image = "assets/tank.png", coord = (50,50), controls=[pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_q]))
list_players[0].angle = 180

if __name__ == "__main__":
    while gameActive:
        # ticks per seconds
        clock.tick(60)
        # stuff to update every tick
        mainDisplay.fill(pg.color.Color('black'))
        handler.keys = pg.key.get_pressed()
        handler.events = pg.event.get()

        # event handling
        handler.listen()
        handler.player_control_process()
        handler.update_bullets()
        # debug
        if DEBUG:
            handler.debug()

        handler.update_screen()
        pg.display.update()