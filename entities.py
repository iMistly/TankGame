import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self, color = "random", coord: tuple = (0,0), controls: list = [None, None, None, None]):
        '''
        color: Pick color according to pygame's list of colors pg.color.THECOLORS
        coord: (x, y) tuple
        controls: [up, left, down, right]
        '''
        super().__init__()
        
        if color == "random":
            color = random.choice(list(pg.color.THECOLORS.values()))
            
        self.image = pg.Surface((20, 20))
        self.image.fill(pg.color.Color(color))
        self.rect = self.image.get_rect()
        self.rect.center = coord
        
        #Controls
        self.controls = {"UP": controls[0],
                         "LEFT": controls[1], 
                         "DOWN": controls[2], 
                         "RIGHT": controls[3]
                         }