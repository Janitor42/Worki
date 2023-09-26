import os
import time

import pygame
field=[]
size_x=10
size_y=20

def create_field():
    field.clear()
    for i in range(size_x*size_y):
        field.append(False)

def get_index(x,y):
    return (y-1)*size_x+x-1

def is_busy(x,y):
    return field[get_index(x,y)]

def set_busy(x,y):
    field[get_index(x,y)]=True

def set_free(x,y):
    field[get_index(x,y)]=False

def drow_field():
    field_x=200
    field_y=400
    start_x=0
    start_y=0
    one_x=field_x/size_x
    one_y=field_y/size_y
    screen.fill([0,0,0])
    for y in range(1, size_y + 1):
        for x in range(1, size_x + 1):
            rect = [start_x + (x - 1) * one_x, start_y + (y - 1) * one_y, one_x, one_y]

            if field[get_index(x, y)]:

                pygame.draw.rect(screen, [250, 0, 0], rect)
            else:

                pygame.draw.rect(screen, [150, 150, 150], rect, 1)






screen=pygame.display.set_mode([500,500])

create_field()
set_busy(10,6)

while True:
    pygame.event.get()
    drow_field()
    pygame.display.flip()
    time.sleep(1/60)


