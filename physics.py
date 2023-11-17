from CONSTANTS import *
import entities as ent
import math
import pygame as pg

tank_img = pg.image.load('assets/tank.png')
tank_img = pg.transform.rotate(tank_img, -90)

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
        # # Angle Text
        # font = pg.font.SysFont("Comic Sans", 20)
        # text = font.render(str(player.angle), True, pg.color.Color('white'))
        # text_rect = text.get_rect()
        # text_rect.center = (SCREEN_WIDTH/2, 10)
        # mainDisplay.blit(text, text_rect)
        # mainDisplay.blit(player.image, player.rect)
        #Draw tank
        tank_rotated = pg.transform.rotate(tank_img, -player.angle)
        tank_rect = tank_rotated.get_rect()
        tank_rect.center = player.rect.center
        mainDisplay.blit(tank_rotated, tank_rect)
    for bullet in list_bullets:
        mainDisplay.blit(bullet.image, bullet.rect)