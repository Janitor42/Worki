reload = 0
value_reload = 0

prepar = 0

fire = 0
action = None

#Перезарядка
#region
def reloading():
    add_ammunition(check_ammunition())

def check_ammunition():
    global action
    print('В барабане ', value_reload)
    if value_reload > 0:
        action = int(input('Заряжаем (1) или взводим и стреляем? (0)'))
        return action
    if value_reload == 0:
        action = int(input('Барабан пустой, для зарядки нажмите (1) '))

def add_ammunition(check_ammunition):
    global reload, value_reload
    if action == 1 and value_reload < 6:
        reload = int(input('Для зарядки патрона нажмите (1) '))
        if reload == 1:
            value_reload += 1
            print('Теперь в барабане', value_reload)
    elif action != 1:
        return
    elif value_reload == 6:
        print('Больше не помещается ')

#endregion


def preparing():
    global prepar
    if value_reload>0:
        prepar=int(input('для взведения курка (1) если не хотим (0)'))


def shoot():
    global fire
    if prepar==1:
        fire=int(input('Можем стрельнуть (1) или пропустить (0) '))
        return fire

def check_shoot(shoot):
    global value_reload,prepar
    if shoot==1:
        print('-----------------------')
        print('Выстрел по мишени ')
        print('-----------------------')
        value_reload-=1
        prepar=False

def work():
    reloading()
    preparing()
    check_shoot(shoot())

while True:
    work()
