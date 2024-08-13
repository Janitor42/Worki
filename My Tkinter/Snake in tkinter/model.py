import tkinter as tk
import view
import controller
import block
import target
import random as rd

import time

speed = 5

up = 0
down = 0
left = 0
right = speed

x = 250
y = 250

screen = tk.Tk()
screen.geometry('600x600')
screen.config(background='black')

snake = []
snake.append(block.Block(screen=screen, x=250, y=250, part='Head'))
for i in range(100):
    snake.append(block.Block(screen=screen,x=0,y=0,part='Body'))
my_target = target.Target(screen)


# region
def calk_move():
    global up, down, left, right, x, y
    x = x + left + right
    y = y + up + down


def go_up(event):
    global up, down, left, right, x, y
    up = -speed
    down, left, right = 0, 0, 0


def go_down(event):
    global up, down, left, right, x, y
    down = abs(speed)
    up, left, right = 0, 0, 0


def go_right(event):
    global up, down, left, right, x, y
    right = abs(speed)
    up, down, left = 0, 0, 0


def go_left(event):
    global up, down, left, right, x, y
    left = -speed
    up, down, right = 0, 0, 0


# endregion

def move_snake():
    calk_move()
    for obj in range(len(snake)):
        if obj == 0:
            snake[obj].move(x=x, y=y)
        else:
            pos = snake[obj - 1].steps[0]
            xx = pos[0]
            yy = pos[1]
            snake[obj].move(x=xx, y=yy)
        if snake[obj].check_collide(my_target=my_target):
            snake.append(block.Block(screen=screen, x=0, y=0, part='Body'))


start = time.time()

# loop
controller.events()
while True:

    finish = time.time()
    # if float(finish) > float(start) + 0.025:
    #     start += 0.025
    move_snake()
    screen.update()
