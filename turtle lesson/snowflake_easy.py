import turtle

turtle.speed(1)


def create_line(how_many_lines):
    for i in range(how_many_lines):
        line = 360 / how_many_lines
        turtle.left(line)
        turtle.forward(100)
        turtle.forward(-100)


create_line(how_many_lines=20)

turtle.mainloop()
