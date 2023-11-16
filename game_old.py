import pygame as pg
import math

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.image.fill(pg.color.Color(color))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(pg.color.Color('white'))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.direction = direction
        self.lifespan = 200
        self.speed = 4

def playerShoot(plyr, dir) -> Bullet:
    return Bullet(plyr.rect.centerx + math.sqrt(0.5)*plyr.rect.width*math.cos(dir), #Edge of player
                  plyr.rect.centery + math.sqrt(0.5)*plyr.rect.height*math.sin(dir), #Edge of player
                  dir)
            

def burst(plyr):
    burstList = []
    for i in range(360, 0, -5):
        burstList.append(Bullet(plyr.rect.centerx + math.sqrt(0.5)*plyr.rect.width*math.cos(math.radians(i)), #Edge of player
                           plyr.rect.centery + math.sqrt(0.5)*plyr.rect.height*math.sin(math.radians(i)), #Edge of player
                           math.radians(i)))
    return burstList
    

pg.init()
width, height = 480, 480
screen = pg.display.set_mode((width, height))

hit_sound = pg.mixer.Sound('Bonk.wav')
hit_sound.set_volume(0.1)

player = Player(100, 100, 'red')
player2 = Player(200, 200, 'blue')

list_of_bullets = {player: [], player2: []}
maxBullets = -1
mouseIsPressed = False

# Game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

    # FPS
    pg.time.Clock().tick(60)

    screen.fill(pg.color.Color('black'))
    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)

    # Get mouse degrees from player
    mouse_pos = pg.mouse.get_pos()
    mouse_pos = [(mouse_pos[0] - player.rect.centerx, mouse_pos[1] - player.rect.centery), 
                 (mouse_pos[0] - player2.rect.centerx, mouse_pos[1] - player2.rect.centery)]
    mouse_dir = [math.atan2(mouse_pos[0][1], mouse_pos[0][0]), 
                 math.atan2(mouse_pos[1][1], mouse_pos[1][0])]
    
    # Movement
    keys = pg.key.get_pressed()
    if keys[pg.K_a] and player.rect.x > 0:
        player.rect.x -= 1
    if keys[pg.K_d] and player.rect.x < width - player.rect.width:
        player.rect.x += 1
    if keys[pg.K_w] and player.rect.y > 0:
        player.rect.y -= 1
    if keys[pg.K_s] and player.rect.y < height - player.rect.height:
        player.rect.y += 1

    # Shoot
    if not mouseIsPressed and pg.mouse.get_pressed()[0]:
        mouseIsPressed = True
        # list_of_bullets[player].append(playerShoot(player, mouse_dir[0]))
        # Burst
        list_of_bullets[player].extend(burst(player))
    elif not pg.mouse.get_pressed()[0]:
        mouseIsPressed = False
    
    # Update bullets
    for item in list_of_bullets:
        for bullet in list_of_bullets[item]:
            bullet.x += math.cos(bullet.direction) * bullet.speed
            bullet.y += math.sin(bullet.direction) * bullet.speed
            bullet.rect.center = (bullet.x, bullet.y)
            screen.blit(bullet.image, bullet.rect)

            #Lifespan
            bullet.lifespan -= 1
            #Delete bullet if out of bounds or lifespan is 0
            if bullet.rect.x > width + 10 or bullet.rect.x < -10 or bullet.rect.y > height + 10 or bullet.rect.y < -10 or bullet.lifespan <= 0:
                if bullet in list_of_bullets[item]:
                    list_of_bullets[item].remove(bullet)
            #Fade out
            if bullet.lifespan < 20:
                bullet.image.set_alpha(bullet.lifespan * 10)

            #Collision with player
            if bullet.rect.colliderect(player.rect):
                #Play hit sound
                hit_sound.play()
                if bullet in list_of_bullets[item]:
                    list_of_bullets[item].remove(bullet)
            if bullet.rect.colliderect(player2.rect):
                #Play hit sound
                hit_sound.play()
                if bullet in list_of_bullets[item]:
                    list_of_bullets[item].remove(bullet)

            #Bounce
            if bullet.rect.y > height - bullet.rect.height or bullet.rect.y < 0:
                bullet.direction = -bullet.direction
            if bullet.rect.x > width - bullet.rect.width or bullet.rect.x < 0:
                bullet.direction = math.pi - bullet.direction

    #Quit game
    if keys[pg.K_ESCAPE]:
        pg.quit()
        raise SystemExit

    pg.display.update()