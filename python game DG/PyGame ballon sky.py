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

#bg = background
bg = pygame.image.load('BlueSky.png')
bgY = 0
bgY2 = 846
#bgY2 = bg.get_height()

#blit is re making the backround when you reach the end of screen
def redrawWindow():
    win.blit(bg, (0, bgY ))
    win.blit(bg, (0, bgY2 ))
    
    pygame.display.update()
    
run = True
#scrolling down backround requires adding onto original then equaling negative original value to reset at
#to make clouds go down add to backround and when it reaches max height multiple by negative
while run:
#speed of screen scroll    
    bgY += .07
    bgY2 += .07
    
    if bgY > bg.get_height() :
        bgY =  bg.get_height() * -1 
        
    if bgY2 > bg.get_height() :
        bgY2 = bg.get_height() * -1 
        
##         bgY = -846
##      if bgY2 > 846 :
##         bgY2 = -846
        
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            run = False
            pygame.quit()
            sys.exit()
            
            
    redrawWindow()
