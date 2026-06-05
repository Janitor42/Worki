import turtle as t
#region
t.speed(0)
t.pensize(2)

def speral():
    t.pendown()
    t.forward(50)
    t.circle(200,45)
    t.circle(170,50)
    t.circle(75,50)
    t.circle(75,50)
    t.circle(75,50)

    t.circle(45,50)
    t.circle(45,50)
    t.circle(45,50)
    t.circle(45,50)
    t.circle(30,50)
    t.circle(45,50)
    t.circle(35,50)
    t.circle(35,50)
    t.circle(35,50)
    t.circle(35,50)
    t.penup()
for i in range(8):
    speral()
    t.goto(0,0)
    t.left(20)

t.mainloop()
#endregion
