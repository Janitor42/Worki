import wrap
from wrap import sprite
import random
import Towers
import time
import Enemies


"""Создание выстрелов и других похожих обьектов"""
bullet_list=[]
bullet_dict={}
def bullets(tower):
    name=sprite.add('pacman',sprite.get_x(tower['Name']),sprite.get_y(tower['Name']),'player3')
    sprite.set_size(name,15,15)
    bullet_dict={'Type':tower['Type'],'Name':name,'speed':tower['Speed'],'Power':tower['Power'],'Time_shoot':tower['Time_for_shoot']}
    bullet_list.append(bullet_dict)

def bullets_star(tower):
    name = sprite.add('mario-items', sprite.get_x(tower['Name']), sprite.get_y(tower['Name']), 'star')
    sprite.set_size(name, 15, 15)
    bullet_dict = {'Type':tower['Type'],'Name': name, 'speed': tower['Speed'], 'Power': tower['Power'],
                   'Time_shoot': tower['Time_for_shoot']}
    bullet_list.append(bullet_dict)
    if sprite.get_y(tower['Name'])>=183:
        name = sprite.add('mario-items', sprite.get_x(tower['Name']), sprite.get_y(tower['Name'])-83, 'star')
        sprite.set_size(name, 15, 15)
        bullet_dict = {'Type':tower['Type'],'Name': name, 'speed': tower['Speed'], 'Power': tower['Power'],
                       'Time_shoot': tower['Time_for_shoot']}
        bullet_list.append(bullet_dict)
    if sprite.get_y(tower['Name'])<=515:
        name = sprite.add('mario-items', sprite.get_x(tower['Name']), sprite.get_y(tower['Name']) + 83, 'star')
        sprite.set_size(name, 15, 15)
        bullet_dict = {'Type':tower['Type'],'Name': name, 'speed': tower['Speed'], 'Power': tower['Power'],
                       'Time_shoot': tower['Time_for_shoot']}
        bullet_list.append(bullet_dict)

def bullets_head(tower):
    name=sprite.add('mario-enemies',sprite.get_x(tower['Name']),sprite.get_y(tower['Name']),'beetle_blue_go')
    sprite.set_size(name,25,25)
    bullet_dict={'Type':tower['Type'],'Name':name,'speed':tower['Speed'],'Power':tower['Power'],'Time_shoot':tower['Time_for_shoot']}
    bullet_list.append(bullet_dict)
def generate_points(tower,coins):
    Towers.points=Towers.points+tower['Power']
    wrap.sprite_text.set_text(coins,'You points '+str(Towers.points))


time_start=time.time()
time_finish=time.time()
true_time=0
def make_actions(coins):
    global true_time, time_star
    if Towers.towers_on_the_game!=None:
        for i in Towers.towers_on_the_game:
            time_finish = time.time()
            true_time = int(time_finish - i['Time_start'])
            i['Time_shoot']=true_time
            if  i['Time_for_shoot']<=i['Time_shoot']:
                if i['Type']=='sun':
                    generate_points(i,coins)
                elif i['Type']=='star':
                    bullets_star(i)
                elif i['Type']=='head':
                    bullets_head(i)
                else:
                    bullets(i)
                i['Time_start']=time.time()

def move_bullets():
    if bullet_list!=None:
        for i in bullet_list:
            sprite.move(i['Name'],2,0)
            if sprite.get_x(i['Name'])>=900 and i['Type']!='head':
                sprite.hide(i['Name'])
                bullet_list.remove(i)
            if sprite.get_x(i['Name'])>=650 and i['Type']=='head':
                sprite.hide(i['Name'])
                bullet_list.remove(i)


def collisions_enemies(enemies):
    for bullet in bullet_list:
        for enemy in enemies:
            if sprite.is_collide_sprite(bullet['Name'],enemy['Name']):
                sprite.hide(bullet['Name'])
                bullet_list.remove(bullet)
                enemy['HP']-=bullet['Power']/10
                wrap.sprite_text.set_text(enemy['text_name'],str(int(enemy['HP'])))
            if enemy['HP'] <= 0:
                sprite.hide(enemy['Name'])
                sprite.hide(enemy['text_name'])
                enemies.remove(enemy)

                break






# def suns():
#     make_actions(score_add,Towers)