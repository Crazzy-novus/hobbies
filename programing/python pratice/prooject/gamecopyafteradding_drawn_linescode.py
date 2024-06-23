#11/05/2022
# initialization

#initializating the tables row & column & width & height of each box
column=5
rows=5

#inilization of screen
from http.client import LineTooLong
from string import whitespace
from tracemalloc import start
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


#initialization  class for toy
class toy:
    def __init__(self):
        self.rect_width = int((WIDTH-100)/column)
        self.rect_height = int((HIEGHT-50)/rows)
#creating toys x & y corridinate to draw lines
    def create_toy(self):
        self.toy_start = ()
        self.toy_end = ()
        for r_ow in range(rows):
            toy_row_start =()
            toy_row_end   =()
            for col_um in range(column):
                toy_start=()
                toy_end=()
                box_x=(col_um*self.rect_width)+100
                box_y=(r_ow*self.rect_height)+30  
                self.start_x  = int(box_x+(self.rect_width/2))
                self.start_y  = int(box_y+(self.rect_height/2))
                self.end_x    = self.start_x
                self.end_y    = box_y+self.rect_height-20
            #storing in temporary tuple
                toy_start     = toy_start+(self.start_x,)
                toy_start     = toy_start+(self.start_y,)
                toy_row_start = toy_row_start+(toy_start,)
                toy_end       = toy_end+(self.end_x,)
                toy_end       = toy_end+(self.end_y,)
                toy_row_end   = toy_row_end+(toy_end,)
            #creating tuple list
            self.toy_start    = self.toy_start+(toy_row_start,)
            self.toy_end      = self.toy_end+(toy_row_end,)
#creating class function for drawing line
    def draw_line(self):
        for row_start,row_end in zip(self.toy_start,self.toy_end):
            for st,ed in zip(row_start,row_end):
                pygame.draw.line(screen,rect_color,st,ed,5)
            
#table object class inilization 
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
                tb=pygame.Rect(box_x,box_y,self.width,self.height) #tables rectangle drawing
                box_row.append(tb)
            self.tables.append(box_row)              
    def draw_box(self):
        for row in self.tables:
            for tb in row:
                pygame.draw.rect(screen,rect_color,tb,2)

#box object creating
box_drawn = tables()
box_drawn.create_tabes()
#toy object creating
line_drawn = toy()
line_drawn.create_toy()
#running screen
run = True
while run:
    screen.fill(color)
    box_drawn.draw_box()
    line_drawn.draw_line()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()