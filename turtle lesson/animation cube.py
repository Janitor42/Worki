import  turtle
import time


# turtle.hideturtle()

turtle.speed(10)
turtle.delay(1)
screen=turtle.Screen()

screen.tracer(0)

turtle.pensize(5)




def square():
    turtle.begin_fill()
    turtle.color('black', 'red')
    for i in range(5):
        turtle.forward(90)
        turtle.left(90)
    turtle.end_fill()

    turtle.begin_fill()
    turtle.color('black', 'red')
    turtle.right(45)
    turtle.forward(45)
    turtle.left(45)
    turtle.forward(90)
    turtle.left(135)
    turtle.forward(45)
    turtle.left(45)
    turtle.forward(90)
    turtle.forward(-90)
    turtle.end_fill()

    turtle.begin_fill()
    turtle.color('black', 'red')
    turtle.right(90)
    turtle.forward(90)
    turtle.right(135)
    turtle.forward(45)
    turtle.right(45)
    turtle.forward(90)
    turtle.right(135)
    turtle.forward(45)
    turtle.right(45)
    turtle.forward(90)
    turtle.end_fill()

    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)


#
for i in range(361):
    turtle.clear()
    square()
    screen.update()
    turtle.right(1)
    time.sleep(0.005)




turtle.mainloop()