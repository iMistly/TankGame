import pygame as pg

#Screen Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_FPS = 60 #Also controls the speed of the game. 60FPS as base

#Player Settings
PLAYER_WIDTH = 40
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_WIDTH)
PLAYER_SPEED = 1*(60/SCREEN_FPS)
PLAYER_TURNING_SPEED = 360/(120/(60/SCREEN_FPS))
DEFAULT_HEALTH = 3
DEFAULT_MAGAZINE_SIZE = 30

#Control Presets [FORWARD, BACK, LEFT, RIGHT, SHOOT]
CONTROL_PRESET = {"WASD": [pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_q],
                  "ARROWS": [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_RCTRL]}

#Bullet Settings
BULLET_WIDTH = 10
BULLET_SIZE = (BULLET_WIDTH, BULLET_WIDTH)
BULLET_SPEED = 4*(60/SCREEN_FPS)
BULLET_DECELERATION = 0.00
BULLET_LIFESPAN = 200

#Debug
DEBUG = True