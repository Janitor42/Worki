import turtle

def create_square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)


def one_square(color):
    turtle.color('black',color)
    turtle.begin_fill()
    create_square()
    turtle.end_fill()


one_square('green')
one_square('orange')
one_square('red')
one_square('blue')

turtle.mainloop()