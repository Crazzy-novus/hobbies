#import turtle
#import random
from pickle import TRUE
from turtle import width
import pygame
pygame.init()
width=100
hieght=700
pygame.display.set_mode((width,hieght))
run=True 
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        

    pygame.display.update()
    #clock.tick(60)
pygame.quit()
quit()
