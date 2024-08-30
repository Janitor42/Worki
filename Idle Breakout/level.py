import blocks

level = 0
protection = 1
create_level = False


def create_next():
    if level % 2 == 0:
        make_level_1()
    else:
        make_level_2()


def make_level_1():
    x_1 = 200
    y_1 = 20
    x_2 = x_1 + 60
    y_2 = y_1 + 25
    for i in range(68):  # 92
        y_1 += 2
        y_2 += 2
        blocks.Block(x_1, y_1, x_2, y_2, protection)
        y_1 += 25
        y_2 += 25
        if i == 16 or i == 33 or i == 50:
            y_1, y_2 = 20, 45
            x_1 += 63
            x_2 += 63


def make_level_2():
    x_1 = 200
    y_1 = 20
    x_2 = x_1 + 60
    y_2 = y_1 + 25
    for i in range(34):  # 92
        y_1 += 2
        y_2 += 2
        blocks.Block(x_1, y_1, x_2, y_2, protection)
        y_1 += 25
        y_2 += 25
        if i == 8 or i == 17 or i == 27:
            y_1, y_2 = 20, 45
            x_1 += 63
            x_2 += 63


def leveling():
    global create_level, level, protection
    if not create_level:
        create_next()
        level += 1
        protection += 1
        create_level = True
    if blocks.Block.all_blocks <= 0:
        create_level = False
