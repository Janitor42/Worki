import time

import wrap
from wrap import sprite as sp
from random import randint as rd
import random
import ball_five
import star_five

win_x = 800
win_y = 800
wrap.add_sprite_dir("C:/Users/i'm/PycharmProjects/Worki/Class wrap/les 5")





class Square:
    place = 1
    def __init__(self, size, x, y, list_square, list_balls,list_stars,time_between):



        if Square.place<5:
            self._define_place()
        else:
            self.x = x
            self.y = y
            self.min_save = 50
            self.max_save = 75
            self.group = 'C'

        self.time_between=time_between
        self.time_begin=time.time()
        self.list_square = list_square
        self.list_balls = list_balls
        self.list_stars=list_stars
        self.size = size

        self.name = sp.add('picture', self.x, self.y, costume='square_five')
        self.name_text = sp.add_text(
            'Для шаров ' + str(self.group)+' '+str(self.min_save)+' '+str(self.max_save),
            self.x, self.y - self.size * 0.6)

        sp.set_width_proportionally(self.name, self.size)
        Square.place += 1




    def _define_place(self):
        if Square.place==1:
            self.x,self.y,self.group=200,200,'A'
            self.min_save=0
            self.max_save=24
        if Square.place==2:
            self.x,self.y,self.group=200,600,'B'
            self.min_save=25
            self.max_save=50
        if Square.place==3:
            self.x,self.y,self.group=600,200,'C'
            self.min_save=51
            self.max_save=75
        if Square.place==4:
            self.x,self.y,self.group=600,600,'D'
            self.min_save=74
            self.max_save=101





    def define_self_balls(self):
        for one_ball in self.list_balls:
            if self.group == one_ball.group and sp.is_collide_sprite(self.name, one_ball.name):

                if one_ball.state == 'open':
                    sp.move_to(one_ball.name, self.x, self.y)
                    sp.move_to(one_ball.name_text, self.x, self.y)
                    sp.move_to(one_ball.name_size, self.x, self.y + 20)
                    sp.move_to(one_ball.name_state, self.x, self.y - 20)
                    one_ball.state = 'loct'
                    wrap.sprite_text.set_text(one_ball.name_state, one_ball.state)

            if one_ball.state == 'loct' and sp.is_collide_sprite(self.name, one_ball.name):
                if sp.get_right(one_ball.name) >= sp.get_right(self.name):
                    one_ball.speed_x = -abs(one_ball.speed_x)
                if sp.get_left(one_ball.name) <= sp.get_left(self.name):
                    one_ball.speed_x = abs(one_ball.speed_x)
                if sp.get_bottom(one_ball.name) >= sp.get_bottom(self.name):
                    one_ball.speed_y = -abs(one_ball.speed_y)
                if sp.get_top(one_ball.name) <= sp.get_top(self.name):
                    one_ball.speed_y = abs(one_ball.speed_y)

            if one_ball.state == 'open':
                if sp.get_left(one_ball.name) <= 0:
                    one_ball.speed_x = abs(one_ball.speed_x)
                if sp.get_right(one_ball.name) >= win_x:
                    one_ball.speed_x = -abs(one_ball.speed_x)
                if sp.get_top(one_ball.name) <= 0:
                    one_ball.speed_y = abs(one_ball.speed_y)
                if sp.get_bottom(one_ball.name) >= win_y:
                    one_ball.speed_y = -abs(one_ball.speed_y)

    def create_self_star(self):
        if int(self.time_begin) + self.time_between <= int(time.time()):
            self.list_stars.append(star_five.Star(rd(sp.get_left(self.name),sp.get_right(self.name)),
                                                  rd(sp.get_top(self.name),sp.get_bottom(self.name)),
                                                  self.rd_randrange(),
                                                  self.rd_not_zero(-10,10),
                                                  self.list_stars))
            self.time_begin=time.time()






    @staticmethod
    def rd_not_zero(min, max):
        return random.choice([i for i in range(min, max + 1) if i != 0])

    @staticmethod
    def rd_randrange():
        return random.randrange(20, 100, 20)
