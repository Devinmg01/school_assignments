# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 19:22:09 2021

@author: devin
"""



import pygame
from pygame.locals import *
import os
import sys
import math
import random
import time


pygame.init()

goingLeft = False
goingRight = False
goingDown = False
flyby = False
flyby2 = False
bombsAway = False
zoomloc=555
zoomloc2 = -183
attitude=0
updown=0
USEREVENT = 24
#x value of bomb
bombloc = 240
#y value of bomb
bombHeight = 50
bombDrop = random.randint(-120, 500)



W, H = 564, 846
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Balloon Sky')
gameover = 0

BXAxis = 200
BYAxis = 500
ScrollSpeed = .01

#bg = background
bg = pygame.image.load(os.path.join('images', 'Bluesky.png'))
TS = pygame.image.load(os.path.join('images', 'TitleScreen.png'))
gs = pygame.image.load(os.path.join('images', 'ground.png'))



bgY = 0
bgY2 = 846
#bgY2 = bg.get_height()

Arial30 = pygame.font.SysFont('Arial',30)
Arial75 = pygame.font.SysFont('Arial',75)

#class that controlls the baloon and its values
class B1(object):
    blank = [pygame.image.load(os.path.join('images', '0.png'))]
    fly = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,5)]
    
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
        self.hitbox = (x, y, width, height)
        
        
    def draw(self, win):
        global goingLeft
        global goingRight
        global goingDown
        
        #self.hitbox = (self.x + 10 , self.y  , self.width+68 , self.height+80)   
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        
        
        if (gameover == 1):
            win.blit(gs, (0, bgY, ))
            pygame.display.flip()
            time.sleep(1)
            run = False
            pygame.quit()
            sys.exit()
            
        
            
        elif self.flying:
            #
            #
            #
            #
            if not(goingLeft) and not(goingRight):
                win.blit(self.fly[0], (self.x,self.y))
            if (goingLeft == True):
                win.blit(self.fly[1], (self.x,self.y))
                goingLeft = False
            if (goingDown == True):
                win.blit(self.fly[2], (self.x,self.y))
                goingDown = False
            if (goingRight == True):
                win.blit(self.fly[3], (self.x,self.y))
                goingRight = False
            self.hitbox = (self.x + 65  , self.y + 65 , self.width , self.height)   
            pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            
        #elif self.popping: 
            
    
        
        
            
#ceates and sets the values the planes will be on                 
class fokker(object):
    a_left = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(30,33)]    
    #a_right = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(40,43)]
    
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4
        
    def draw(self, win):
        win.blit(self.a_left[attitude], (self.x,self.y))
        #win.blit(self.a_right[attitude], (self.x,self.y))
        
        
class fokker2(object):    
    a_right = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(40,43)]
    
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4
        
    def draw(self, win):
        win.blit(self.a_right[attitude], (self.x,self.y))
        
        
        
class bomb(object):
    b_down = pygame.image.load(os.path.join('images', '33.png'))
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width    
        self.height = height
        self.hitbox = (x,y,width,height)
           
        
    def draw(self, win):
        
        win.blit(self.b_down, (self.x,self.y))
        self.hitbox = (self.x + 14, self.y + 14 , self.width -10, self.height)
        #creates rectangle around object and 1st set of numbers is color
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        
        
    def collide(self, rect):
        #self.hitbox = (self.x + 14, self.y + 14 , self.width -10, self.height)
        #print(rect[0])
        #print(self.hitbox[1])
        #print(self.hitbox[1] + self.hitbox[3])
        if rect[0] - rect[2] < self.hitbox[0] and rect[0] + rect[2] > self.hitbox[0]:
            if rect[1] < self.hitbox[1]  and rect[1] + rect [3] > self.hitbox[1] - self.hitbox[3]:
                return True
        return False
       

#blit is re making the backround when you reach the end of screen
def redrawWindow():
    
    win.blit(bg, (0, bgY ))
    win.blit(bg, (0, bgY2 ))
    
    Balloon.draw(win)
    if (flyby == True):
        zoom.draw(win)
    if (flyby2 == True):
        zoom2.draw(win)
    if (bombsAway == True):
        boom.draw(win)
    #for x in objects:
        #x.draw()
        
    pygame.display.update()

#dispalys title screen    
win.blit(TS, (0, bgY, ))

text = Arial30.render("Devin Grace", 1, (0,0,0))
win.blit (text,(50,500))
pygame.display.update()
time.sleep(4)   
run = True
gameover = False
flyby = False
flyby2 = False
bombsAway = False
pygame.time.set_timer(USEREVENT+2,random.randrange(8000,9500))

#where to put baloon on screen
Balloon = B1(BXAxis, BYAxis, 75, 100 )
zoom = fokker(zoomloc, 50,50,50)
zoom2 = fokker2(zoomloc2,50,50,50)
objects = []
boom = bomb(bombloc,bombHeight,50,50)
objects.append(boom)
#scrolling down backround requires adding onto original then equaling negative original value to reset at
#to make clouds go down add to backround and when it reaches max height multiple by negative
while run:
#speed of screen scroll    
    
    

    bgY += ScrollSpeed
    bgY2 += ScrollSpeed
    
    if (ScrollSpeed > 0):
        if bgY > bg.get_height() :
            bgY =  bg.get_height() * -1 
        
        if bgY2 > bg.get_height() :
            bgY2 = bg.get_height() * -1 
            
    if (ScrollSpeed < 0):
        if bgY < bg.get_height() * -1 :
            bgY =  bg.get_height() 
        
        if bgY2 < bg.get_height() * -1 :
            bgY2 = bg.get_height() 
            
    if(updown>2):
        attitude=2
    if(updown<-2):
        attitude = 1 
    if (updown < 2)and (updown > -2):
        attitude = 0           
    #print(updown)
    #used to go through each hitbox number and compare to check collision
    for event in objects:
        if boom.collide(Balloon.hitbox):
            #pygame.time.delay(1000)
            print("hit")
            run = False
            win.blit(gs, (0, 0, ))
            pygame.display.flip()
            time.sleep(.5)
            text = Arial75.render("GAME OVER!", 1, (255,0,0))
            win.blit (text,(95,300))
            pygame.display.flip()
            time.sleep(4)
            run = False
            pygame.quit()
            sys.exit()
            
      
    
   
        
    
    
    
    
    
    
        
##         bgY = -846
##      if bgY2 > 846 :
##         bgY2 = -846
        
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            run = False
            win.blit(gs, (0, 0, ))
            pygame.display.flip()
            time.sleep(.5)
            text = Arial75.render("GAME OVER!", 1, (255,0,0))
            win.blit (text,(95,300))
            pygame.display.flip()
            time.sleep(4)
            run = False
            pygame.quit()
            sys.exit()
        if event.type == USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0: 
                flyby = True
                #objects.append(boom)
            if r == 1:
                flyby2 = True
                #objects.append(boom)
            if r == 1 or r == 0:
                #while bombsAway == True:
                    #objects.append(boom)
                    bombDrop = random.randint(-120, 500)
        
        
           
        
                    
                
                
            
                
    if keys[pygame.K_z]:
        flyby2 = True
        pygame.mixer.music.load('airplane.mp3')
        pygame.mixer.music.play(1)
    
    
    
    if keys[pygame.K_LEFT]:
       # BXAxis is the location left/right on the screen x axis lower the number more to the left  
        #print(BXAxis)
        BXAxis = BXAxis - .2
        Balloon = B1(BXAxis, BYAxis, 75, 100)
        if BXAxis < -180:
            BXAxis = 552
        goingLeft = True
        
    if keys[pygame.K_RIGHT]:
        #print(BXAxis)
        BXAxis = BXAxis + .2
        Balloon = B1(BXAxis, BYAxis, 75, 100)
        if BXAxis > 552:
            BXAxis = -180
        goingRight = True
            
        
    if keys[pygame.K_UP]:
       ScrollSpeed += .0001
       Balloon = B1(BXAxis, BYAxis, 75, 100)
       updown +=1
       
       
        
    if keys[pygame.K_DOWN]:
        ScrollSpeed -= .0001
        Balloon = B1(BXAxis, BYAxis, 75, 100)
        goingDown = True
        updown -=1
        
    #add bomb down here    
    if (flyby==True):
        zoom = fokker(zoomloc,50,50,50)
        zoomloc = zoomloc-.25
        pygame.mixer.music.load('airplane.mp3')
        pygame.mixer.music.play(1)
        if (zoomloc == bombDrop):
            bombsAway = True
        if (zoomloc < -180):
            zoomloc = 555
            flyby = False
            
            
    if (flyby2 == True):
        zoom2 = fokker2(zoomloc2,50,50,50)
        zoomloc2 += .25
        pygame.mixer.music.load('airplane.mp3')
        pygame.mixer.music.play(1)
        if (zoomloc2 == bombDrop):
            bombsAway = True         
        if (zoomloc2 > 552):
            zoomloc2 = -183
            flyby2 = False
            
    if (bombsAway == True):
        
        boom = bomb(bombDrop, bombHeight, 50, 50) 
        bombHeight +=  .3
        #objects.append(boom)
        #print(bombHeight)
        if (bombHeight > 900):
            #bombDrop = random.randint(-120, 500)
            bombHeight = 50
            bombDrop = 555555
            bombsAway = False
            
            
        
        
        
            
            
    redrawWindow()
