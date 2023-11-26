import turtle

def create_line(how_many_lines):
    for i in range(how_many_lines):
        line=360/how_many_lines
        turtle.left(line)
        turtle.forward(100)
        turtle.forward(-100)



def create_small_effects(how_many_lines):

    line = 360 / how_many_lines

    for i in range(how_many_lines):
        turtle.left(line)
        size_small_lines = 20
        for i in range(5):
            turtle.left(30)
            turtle.forward(size_small_lines)
            turtle.forward(-size_small_lines)
            turtle.left(-60)
            turtle.forward(size_small_lines)
            turtle.forward(-size_small_lines)
            turtle.left(30)
            turtle.forward(20)
            size_small_lines=size_small_lines*1.2
        turtle.forward(-100)






create_small_effects(5)





turtle.mainloop()