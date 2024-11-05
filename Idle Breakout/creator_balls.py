import screen_wrap
import blocks
from wrap import sprite as sp
import random as rd
import frame_statistics
import ball
import red_ball
import purple_ball
import green_ball
import blue_ball

new_ball = []


def create_new_record(color, id):
    dici = {'color': color, 'id': id}
    new_ball.append(dici)


def add_new_balls():
    for i in new_ball:
        if i['id'] not in ball.Ball.all_id:
            choice_ball(color=i['color'],id=i['id'])
            new_ball.remove(i)


def choice_ball(color,id):
    if color in 'yellow':
        ball.Ball(id=id)
    if color in 'red':
        red_ball.Red_ball(id=id)
    if color in 'purple':
        purple_ball.Purple_ball(id=id)
    if color in 'green':
        green_ball.Green_ball(id=id)
    if color in 'blue':
        blue_ball.Blue_ball(id=id)
