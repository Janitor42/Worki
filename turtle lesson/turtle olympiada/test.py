import turtle as t

t.speed(6)
t.pensize(2)

def rectangle_spiral():
    sizes = [80*2, 70*2, 60*2, 50*2, 40*2, 30*2, 20*2]
    t.pendown()
    for s in sizes:
        for _ in range(4):
            t.forward(s)
            t.left(90)
    t.penup()

for i in range(12):
    rectangle_spiral()
    t.goto(0, 0)
    t.left(30)


t.mainloop()