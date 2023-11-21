import pygame as pg
from CONSTANTS import *
from global_vars import *
import entities as ent
from event_handler import EventHandler

#Pygame initialization
pg.init()
handler = EventHandler()


list_players.append(ent.Player(1, image = "assets/tank.png", coord = (50,50), controls=CONTROL_PRESET["WASD"]))
list_players.append(ent.Player(2, image = "assets/tank.png", coord = (SCREEN_WIDTH-50, 50), angleDeg=180, controls=CONTROL_PRESET["ARROWS"]))

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

        handler.update_screen()
        pg.display.update()