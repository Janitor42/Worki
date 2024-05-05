
import turtle
def create_square(size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
def one_figure(size,color):
    turtle.color('black',color)
    turtle.begin_fill()
    create_square(size)
    turtle.end_fill()























one_figure(200,'orange')
one_figure(175,'blue')
one_figure(150,'grey')
one_figure(125,'pink')
one_figure(100,'purple')
one_figure(75,'yellow')
one_figure(50,'brown')
one_figure(25,'lime')







turtle.mainloop()