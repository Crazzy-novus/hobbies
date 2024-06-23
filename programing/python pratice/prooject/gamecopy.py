#10/05/2022
# inilization
column=5
rows=5

#inilization of screen
from string import whitespace
from turtle import Screen, Turtle, bgcolor, color
import pygame
pygame.init()
WIDTH =1300
HIEGHT=700
screen=pygame.display.set_mode((WIDTH,HIEGHT))

#adding heading
pygame.display.set_caption("dv games")

#screen colour
color=(0,0,0)
rect_color=(200,200,200)

#table creation
class tables:
    def __init__(self):
        self.width = int((WIDTH-100)/column)
        self.height = int((HIEGHT-50)/rows)

#creating boxes
    def create_tabes(self):
        self.tables = []
        for r_ow in range(rows):
            box_row = []
            for col_um in range(column):
                box_x=(col_um*self.width)+100   #table x coordinate
                box_y=(r_ow*self.height)+45   #table y coordinates
                tb=pygame.Rect(box_x,box_y,self.width,self.height,) #tables rectangle drawing
                box_row.append(tb)
            self.tables.append(box_row)
    def draw_box(self):
        for row in self.tables:
            for tb in row:
                pygame.draw.rect(screen,rect_color,tb,2)

#box object creating
box_drawn = tables()
box_drawn.create_tabes()

#running screen
run = True
while run:
    screen.fill(color)
    box_drawn.draw_box()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()