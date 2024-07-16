r1=eval(input("enter row1:"))
c1=eval(input("enter column1:"))
r2=eval(input("enter row2:"))
c2=eval(input("enter column2:"))
def matinput(r,c,list):
    for i in range(1,r1+1):
        tem=[]
        for j in range(1,c1+1):
            n=eval(input(f"enter the element{i}{j}:"))
            tem.append(n)
        list.append(tem)
if(r1==r2 and c1==c2):
    m1=[]
    m2=[]
    matinput(r1,c1,m1)
    matinput(r2,c2,m2)
    m3=[]
    for i in range(r1):
        tem=[]
        for j in range(c1):
            add=m1[i][j]+m2[i][j]
            tem.append(add)
        m3.append(tem)
print(m1)
print(m2)
print(m3)