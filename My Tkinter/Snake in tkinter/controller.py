import model


def events():
    model.screen.bind('<Right>', model.go_right)
    model.screen.bind('<Left>', model.go_left)
    model.screen.bind("<Up>", model.go_up)
    model.screen.bind("<Down>", model.go_down)


