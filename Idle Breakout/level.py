import blocks
import screen_wrap

level = 0


def make(x, y, rep, count_need, new_y):
    y = y
    x = x
    count = 0
    for i in range(rep):
        count += 1
        blocks.Block(x, y)
        y += 25
        if count == count_need:
            y = new_y
            x += 52
            count = 0


def make_level_1():
    make(x=271, y=12, rep=100, count_need=20, new_y=12)


def make_level_2():
    make(y=150, x=78, rep=45, count_need=9, new_y=150)
    make(y=150, x=463, rep=45, count_need=9, new_y=150)


def make_level_3():
    make(x=26, y=12, rep=20, count_need=20, new_y=0)
    make(x=323, y=12, rep=60, count_need=20, new_y=12)
    make(x=724, y=12, rep=20, count_need=20, new_y=0)


def make_level_4():
    make(x=112, y=100, rep=25, count_need=5, new_y=100)
    make(x=112, y=290, rep=25, count_need=5, new_y=290)

    make(x=427, y=100, rep=25, count_need=5, new_y=100)
    make(x=427, y=290, rep=25, count_need=5, new_y=290)


def make_level_5():
    y = 35
    for i in range(5):
        make(x=120, y=y, rep=10, count_need=2, new_y=y)
        make(x=425, y=y, rep=10, count_need=2, new_y=y)
        y += 100


def check_level():#можно написать проще (потом)

    global level
    if len(blocks.Block.all_blocks) <= 0:
        if level % 10 in [0, 5]:
            make_level_1()
            level += 1
            blocks.Block.protect_power += 1
        elif level % 10 in [1, 6]:
            make_level_2()
            level += 1
            blocks.Block.protect_power += 1
        elif level % 10 in [2, 7]:
            make_level_3()
            level += 1
            blocks.Block.protect_power += 1
        elif level % 10 in [3, 8]:
            make_level_4()
            level += 1
            blocks.Block.protect_power += 1
        elif level % 10 in [4, 9]:
            make_level_5()
            level += 1
            blocks.Block.protect_power += 1
