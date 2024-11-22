import turtle
import time

turtle.left(90)
turtle.penup()
turtle.forward(300)
turtle.pendown()
screen = turtle.Screen()
screen.tracer(0)

speed_y = 5
speed_x = 5

degree = 0

turtle.left(180)

turtle.ht()


def circle():
    turtle.color('black', 'red')
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


while True:

    turtle.clear()
    turtle.left(degree)
    circle()
    if turtle.ycor() < -380:
        speed_y = -5
    if turtle.ycor() > 380:
        speed_y = 5
    if turtle.xcor() < -380:
        speed_x = 5
    if turtle.xcor() > 380:
        speed_x = -5

    turtle.forward(speed_y)
    turtle.left(90)
    turtle.forward(speed_x)
    turtle.right(90)
    print(turtle.xcor())
    time.sleep(0.020)
    screen.update()
