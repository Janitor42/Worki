import turtle
"""
turtle.circle(50) #Рисуем круг - (радиус)
turtle.circle(50,90) # Рисуем круг(радиус круга, длинна окружности которую рисуем в градусах)
"""

def create_circle(color,size,long):
    turtle.begin_fill()
    turtle.color('black',color)
    turtle.circle(size)
    turtle.end_fill()
    turtle.circle(size,long)
    turtle.right(180)

def create_lines():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)



















create_circle('brown',60,180)
create_circle('grey',40,180)
create_circle('pink',25,180)

turtle.mainloop()