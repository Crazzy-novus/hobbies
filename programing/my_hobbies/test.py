# inilization


column=5
rows=5
WIDTH =1300
HIEGHT=700

class toy:
    def __init__(self):
        self.rect_width = int((WIDTH-100)/column)
        self.rect_height = int((HIEGHT-50)/rows)


#creating toys
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
    def display(self):
        print(self.toy_start)
        print("summa")
        print(self.toy_end)  
ob=toy()
ob.create_toy()
ob.display()