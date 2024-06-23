import pygame
pygame.init()
WIDTH=700
HEIGHT=700  
screen=pygame.display.set_mode((HEIGHT,WIDTH))


clock=pygame.time.Clock()
color=(222,111,123)
color1=(0,0,0)
run =True
while run:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    st_x=400;st_y=300;en_x=400;en_y=500
    pygame.draw.line(screen,color1,(st_x,st_y),(en_x,en_y),20)
    
    #hand
    str_x=400;str_y=st_y+60;enr_x=480;enr_y=420
    pygame.draw.line(screen,color1,(str_x,str_y),(enr_x,enr_y),15)
    stl_x=400;stl_y=st_y+60;enl_x=320;enl_y=420
    pygame.draw.line(screen,color1,(stl_x,stl_y),(enl_x,enl_y),15)
    
    #legs
    stbr_x=400;stbr_y=en_y-5;enbr_x=480;enbr_y=560
    pygame.draw.line(screen,color1,(stbr_x,stbr_y),(enbr_x,enbr_y),15)
    stbl_x=400;stbl_y=en_y-5;enbl_x=320;enbl_y=560
    pygame.draw.line(screen,color1,(stbl_x,stbl_y),(enbl_x,enbl_y),15)
    
    #head
    X=400;Y=220;RADIUS=82
    pygame.draw.circle(screen,color1,(X,Y),RADIUS,10)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
