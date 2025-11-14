import turtle
"""
turtle.circle(50) #Рисуем круг - (радиус)
turtle.circle(50,90) # Рисуем круг(радиус круга, длинна окружности которую рисуем в градусах)
"""
def create_circle(color,size,circumference):
    turtle.begin_fill()
    turtle.color('black',color)
    turtle.circle(size)
    turtle.end_fill()
    turtle.circle(size,circumference)

def create_lines():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)






create_circle('red',60,90)
create_lines()

create_circle('blue',40,180)
create_lines()

create_circle('orange',50,180)
create_lines()

create_circle('grey',40,180)
create_lines()

turtle.mainloop()