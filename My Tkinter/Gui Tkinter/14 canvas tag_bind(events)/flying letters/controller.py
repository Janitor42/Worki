import model


# добавить новую фигуру в модель
def add_letter(even):
    model.add_letters()
    print(1)


def events(can):
    can.bind('<ButtonPress-1>', add_letter)

