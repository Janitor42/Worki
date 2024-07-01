import turtle

turtle.speed(1)


def line(angle_begin, line1, angle1, line2, angle2, line3):
    turtle.left(angle_begin)
    turtle.forward(line1)
    turtle.left(angle1)
    turtle.forward(line2)
    turtle.left(angle2)
    turtle.forward(line3)


line(0, 200, 45, 100, -135, 200 / 3)
line(-45, 100, -45, 200, -90, -200 / 3)
line(-90, 200, 45, 100, -135, 200 / 3)
line(-45, 100, -45, 200, -90, 0)
line(0, 200, -45, 100, -45, 200 / 3)
line(-135, 100, 45, 200, -90, -200 / 3)
line(-90, 200, -45, 100, -45, 200 / 3)
line(-135, 100, 45, 200, -90, 0)
line(-135, 100 / 3, 0, 0, 0, 0)
line(45, 200, 90, 200, -135, 100 / 3)
line(-45, 200, -90, 200, 135, 100 / 3)
line(45, 200, 90, 200, -135, 0)
turtle.mainloop()
