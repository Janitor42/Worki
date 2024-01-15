import turtle


def create_line(how_many_lines):
    for i in range(how_many_lines):
        line=360/how_many_lines
        turtle.left(line)
        turtle.forward(100)
        turtle.forward(-100)




create_line(7)

turtle.mainloop()