import turtle
#outline

turtle.bgcolor(0.6,0.5,0.5)
turtle.penup()
turtle.goto(-100,-30)
turtle.pendown()
turtle.begin_fill()
turtle.pencolor("black")
turtle.left(90)
turtle.fd(200)
turtle.right(90)
turtle.fd(300)
turtle.right(90)
turtle.fd(200)
turtle.right(90)
turtle.fd(300)
turtle.end_fill()

#function for rectangles

a=turtle.Turtle()
a.penup()
a.goto(-10,15)
a.pendown()
a.left(90)
def net():
    
    a.fillcolor("red")
    a.begin_fill()
    a.pencolor("red")
    a.forward(130)
    a.right(90)
    a.fd(28)
    a.right(90)
    a.fd(130)
    a.right(90)
    a.fd(28)
    a.end_fill()

# rectangle 1

net()
#rectangle 2

a.penup()
a.goto(72,12)
a.right(90)
net()
print(round(a.xcor()))
print(round(a.ycor()))
a.fillcolor("red")
a.begin_fill()
a.pencolor("red")
#rectangle 3
a.right(58)
a.fd(156)
a.right(122)
a.fd(30)
a.right(58)
a.fd(151)
a.end_fill()
turtle.done()