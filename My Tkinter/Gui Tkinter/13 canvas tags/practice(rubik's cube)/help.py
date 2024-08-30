def create_field_x(field_x, can):
    x = 150
    y = 150
    for i in range(9):
        square = can.create_rectangle(x, y, x + 66, y + 66, fill='lime', width=3,
                                      outline='black', activefill='pink',
                                      activeoutline='black',tags=['x'])
        x += 66
        if x > 347:
            y += 66
            x = 150
        field_x.append(square)


def create_field_y(field_y, can):
    x_begin = 150
    x = 150
    y = 150
    for i in range(9):
        polygon = (
            (x, y),
            (x + 25, y - 25),
            (x + 91, y - 25),
            (x + 66, y)
        )
        poly=can.create_polygon(*polygon, fill='lime', width=3, outline='black',
                           activefill='pink', activeoutline='black',tags=['y'])
        field_y.append(poly)
        x += 66
        if x > 347:
            y -= 25
            x_begin += 25
            x = x_begin


def create_field_z(field_z, can):
    x = 348
    y = 150
    x_begin = x
    y_begin = y

    for i in range(9):
        polygon = (
            (x, y),
            (x + 25, y - 25),
            (x + 25, y + 40),
            (x, y + 66)
        )
        poly=can.create_polygon(*polygon, fill='lime', width=3, outline='black',
                           activefill='pink', activeoutline='black',tags=['z'])
        field_z.append(poly)
        y += 66
        if i in (2, 5):
            x_begin += 25
            x = x_begin
            y_begin -= 25
            y = y_begin
