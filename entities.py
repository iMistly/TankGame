import pygame as pg
from CONSTANTS import *
import entities as ent
import math
import random

class Player(pg.sprite.Sprite):
    def __init__(self, image: pg.image = "no_image", coord: tuple = (0,0), controls: list = "Dummy"):
        """
        image: Pick color according to pygame's list of colors pg.color.THECOLORS
        coord: (x, y) tuple
        controls: [up, left, down, right] default is dummy
        """
        super().__init__()
        
        self.texture = pg.image.load(image) if image != "no_image" else pg.image.load("assets/none.png")
        self.texture = pg.transform.scale(self.texture, (PLAYER_WIDTH*1.1, PLAYER_WIDTH*1.1))
        self.image = pg.surface.Surface(PLAYER_SIZE)
        self.image.fill(pg.color.Color(random.choice(list(pg.color.THECOLORS.keys()))))
        self.rect = self.image.get_rect()
        self.x = coord[0]
        self.y = coord[1]
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.dummy = False
        #Controls
        if len(controls) != 5 or controls == "Dummy":
            self.dummy = True
            self.controls = None
        else:
            self.controls = {"FORWARD": controls[0],
                             "LEFT": controls[1], 
                             "BACK": controls[2], 
                             "RIGHT": controls[3],
                             "SHOOT": controls[4]
                             }
    
    def move(self, keys):
        if keys[self.controls["FORWARD"]]:
            self.x += math.cos(math.radians(self.angle)) * PLAYER_SPEED
            self.y += math.sin(math.radians(self.angle)) * PLAYER_SPEED
        if keys[self.controls["BACK"]]:
            self.x -= math.cos(math.radians(self.angle))
            self.y -= math.sin(math.radians(self.angle))
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
        self.rect.center = (self.x, self.y)
        self.angle %= 360
        
class Bullet(pg.sprite.Sprite):
    def __init__(self, coord, angle):
        super().__init__()
        self.image = pg.Surface(BULLET_SIZE)
        self.image.fill(pg.color.Color('white'))
        self.rect = self.image.get_rect()
        self.x = coord[0]
        self.y = coord[1]
        self.rect.center = (self.x, self.y)
        self.angle = angle
        self.lifespan = BULLET_LIFESPAN
        self.speed = BULLET_SPEED

    def update_location(self):
        self.x += math.cos(self.angle) * BULLET_SPEED
        self.y += math.sin(self.angle) * BULLET_SPEED
        self.rect.center = (self.x, self.y)
        self.lifespan -= 1
        #Fade out
        if self.lifespan < 20:
            self.image.set_alpha(self.lifespan * 10)
        #Bounce
        if self.y > SCREEN_HEIGHT - self.rect.height or self.y < 0:
            self.angle = -self.angle
        if self.x > SCREEN_WIDTH - self.rect.width or self.x < 0:
            self.angle = math.pi - self.angle