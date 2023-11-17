import pygame as pg
from CONSTANTS import *
import entities as ent
import math
import random

class Player(pg.sprite.Sprite):
    def __init__(self, image: pg.image = "random_color", coord: tuple = (0,0), controls: list = [None, None, None, None, None]):
        """
        image: Pick color according to pygame's list of colors pg.color.THECOLORS
        coord: (x, y) tuple
        controls: [up, left, down, right] default is dummy
        """
        super().__init__()
        
        if image == "random_color":
            self.texture = pg.Surface(PLAYER_SIZE)
            self.image = self.texture
            self.image.fill(pg.color.Color(random.choice(list(pg.color.THECOLORS.keys()))))
        else:
            self.texture = pg.image.load(image)
            self.texture = pg.transform.scale(self.texture, PLAYER_SIZE)
            self.image = self.texture
        self.rect = self.image.get_rect()
        self.coord = {"x": coord[0], "y": coord[1]}
        self.rect.center = (self.coord["x"], self.coord["y"])
        self.angle = 0
        
        #Controls
        self.controls = {"FORWARD": controls[0],
                         "LEFT": controls[1], 
                         "BACK": controls[2], 
                         "RIGHT": controls[3],
                         "SHOOT": controls[4]
                         }
    
    def move(self, keys):
        if keys[self.controls["FORWARD"]]:
            self.coord["x"] += math.cos(math.radians(self.angle))
            self.coord["y"] += math.sin(math.radians(self.angle))
        if keys[self.controls["BACK"]]:
            self.coord["x"] -= math.cos(math.radians(self.angle))
            self.coord["y"] -= math.sin(math.radians(self.angle))
        if keys[self.controls["LEFT"]]:
            self.angle -= PLAYER_TURNING_SPEED
        if keys[self.controls["RIGHT"]]:
            self.angle += PLAYER_TURNING_SPEED
        
    def shoot(self):
        angle_rad = math.radians(self.angle)
        return ent.Bullet((self.rect.centerx + math.sqrt(0.5)*self.rect.width*math.cos(angle_rad), #Edge of player
                          self.rect.centery + math.sqrt(0.5)*self.rect.height*math.sin(angle_rad)), #Edge of player
                          angle_rad)
    
    def update_location(self):
        self.rect.center = (self.coord["x"], self.coord["y"])
        self.angle %= 360
        
class Bullet(pg.sprite.Sprite):
    def __init__(self, coord, angle):
        super().__init__()
        self.image = pg.Surface(BULLET_SIZE)
        self.image.fill(pg.color.Color('white'))
        self.rect = self.image.get_rect()
        self.coord = {"x": coord[0], "y": coord[1]}
        self.rect.center = (self.coord["x"], self.coord["y"])
        self.angle = angle
        self.lifespan = BULLET_LIFESPAN
        self.speed = BULLET_SPEED

    def update_location(self):
        self.coord["x"] += math.cos(self.angle)
        self.coord["y"] += math.sin(self.angle)
        self.rect.center = (self.coord["x"], self.coord["y"])
        self.lifespan -= 1
        #Fade out
        if self.lifespan < 20:
            self.image.set_alpha(self.lifespan * 10)
        #Bounce
        if self.coord["y"] > SCREEN_HEIGHT - self.rect.height or self.coord["y"] < 0:
            self.angle = -self.angle
        if self.coord["x"] > SCREEN_WIDTH - self.rect.width or self.coord["x"] < 0:
            self.angle = math.pi - self.angle