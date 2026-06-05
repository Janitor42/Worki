import turtle as t

#region
t.speed(0)
t.pensize(3)
t.Turtle

def figure():
    t.right(30)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(90 + 30)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(90)


for i in range(10):
    figure()
    t.left(96)


t.mainloop()

#endregion























