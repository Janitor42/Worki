import turtle

#region
def block(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)

def half_block(width,height):
    turtle.forward(width/2)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width/2)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width/2)


def move_to_place(how_many,width,height):
    turtle.forward(-how_many*width)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
def row_1(how_many,width,height):

    for i in range(how_many):
        block(width,height)

def row_2(how_many,width,height):
    move_to_place(how_many,width,height)
    half_block(width,height)
    for i in range(how_many-1):
        block(width, height)
    half_block(width, height)
    move_to_place(how_many,width,height)


def build(width,height,long_row,height_row):
    for i in range(height_row//2):
        row_1(long_row,width,height)
        row_2(long_row,width,height)
    if height_row%2==1:
        row_1(long_row, width, height)
#endregion

turtle.speed(20)





build(50,25,10,40)


turtle.mainloop()