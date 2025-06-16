# import turtle
#
# background="#9EC388"
# crust="#ECA84F"
# sauce="#AD0509"
# cheese="#FBC70F"
# pepperoni=[[-70,105],[-85,175],[-25,50],[-15,100],[-25,150],[-30,205],[15,50],[20,120],[20,200],[60,156],[71,215],[80,90]]
# screen=turtle.Screen()
# screen.bgcolor(background)
# screen.title("my pizza")
# my_turtle=turtle.Turtle()
# my_turtle.pensize(5)
# my_turtle.shape("circle")
# def draw_circle(radius,line_color,fill_color):
#     my_turtle.color(line_color)#draw the circle with the defined line color
#     my_turtle.fillcolor(fill_color)#fill the circle
#     my_turtle.begin_fill()
#     my_turtle.circle(radius)
#     my_turtle.end_fill()
# def move_turtle(x,y):
#     my_turtle.up   #my_turtle.penup()
#     my_turtle.goto(x,y) #move the turtle
#     my_turtle.down   #my_turtle.pendown()
#
# draw_circle(150,crust,crust)  #first circle for the crust which is drawn and filled by the same color
# move_turtle(0,25)
# draw_circle(125, sauce, cheese) #second circle with our sauce color and filled with cheese color
# #draw pepperoni
# for i in pepperoni:
#     my_turtle.penup()
#     move_turtle(i[0],i[1])
#     draw_circle(10,sauce,sauce)
#
# move_turtle(0,150)
# my_turtle.color(background)
#
# for x in range(0,8):
#     my_turtle.pendown()
#     my_turtle.left(45)
#     my_turtle.forward(150)
#     my_turtle.penup()
#     my_turtle.backward(150)
#
# turtle.done()


import turtle

# Цвета
background = "#9EC388"
crust = "#ECA84F"
sauce = "#AD0509"
cheese = "#FBC70F"
pepperoni = [[-70, 105], [-85, 175], [-25, 50], [-15, 100], [-25, 150], [-30, 205], [15, 50], [20, 120], [20, 200],
             [60, 156], [71, 215], [80, 90]]

# Настройки экрана
screen = turtle.Screen()
screen.bgcolor(background)
screen.title("My Pizza")
screen.setup(width=800, height=600)  # Устанавливаем размер экрана
screen.tracer(0)  # Отключаем автоматическое обновление экрана

# Создание черепахи
my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")
my_turtle.speed(0)  # Устанавливаем максимальную скорость черепахи

# Функция для рисования круга
def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

# Функция для перемещения черепахи
def move_turtle(x, y):
    my_turtle.penup()  # Без рисования перемещаем черепаху
    my_turtle.goto(x, y)
    my_turtle.pendown()  # Начинаем рисование

# Функция для рисования пиццы
def draw_pizza():
    # Рисуем корку пиццы
    draw_circle(150, crust, crust)

    # Рисуем соус и сыр
    move_turtle(0, 25)
    draw_circle(125, sauce, cheese)

    # Рисуем пепперони
    for i in pepperoni:
        move_turtle(i[0], i[1])
        draw_circle(10, sauce, sauce)

# Функция для вращения пиццы
def rotate_pizza():
    while True:  # Бесконечный цикл для непрерывного вращения
        my_turtle.clear()  # Очищаем экран
        draw_pizza()  # Рисуем пиццу заново
        my_turtle.right(1)  # Поворачиваем пиццу на 1 градус
        screen.update()  # Обновляем экран

# Рисуем пиццу в центре экрана
move_turtle(0, -150)  # Центрируем пиццу
draw_pizza()

# Запускаем бесконечное вращение пиццы
rotate_pizza()

turtle.done()