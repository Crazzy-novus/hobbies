#started on 8/05/2022
#last modified on 14/05/2022
# initialization

#initializating the tables row & column & width & height of each box
column=5
rows=5

#inilization of screen
from http.client import LineTooLong
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


#initialization  class for toy
class toy(tables):
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
                box_x=(col_um*box_drawn.width)+100
                box_y=(r_ow*box_drawn.height)+30  
                self.start_x  = int(box_x+(box_drawn.width/2))
                self.start_y  = int(box_y+(box_drawn.height/2))
                self.end_x    = self.start_x
                self.end_y    = box_y+box_drawn.height-20
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
            
#creating head to the charactor
class head(toy,tables):
    def __init__(self):
        self.RADIUS = 23
        self.EYE_RADIUS=3
    def create_head(self):
        self.X_Y_coordinates = ()
        self.EYE_X_Y_coordinates1 = ()
        self.EYE_X_Y_coordinates2 = ()
        for r_ow in range(rows):
            head_X_Y =()
            eye_X_Y1 =()
            eye_X_Y2 =()
            for col_um in range(column):
                head_cor=()
                eye_cor1=()
                eye_cor2=()
                box_x=(col_um*box_drawn.width)+100
                box_y=(r_ow*box_drawn.height)+30  
                line_drawn.start_x  = int(box_x+(box_drawn.width/2))
                line_drawn.start_y  = int(box_y+(box_drawn.height/2))
                self.X = line_drawn.start_x
                self.Y = line_drawn.start_y - 23
                self.EYE_X1 = self.X -9
                self.EYE_Y = self.Y
                self.EYE_X2 = self.X +9
                
        #storing it in tuple
                head_cor = head_cor+(self.X,)
                head_cor = head_cor+(self.Y,)
                head_X_Y = head_X_Y+(head_cor,)
                eye_cor1 = eye_cor1+(self.EYE_X1,)
                eye_cor1 = eye_cor1+(self.EYE_Y,)
                eye_X_Y1 = eye_X_Y1+(eye_cor1,)
                eye_cor2 = eye_cor2+(self.EYE_X2,)
                eye_cor2 = eye_cor2+(self.EYE_Y,)
                eye_X_Y2 = eye_X_Y2+(eye_cor2,)
            self.X_Y_coordinates = self.X_Y_coordinates+(head_X_Y,)
            self.EYE_X_Y_coordinates1 = self.EYE_X_Y_coordinates1+(eye_X_Y1,)
            self.EYE_X_Y_coordinates2 = self.EYE_X_Y_coordinates2+(eye_X_Y2,)

    
    #drawing head codes
    def draw_head(self):
        for X_Y_coordinate,EYE_coordinate1,EYE_coordinate2 in zip(self.X_Y_coordinates,self.EYE_X_Y_coordinates1,self.EYE_X_Y_coordinates2):
            for head_coordinates,eye_coordinates1,eye_coordinates2 in zip(X_Y_coordinate,EYE_coordinate1,EYE_coordinate2):
                pygame.draw.circle(screen,rect_color,head_coordinates,self.RADIUS,5)
                pygame.draw.circle(screen,rect_color,eye_coordinates1,self.EYE_RADIUS,3)
                pygame.draw.circle(screen,rect_color,eye_coordinates2,self.EYE_RADIUS,3)



#box object creating
box_drawn = tables()
box_drawn.create_tabes()

#toy object creating
line_drawn = toy()
line_drawn.create_toy()

#head object creating
head_drawn = head();
head_drawn.create_head()
#running screen
run = True
while run:
    screen.fill(color)
    box_drawn.draw_box()
    line_drawn.draw_line()
    head_drawn.draw_head()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()