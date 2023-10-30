# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:22:08 2021

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

W, H = 564, 846
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Balloon Sky')
gameover = 0

BXAxis = 200
BYAxis = 500
ScrollSpeed = .02

#bg = background
bg = pygame.image.load('BlueSky.png')
bgY = 0
bgY2 = 846
#bgY2 = bg.get_height()

class B1(object):
    blank = [pygame.image.load(os.path.join('images', '0.png'))]
    fly = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,4)]
    
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
        if (gameover == 1):
            pygame.display.flip()
            time.sleep(8)
            run = False
            pygame.quit()
            sys.exit()
            
        elif self.flying:
            #
            #
            #
            #
            win.blit(self.fly[0], (self.x,self.y))
             

#blit is re making the backround when you reach the end of screen
def redrawWindow():
    
    win.blit(bg, (0, bgY ))
    win.blit(bg, (0, bgY2 ))
    
    Balloon.draw(win)
    pygame.display.update()
    
run = True
#where to put baloon on screen
Balloon = B1(BXAxis, BYAxis, 0, 0 )
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
    
        
##         bgY = -846
##      if bgY2 > 846 :
##         bgY2 = -846
        
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            run = False
            pygame.quit()
            sys.exit()
            
    if keys[pygame.K_LEFT]:
       # BXAxis is the location left/right on the screen x axis lower the number more to the left 
        BXAxis = BXAxis - .5
        Balloon = B1(BXAxis, BYAxis, 100, 100)
        if BXAxis < -180:
            gameover = 1
        
        
    if keys[pygame.K_RIGHT]:
        BXAxis = BXAxis + .5
        Balloon = B1(BXAxis, BYAxis, 100, 100)
        if BXAxis > 550:
            gameover = 1
            
        
    if keys[pygame.K_UP]:
       ScrollSpeed += .001
       Balloon = B1(BXAxis, BYAxis, 100, 100)
       
        
    if keys[pygame.K_DOWN]:
        ScrollSpeed -= .001
        Balloon = B1(BXAxis, BYAxis, 100, 100)
        
    
        
        
        
            
            
    redrawWindow()
