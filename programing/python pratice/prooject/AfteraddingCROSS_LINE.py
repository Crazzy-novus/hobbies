'''

************** started on 8/05/2022 ****************
               last modified on 8/05/2022
**************   initialization     *****************
'''
#  ******** initializating the tables row & column & width & height of each box *********
column=int(input("enter the total number of users"))
rows=5

# *************** inilization of screen ***************

from turtle import Screen, Turtle, bgcolor, color, pos, position
import pygame
import random
pygame.init()
WIDTH =1300
HIEGHT=700
x=200#
y=200#
screen=pygame.display.set_mode((WIDTH,HIEGHT))
gun=pygame.image.load('D:\programing\python pratice\prooject\picsart3.png')
pygame.display.set_icon(gun)
clock=pygame.time.Clock()
 # ************** adding heading *************** #
pygame.display.set_caption("dv games")

# *************** screen colour *************** #
color=(0,0,0)
rect_color=(200,200,200)

# ******** adding the text to the screen ******* #

fornt = pygame.font.Font('freesansbold.ttf',22)
text_x = 10
text_y = 5

# ********** function for displaying text ********** #
def show_number(x,y,n):
    number = fornt.render("random number is :"+ str(n),True,(255,255,255))
    screen.blit(number,(x,y))


def show_text(x,y,n):
    number = fornt.render( n,True,(255,255,255))
    screen.blit(number,(x,y))

# *************** creating user class ***************#
class user():
    def __init__(self):
        self.occurance_0 =0
        self.occurance_2 =0
        self.occurance_4 =0
        self.occurance_6 =0
        self.occurance_8 =0
        

# *************** table object class initialization ********* # 
class tables:
    def __init__(self):
        self.width = int((WIDTH-100)/column)
        self.height = int((HIEGHT-80)/rows)
        
#  *************** function for creating boxes *************** #
    def create_tabes(self):
        self.tables = []
        for r_ow in range(rows):
            box_row = []
            for col_um in range(column):
                box_x=(col_um*self.width)+100   #table x coordinate
                box_y=(r_ow*self.height)+75   #table y coordinates   ######

# ********* creating objects for tables rectangle and store it in a list  ********** #
                tb=pygame.Rect(box_x,box_y,self.width,self.height) 
                box_row.append(tb)
            self.tables.append(box_row)              

# ********** function for diplay tables on the screen ********** #
    def draw_box(self):
        for row in self.tables:
            for tb in row:
                pygame.draw.rect(screen,rect_color,tb,2)


#  ********** initialization  class for toy *************** #
class toy_body(tables):
# *********** creating toys x & y corridinate to draw lines ********** #

    '''  defining the function to generate the required coordinates and diplay the the line '''
    def create_toy(self,col_um,r_ow):
                box_x=(col_um*box_drawn.width)+100
                box_y=(r_ow*box_drawn.height)+60  
                self.start_x  = int(box_x+(box_drawn.width/2)-20) 
                self.start_y  = int(box_y+(box_drawn.height/2))
                self.end_x    = self.start_x
                self.end_y    = box_y+box_drawn.height-20
        # *********** Command for display line *********** #
                pygame.draw.line(screen,rect_color,(self.start_x,self.start_y),(self.end_x,self.end_y),5)
            
# ********** creating head to the charactor ********** #
class toy_head(toy_body,tables):
    def __init__(self):
        self.RADIUS = 23
        self.EYE_RADIUS=3
    '''similar that of line 90 same action but different shape  '''

    def create_head(self,col_um,r_ow):
                box_x=(col_um*box_drawn.width)+100
                box_y=(r_ow*box_drawn.height)+60  
                line_drawn.start_x  = int(box_x+(box_drawn.width/2)-20)#edited part
                line_drawn.start_y  = int(box_y+(box_drawn.height/2))
                self.X = line_drawn.start_x
                self.Y = line_drawn.start_y - 23
                self.EYE_X1 = self.X -9
                self.EYE_Y = self.Y
                self.EYE_X2 = self.X +9
# ************ Command for display head and eyes ************ #
                pygame.draw.circle(screen,rect_color,(self.X,self.Y),self.RADIUS,5)
                pygame.draw.circle(screen,rect_color,(self.EYE_X1,self.EYE_Y),self.EYE_RADIUS,3)
                pygame.draw.circle(screen,rect_color,(self.EYE_X2,self.EYE_Y),self.EYE_RADIUS,3)

# ************ creating hands and legs for the character ************ # 
class toy_hands_legs(toy_body,tables):
    def create_toy_hand_R(self,col_um,r_ow):    
                box_x=(col_um*box_drawn.width)+100
                box_y=(r_ow*box_drawn.height)+60  
                self.hand_R_start_x  = int(box_x+(box_drawn.width/2)-20)
                self.hand_R_start_y  = int(box_y+(box_drawn.height/2))+5#######
                self.hand_R_end_x    = self.hand_R_start_x+30
                self.hand_R_end_y    = self.hand_R_start_y+25
                
                #FOR LEFT HAND
                self.hand_L_end_x   = self.hand_R_end_x-60
                self.hand_L_end_y   = self.hand_R_end_y

            #for legs
                self.leg_R_start_x  = int(box_x+(box_drawn.width/2)-20)
                self.leg_R_start_y  = int(box_y+(box_drawn.height/2))+40
                self.leg_R_end_x    = self.leg_R_start_x+30
                self.leg_R_end_y    = self.leg_R_start_y+25
            #for left
                self.leg_L_end_x    = self.leg_R_start_x-30
                self.leg_L_end_y    = self.leg_R_end_y
            #up to this
        #Command for display hand and legs
                pygame.draw.line(screen,rect_color,(self.hand_R_start_x,self.hand_R_start_y),(self.hand_R_end_x,self.hand_R_end_y),5)
                pygame.draw.line(screen,rect_color,(self.hand_R_start_x,self.hand_R_start_y),(self.hand_L_end_x,self.hand_L_end_y),5)
                pygame.draw.line(screen,rect_color,(self.leg_R_start_x,self.leg_R_start_y),(self.leg_R_end_x,self.leg_R_end_y),5)
                pygame.draw.line(screen,rect_color,(self.leg_R_start_x,self.leg_R_start_y),(self.leg_L_end_x,self.leg_L_end_y),5)

# ********** creating class for display gun ********** #
class toy_gun(tables):
    def create_coordinates(self,col_um,r_ow):
                box_x=(col_um*self.width)+100   #table x coordinate
                box_y=(r_ow*self.height)+60   #table y coordinates
                self.gun_x = int(box_x+(box_drawn.width/2))
                self.gun_y =int(box_y+(box_drawn.height/2))
        #Command for display image
                screen.blit(gun,(self.gun_x,self.gun_y))


          
#creating user objects
user_list =[]
for i in range(0,column):
    user_list.append(user())



#box object creating
box_drawn = tables()
box_drawn.create_tabes()

#toy object creating
line_drawn = toy_body()

#head object creating
head_drawn = toy_head()


#hand object creating
hand_R_drawn = toy_hands_legs()


#gun object creating
gun_drawn = toy_gun()


# ********** function to draw cross line at right box ******** #
def cross_line(x,y):
    for col_um in range(column):
        for r_ow in range(rows):        
            box_x=(col_um*box_drawn.width)+100 
            box_y=(r_ow*box_drawn.height)+75
            if (x>=box_x and x<(box_x+box_drawn.width)) and (y>=box_y and y< box_y+box_drawn.height):
                pygame.draw.rect(screen,rect_color,pygame.Rect(box_x,box_y,box_drawn.width,box_drawn.height))
                pygame.display.update()
                return False
                break

screen.fill(color)
box_drawn.draw_box()
run = True
while run:
    
    for i in range(0,column):
        summa = True
        while summa:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_a]:
                    summa = False
                if event.type == pygame.QUIT:
                    run = False
        
                
            pygame.display.flip()   
        #num = random.randint(0,554)
        num =0
        if(num % 2 != 0):
            num = num-1
        
        pygame.draw.rect(screen,color,pygame.Rect(text_x,text_y,250,20))
        show_number(text_x,text_y,num)
        
        if(num % 10 ==0):
            row =0
            user_list[i].occurance_0 = user_list[i].occurance_0 + 1
            if(user_list[i].occurance_0==1):
                head_drawn.create_head(i,row)
            elif(user_list[i].occurance_0==2):
                line_drawn.create_toy(i,row)
                hand_R_drawn.create_toy_hand_R(i,row)
            elif(user_list[i].occurance_0==3):
                gun_drawn.create_coordinates(i,row)
            elif(user_list[i].occurance_0>3):
                click = True
                while click:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed():
                                position =pygame.mouse.get_pos()
                                click =cross_line(position[0],position[1])
                                
                pygame.display.update()                
        

        elif(num % 10 ==2):
            row =1
            user_list[i].occurance_2 = user_list[i].occurance_2 + 1
            if(user_list[i].occurance_2==1):
                head_drawn.create_head(i,row)
            elif(user_list[i].occurance_2==2):
                line_drawn.create_toy(i,row)
                hand_R_drawn.create_toy_hand_R(i,row)
            elif(user_list[i].occurance_2==3):
                gun_drawn.create_coordinates(i,row)

            elif(user_list[i].occurance_2>3):
                click = True
                while click:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed():
                                position =pygame.mouse.get_pos()
                                click =cross_line(position[0],position[1])
                                
                pygame.display.update()                
        
    
        elif(num % 10 ==4):
            row =2
            user_list[i].occurance_4 = user_list[i].occurance_4 + 1
            if(user_list[i].occurance_4==1):
                head_drawn.create_head(i,row)
            elif(user_list[i].occurance_4==2):
                line_drawn.create_toy(i,row)
                hand_R_drawn.create_toy_hand_R(i,row)
            elif(user_list[i].occurance_4==3):
                gun_drawn.create_coordinates(i,row)

            elif(user_list[i].occurance_4>3):
                click = True
                while click:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed():
                                position =pygame.mouse.get_pos()
                                click =cross_line(position[0],position[1])
                                
                pygame.display.update()                
        
    
        elif(num % 10 ==6):
            row =3
            user_list[i].occurance_6 = user_list[i].occurance_6 + 1
            if(user_list[i].occurance_6==1):
                head_drawn.create_head(i,row)
            elif(user_list[i].occurance_6==2):
                line_drawn.create_toy(i,row)
                hand_R_drawn.create_toy_hand_R(i,row)
            elif(user_list[i].occurance_6==3):
                gun_drawn.create_coordinates(i,row)
            elif(user_list[i].occurance_6>3):
                click = True
                while click:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed():
                                position =pygame.mouse.get_pos()
                                click =cross_line(position[0],position[1])
                                
                pygame.display.update()                
        
        elif(num % 10 ==8):
            row =4
            user_list[i].occurance_8 = user_list[i].occurance_8 + 1
            if(user_list[i].occurance_8==1):
                head_drawn.create_head(i,row)
            elif(user_list[i].occurance_8==2):
                line_drawn.create_toy(i,row)
                hand_R_drawn.create_toy_hand_R(i,row)
            elif(user_list[i].occurance_8==3):
                gun_drawn.create_coordinates(i,row)
            elif(user_list[i].occurance_8>3):
                click = True
                while click:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed():
                                position =pygame.mouse.get_pos()
                                click =cross_line(position[0],position[1])
                                
                pygame.display.update()                
        
        
        #clock.tick(60)            
        pygame.display.update()



    pygame.display.flip()
    clock.tick(60)
pygame.quit()