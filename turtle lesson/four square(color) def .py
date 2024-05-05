import turtle

turtle.speed(1)


def one_square(color):
    turtle.color('black', color)
    turtle.begin_fill()
    create_square()
    turtle.end_fill()


def create_square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)


one_square('green')
one_square('orange')
one_square('blue')
one_square('pink')

turtle.mainloop()
