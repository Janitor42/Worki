import turtle
import time


turtle.hideturtle()




turtle.speed(1)
turtle.delay(0)
screen=turtle.Screen()
screen.tracer(0)

turtle.pensize(5)


def square():
    for i in range(4):
        turtle.forward(90)
        turtle.left(90)



for i in range(1000001):
    turtle.clear()

    square()
    screen.update()
    turtle.right(1)
    time.sleep(0.005)




turtle.mainloop()



