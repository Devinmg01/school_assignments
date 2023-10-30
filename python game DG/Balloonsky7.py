##from os import environ
##environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
import os
import sys
import math
import random
import time

pygame.init()

goingleft = False
goingright = False
flyby = False
zoomloc=555
attitude=0
updown=0

W, H = 564, 846
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('BalloonSky')
gameover=0

BXAxis = 200
scrollspeed = .01



bg = pygame.image.load(os.path.join('images', 'Bluesky.png'))
TS = pygame.image.load(os.path.join('images', 'TitleScreen.png'))
gs = pygame.image.load(os.path.join('images', 'ground.png'))

bgY = 0
bgY2 = 846
#bgY2 = bg.get_height()

Arial30 = pygame.font.SysFont('Arial',30)
Arial75 = pygame.font.SysFont('Arial',75)

class B1(object):
    blank = [pygame.image.load(os.path.join('images', '0.png'))]
    fly = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1, 5)]
    #crash = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(4, 7)]
    #pop = pygame.image.load(os.path.join('images', '8.png'))
    

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.flying = True
        self.blanking = True
        self.crashing = False
        self.popping = False
        self.bumping = False
        self.width = width
        self.height = height
        self.flyCount = 0
        self.crashCount = 0

        
        
    def draw(self, win):
        global goingleft
        global goingright
        if (gameover == 1):
            win.blit(gs, (0, bgY, ))
            pygame.display.flip()
            time.sleep(4)
            run = False
            pygame.quit()
            sys.exit()
            
                                 
        elif self.flying:
            if not(goingleft) and not(goingright):
                win.blit(self.fly[0],(self.x,self.y))
            if (goingleft == True):
                win.blit(self.fly[1],(self.x,self.y))
                goingleft = False
            if (goingright == True):
                win.blit(self.fly[3],(self.x,self.y))
                goingright = False

class fokker(object):
    a_left = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(30, 33)]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
       win.blit(self.a_left[attitude],(self.x,self.y))
   

def redrawWindow():
   
    win.blit(bg, (0, bgY, ))
    win.blit(bg, (0, bgY2,))   
    
    Balloon.draw(win)
    if (flyby == True):
        zoom.draw(win)
    pygame.display.update()

#First Show the Title Screen for 4 Seconds
win.blit(TS, (0, bgY, ))

# Add Name of Programmer
text = Arial30.render("John Q. Programmer", 1, (0,0,0))
win.blit (text,(50,500))

pygame.display.update()
time.sleep(4)

run = True
gameover=False
flyby=False
#name = class(Xcoord, Ycoord, width, Height)
Balloon = B1(BXAxis, 500, 100, 100 )
zoom = fokker(zoomloc,75,50,50)

while run:
    
    # these lines control the speed
    bgY += scrollspeed
    bgY2 += scrollspeed

    if (scrollspeed < 0):   
        if bgY < bg.get_height() * -1:
            bgY = bg.get_height()
        if bgY2 < bg.get_height() * -1:
            bgY2 = bg.get_height()

    if (scrollspeed>0):        
        if bgY > 846:
            bgY = -846
        if bgY2 > 846:
            bgY2 = -846

    if (updown>2):
        attitude = 2
    if (updown<-2):
        attitude = 1
    if (updown <2) and (updown>-2):
        attitude = 0

    #print(updown)    
        
            
 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            run = False
            win.blit(gs, (0, 0, ))
            pygame.display.flip()
            time.sleep(.5)
            text = Arial75.render("GAME OVER", 1, (255,0,0))
            win.blit (text,(95,300))
            pygame.display.flip()
            time.sleep(4)
            run = False
            pygame.quit()
            sys.exit()
            
    if keys[pygame.K_z]:
        flyby=True
        pygame.mixer.music.load('airplane.mp3')
        pygame.mixer.music.play(1)
            
    if keys[pygame.K_UP]:
        scrollspeed = scrollspeed + .001
        Balloon = B1(BXAxis, 500, 100, 100 )
        updown +=1
        
    if keys[pygame.K_DOWN]:
        scrollspeed = scrollspeed - .001
        Balloon = B1(BXAxis, 500, 100, 100 )
        updown -=1
        
    if keys[pygame.K_LEFT]:
        # BXAxis is the location left/rigth on the screen - lower to the left
        BXAxis = BXAxis - .75
        if (BXAxis < -183):
                BXAxis = 555
        Balloon = B1(BXAxis, 500, 100, 100 )
        goingleft = True

    if keys[pygame.K_RIGHT]:
       # BXAxis is the location left/rigth on the screen - higher to the right
        BXAxis = BXAxis + .75
        if (BXAxis >555):
                BXAxis = -183
        Balloon = B1(BXAxis, 500, 100, 100 )
        goingright = True
        
    if (flyby==True):
        zoom = fokker(zoomloc,25,50,50)
        #zoom = fokker(zoomloc,750,50,50) is the bottom of the screen
        zoomloc = zoomloc-.75
        if (zoomloc < -200):
            zoomloc = 555
            flyby=False
       
    
    
    redrawWindow()
