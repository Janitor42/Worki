import turtle
def create_square(a):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)



def one_figure(a,color):
    turtle.color('black',color)
    turtle.begin_fill()
    create_square(a)
    turtle.end_fill()








one_figure(200,'red')
one_figure(175,'blue')
one_figure(150,'grey')
one_figure(125,'pink')
one_figure(100,'purple')
one_figure(75,'yellow')
one_figure(50,'brown')
one_figure(25,'lime')

turtle.mainloop()