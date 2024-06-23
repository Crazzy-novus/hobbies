#started on 8/05/2022
#last modified on 29/05/2022
# initialization

#initializating the tables row & column & width & height of each box
column=6
rows=5

#inilization of screen
from cmath import rect
from http.client import LineTooLong
from string import whitespace
from tkinter import Y, Scale
from turtle import Screen, Turtle, bgcolor, color
import pygame
pygame.init()
WIDTH =1300
HIEGHT=700
x=200#
y=200#
Scale = 100
screen=pygame.display.set_mode((WIDTH,HIEGHT))
gun=pygame.image.load('D:\programing\python pratice\prooject\picsart3.png')
#gun=pygame.transform.scale(gun,(int(gun.get_width()*Scale),int(gun.get_height()*Scale)))
#rect = gun.get_rect()#
#rect.center =(x,y) #
pygame.display.set_icon(gun)

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
class toy_body(tables):
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
                self.start_x  = int(box_x+(box_drawn.width/2)-20) #edited part
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
class toy_head(toy_body,tables):
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
                line_drawn.start_x  = int(box_x+(box_drawn.width/2)-20)#edited part
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

#creating hands and legs for the character 
class toy_hands_legs(toy_body,tables):
    def create_toy_hand_R(self):
        #for hand
        self.toy_hand_R_start = ()
        self.toy_hand_R_end = ()
        
        #tuple for left hand
        """starting point for left and right are same . 
        so we can use hand right start for habd left start also"""
        self.toy_hand_L_end = ()
        #TUPLE FOR LEFT HAND OVER

        #for legs
        self.toy_leg_R_start = ()
        self.toy_leg_R_end = ()

        #for left 
        """starting point for left and right are same . 
        so we can use hand right start for habd left start also"""
        self.toy_leg_L_end = ()
        
        #upto this

        for r_ow in range(rows):
            toy_hand_R_row_start =()
            toy_hand_R_row_end   =()
            #tuple for left hand 
            #starting point for left and right are same . so we can use hand right start for habd left start also
            toy_hand_L_row_end   =()
            #TUPLE FOR LEFT HAND OVER
            
            #for legs
            toy_leg_R_row_start =()
            toy_leg_R_row_end   =()
            #for left
            toy_leg_L_row_end   =()
            
            #up to this
            for col_um in range(column):
                toy_hand_R_start=()
                toy_hand_R_end=()
            #tuple for left hand
                toy_hand_L_end=()
            #up to this

            #for legs
                toy_leg_R_start=()
                toy_leg_R_end=()
                #for left
                toy_leg_L_end=()
            #up to this    
                box_x=(col_um*box_drawn.width)+100
                box_y=(r_ow*box_drawn.height)+30  
                self.hand_R_start_x  = int(box_x+(box_drawn.width/2)-20)#edited part
                self.hand_R_start_y  = int(box_y+(box_drawn.height/2))+5
                self.hand_R_end_x    = self.hand_R_start_x+30
                self.hand_R_end_y    = self.hand_R_start_y+25
                
                #FOR LEFT HAND
                self.hand_L_end_x   = self.hand_R_end_x-60
                self.hand_L_end_y   = self.hand_R_end_y

            #for legs
                self.leg_R_start_x  = int(box_x+(box_drawn.width/2)-20)#edited part
                self.leg_R_start_y  = int(box_y+(box_drawn.height/2))+45
                self.leg_R_end_x    = self.leg_R_start_x+30
                self.leg_R_end_y    = self.leg_R_start_y+25
            #for left
                self.leg_L_end_x    = self.leg_R_start_x-30
                self.leg_L_end_y    = self.leg_R_end_y
            #up to this

             #storing in temporary tuple
                toy_hand_R_start     = toy_hand_R_start+(self.hand_R_start_x,)
                toy_hand_R_start     = toy_hand_R_start+(self.hand_R_start_y,)
                toy_hand_R_row_start = toy_hand_R_row_start+(toy_hand_R_start,)
                toy_hand_R_end       = toy_hand_R_end+(self.hand_R_end_x,)
                toy_hand_R_end       = toy_hand_R_end+(self.hand_R_end_y,)
                toy_hand_R_row_end   = toy_hand_R_row_end+(toy_hand_R_end,)
            #FOR LEFT HAND
                toy_hand_L_end       = toy_hand_L_end+(self.hand_L_end_x,)
                toy_hand_L_end       = toy_hand_L_end+(self.hand_L_end_y,)
                toy_hand_L_row_end   = toy_hand_L_row_end+(toy_hand_L_end,)

            #for legs
                toy_leg_R_start     = toy_leg_R_start+(self.leg_R_start_x,)
                toy_leg_R_start     = toy_leg_R_start+(self.leg_R_start_y,)
                toy_leg_R_row_start = toy_leg_R_row_start+(toy_leg_R_start,)
                toy_leg_R_end       = toy_leg_R_end+(self.leg_R_end_x,)
                toy_leg_R_end       = toy_leg_R_end+(self.leg_R_end_y,)
                toy_leg_R_row_end   = toy_leg_R_row_end+(toy_leg_R_end,)
            #for left
                toy_leg_L_end       = toy_leg_L_end+(self.leg_L_end_x,)
                toy_leg_L_end       = toy_leg_L_end+(self.leg_L_end_y,)
                toy_leg_L_row_end   = toy_leg_L_row_end+(toy_leg_L_end,)

            #up to this

            #creating tuple list
            self.toy_hand_R_start    = self.toy_hand_R_start+(toy_hand_R_row_start,)
            self.toy_hand_R_end      = self.toy_hand_R_end+(toy_hand_R_row_end,)

            #FOR LEFT HAND
            self.toy_hand_L_end      = self.toy_hand_L_end+(toy_hand_L_row_end,)

            #for legs
            self.toy_leg_R_start    = self.toy_leg_R_start+(toy_leg_R_row_start,)
            self.toy_leg_R_end      = self.toy_leg_R_end+(toy_leg_R_row_end,)
            #for left
            self.toy_leg_L_end      = self.toy_leg_L_end+(toy_leg_L_row_end,)
    
    
    # creating hand code
    def draw_hand_R(self):
        for row_head_start,row_head_end,row_head_end_y in zip(self.toy_hand_R_start,self.toy_hand_R_end,self.toy_hand_L_end):
            for st_hand_R,ed_hand_R,ed_hand_L in zip(row_head_start,row_head_end,row_head_end_y):
                pygame.draw.line(screen,rect_color,st_hand_R,ed_hand_R,5)
                pygame.draw.line(screen,rect_color,st_hand_R,ed_hand_L,5)

        #for legs
        for row_leg_start,row_leg_end,row_leg_end_y in zip(self.toy_leg_R_start,self.toy_leg_R_end,self.toy_leg_L_end):
                for st_leg_R,ed_leg_R,ed_leg_L in zip(row_leg_start,row_leg_end,row_leg_end_y):
                    pygame.draw.line(screen,rect_color,st_leg_R,ed_leg_R,5)
                    pygame.draw.line(screen,rect_color,st_leg_R,ed_leg_L,5)

#creating class for display gun
class toy_gun(tables):
    def create_coordinates(self):
        self.gun_coordinates1 =()
        self.gun_coordinates =()
        
        for r_ow in range(rows):
            tem_gun_coordinates =()
            for col_um in range(column):
                tem_gun_coor =()
                box_x=(col_um*self.width)+100   #table x coordinate
                box_y=(r_ow*self.height)+30   #table y coordinates
                self.gun_x = int(box_x+(box_drawn.width/2))
                self.gun_y =int(box_y+(box_drawn.height/2))
                tem_gun_coor = tem_gun_coor+(self.gun_x,)
                tem_gun_coor = tem_gun_coor+(self.gun_y,)
                tem_gun_coordinates = tem_gun_coordinates+(tem_gun_coor,)
            self.gun_coordinates1 = self.gun_coordinates1 +(tem_gun_coordinates,)

    def place(x,y):  # function to convert list to int values which only accept by screen.blit() command
        screen.blit(gun,(x,y))

    def draw_gun(self):
        for row in self.gun_coordinates1:
            for coor in row:
                x = coor[0]
                y = coor[1]
                toy_gun.place(x,y)
        


#box object creating
box_drawn = tables()
box_drawn.create_tabes()

#toy object creating
line_drawn = toy_body()
line_drawn.create_toy()

#head object creating
head_drawn = toy_head()
head_drawn.create_head()

#hand object creating
hand_R_drawn = toy_hands_legs()
hand_R_drawn.create_toy_hand_R()

#gun object creating
gun_drawn = toy_gun()
gun_drawn.create_coordinates()
#gun_drawn.draw_gun()
#running screen
run = True
while run:
    screen.fill(color)
    #screen.blit(gun, rect)
    gun_drawn.draw_gun()
    box_drawn.draw_box()
    line_drawn.draw_line()
    head_drawn.draw_head()
    hand_R_drawn.draw_hand_R()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()