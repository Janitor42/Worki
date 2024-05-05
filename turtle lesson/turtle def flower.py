import turtle

def create_circle_center(color,size):
    turtle.begin_fill()
    turtle.color('black',color)
    turtle.circle(size)
    turtle.end_fill()
    # turtle.circle(size,long)

def create_circle(color,size):
    turtle.right(180)

    turtle.begin_fill()
    turtle.color('black',color)
    turtle.circle(size)
    turtle.end_fill()
    turtle.right(180)
    turtle.circle(60,40)
























































create_circle_center('brown',60)

create_circle('blue',30)
create_circle('lime',30)
create_circle('orange',30)
create_circle('yellow',30)
create_circle('pink',30)
create_circle('purple',30)
create_circle('green',30)
create_circle('gray',30)
create_circle('red',30)


turtle.mainloop()