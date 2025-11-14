import turtle
import time


# turtle.hideturtle()

turtle.speed(1)
screen=turtle.Screen()
screen.tracer(0)
turtle.pensize(7)
blue_angle=0
red_angle=45

def square_blue():
    global blue_angle
    turtle.setheading(blue_angle)
    turtle.color('blue')
    turtle.penup()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(-45)
    turtle.pendown()

    for i in range(4):
        turtle.forward(90)
        turtle.left(90)
    turtle.penup()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    blue_angle+=1

def square_red():
    global red_angle
    turtle.setheading(red_angle)
    turtle.color('red')
    turtle.penup()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(-45)
    turtle.pendown()

    for i in range(4):
        turtle.forward(90)
        turtle.left(90)
    turtle.penup()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    red_angle+=-2









while True:
    turtle.clear()
    square_blue()
    square_red()
    screen.update()
    turtle.right(1)
    time.sleep(0.1)





turtle.mainloop()