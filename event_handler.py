import pygame as pg
from CONSTANTS import *
from global_vars import *

class EventHandler():
    def __init__(self):
        self.display = mainDisplay
        self.events = None
        self.keys = None

    def listen(self):
        for event in self.events:
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                pg.quit()
            if event.type == pg.KEYDOWN:
                for player in list_players:
                    if not player.dummy:
                        if event.key == player.controls["SHOOT"] and player.magazine > 0:
                            list_bullets.append(player.shoot())

    def player_control_process(self):
        for player in list_players:
            if not player.dummy:
                player.move(self.keys)
                player.update_location()

    def update_bullets(self):
        for bullet in list_bullets:
            bullet.update_location()
            #Delete bullet if out of bounds or lifespan is 0
            if bullet.x > SCREEN_WIDTH + 10 or bullet.x < -10 or bullet.y > SCREEN_HEIGHT + 10 or bullet.y < -10 or bullet.lifespan <= 0:
                if bullet in list_bullets:
                    bullet.owner.magazine += 1
                    list_bullets.remove(bullet)


    def update_screen(self):
        for player in list_players:
            # Rotate image but not rect
            rotated_texture = pg.transform.rotate(player.texture, -player.angle)
            rotated_rect = rotated_texture.get_rect(center=player.rect.center)
            mainDisplay.blit(rotated_texture, rotated_rect)
        for bullet in list_bullets:
            mainDisplay.blit(bullet.image, bullet.rect)

    def debug(self):
        font = pg.font.SysFont('Arial', 20)
        mainDisplay.blit(font.render("FPS: " + str(int(clock.get_fps())), False, pg.color.Color('white')), (0,0))
        mainDisplay.blit(font.render("Bullets: " + str(len(list_bullets)), False, pg.color.Color('white')), (0,20))
        mainDisplay.blit(font.render("Players: " + str(len(list_players)), False, pg.color.Color('white')), (0,40))
        for player in list_players:
            mainDisplay.blit(player.image, player.rect)