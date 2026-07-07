import turtle
import turtle as t
#region
t.speed(6)
t.pensize(2)


# def speral():
#     t.pendown()
#     t.forward(50)
#     t.circle(200,45)
#     t.circle(170,50)
#     t.circle(75,50)
#     t.circle(75,50)
#     t.circle(75,50)
#
#     t.circle(45,50)
#     t.circle(45,50)
#     t.circle(45,50)
#     t.circle(45,50)
#     t.circle(30,50)
#     t.circle(45,50)
#     t.circle(35,50)
#     t.circle(35,50)
#     t.circle(35,50)
#     t.circle(35,50)
#     t.penup()
# for i in range(8):
#     speral()
#     t.goto(0,0)
#     t.left(20)

t.penup()
t.goto(200,0)
t.pendown()

size1=100
size2=300
size3=320
for i in range(1):
    turtle.circle(100,180)
    turtle.circle(300,45)
    turtle.circle(-320,50)

    turtle.circle(-100,180)
    turtle.circle(-300,45)
    turtle.circle(320,50)

    size1+=10
    size2+=10
    size3+=10

    t.goto(200,0)
t.mainloop()
#endregion
