import pygame
import random
from math import fabs


pygame.init()

disPlay_height = 800
disPlay_width = 600
black = (0,0,0)
white = (255,255,255)
guns = False
xB = (disPlay_width * 0.15)
yB = (disPlay_height * .5)
bChange = 0
xG = (disPlay_width * .9)
yG = (disPlay_height * .4)
gravity = 5
velocity = 0
crashed = False
d = {}

disPlay = pygame.display.set_mode((disPlay_height,disPlay_width))
pygame.display.set_caption('FlappyKill')
clock = pygame.time.Clock()
birdImg = pygame.image.load('bird.png')
bg = pygame.image.load("bg.png")
gunImg = pygame.image.load('gun.png')
# ran = random.randint(1,3)


def has_collided_with(rect1,rect2):
    deltay = fabs(rect1.centery - rect2.centery)
    deltax = fabs(rect1.centerx - rect2.centerx)
    return deltay < rect2.height and deltax < rect2.width


def bird(x,y):
    disPlay.blit(birdImg,(x,y))

def gun(x,y):

    disPlay.blit(gunImg,(x,y))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        pressed = pygame.key.get_pressed()


    disPlay.blit(bg, (0, 0))
    velocity =gravity
    yB += velocity
    xG += -6
    bird(xB,yB)
    
    if guns:
        gun(xG,yG)

    if xG < -150:
        guns = False
        xG = (disPlay_width * 1.3)
        yG = (1 + 7*10)

    if yB > 550:
        yB=550

    if yB < 0:
        yB=0

    if pressed[pygame.K_SPACE]:
        yB += -16

    if pressed[pygame.K_l]:
        guns = True


    print(xG,yB)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
