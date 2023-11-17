import pygame as pg

class EventHandler():
    def __init__(self, display):
        self.display = display

    def listen(self, events, keys):
        for event in events:
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                