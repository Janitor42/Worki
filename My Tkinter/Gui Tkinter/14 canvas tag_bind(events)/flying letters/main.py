import controller,model
import view
import time as ti

controller.events(view.can)


while True:
    # ti.sleep(0.01)  # сюда писать нормальный таймер
    model.move_all()
    view.draw()


