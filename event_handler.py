import pygame as pg
from CONSTANTS import *

class EventHandler():
    def __init__(self, display):
        self.display = display

    def listen(self, events, keys):
        for event in events:
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()

def player_control_process(list_players, list_bullets, keys):
    for player in list_players:
        player.move(keys)
        player.update_location()
        if keys[player.controls["SHOOT"]]:
            list_bullets.append(player.shoot())

def update_bullets(list_bullets):
    for bullet in list_bullets:
        bullet.update_location()
        #Delete bullet if out of bounds or lifespan is 0
        if bullet.coord["x"] > SCREEN_WIDTH + 10 or bullet.coord["x"] < -10 or bullet.coord["y"] > SCREEN_HEIGHT + 10 or bullet.coord["y"] < -10 or bullet.lifespan <= 0:
            if bullet in list_bullets:
                list_bullets.remove(bullet)

def update_screen(mainDisplay, list_players, list_bullets):
    for player in list_players:
        # Rotate player
        player.image = pg.transform.rotate(player.texture, -player.angle)
        player.rect = player.image.get_rect()
        player.rect.center = (player.coord["x"], player.coord["y"])
        mainDisplay.blit(player.image, player.rect)
    for bullet in list_bullets:
        mainDisplay.blit(bullet.image, bullet.rect)