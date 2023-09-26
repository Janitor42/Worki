import wrap
from wrap import sprite,sprite_text
import random
import Shoot_towers



"""Облака"""

clouds=[]
cloud_x=100
cloud_y=100
def cloud(clouds,cloud_x,cloud_y):
    for i in range(28):
        clouds.append(sprite.add('mario-scenery', cloud_x, cloud_y, 'cloud1',False))
        cloud_y+=83
        if cloud_y>598:
            cloud_y=100
            cloud_x+=100
def add_clouds():
    cloud(clouds,100,100)


"""Создание Башен и их позиции"""
#region
def create_tower(type,place):
    for i in range(5):
        if types[i]==type:
            name = sprite.add(folder[i], x[i], 750, name_costume[i])
            towers_d = {'Hand':True,'Type': types[i], 'Name': name, 'Xp': xp[i] ,'PriceXp' : 200,
                        'Speed': speed[i],'PriceSpeed' : 200, 'Power': power[i],'PricePower' : 200,
                        'Time_for_shoot': time_for_shoot[i], 'Time_shoot': 0, 'Time_start': Shoot_towers.time_start,
                        "Explan":expl[i],'Prices':prices[i]}
            sprite.set_height_proportionally(towers_d['Name'], 40)
            place.append(towers_d)

types=['sun','mushroom','star','plain','head']
folder=['pacman','mario-items','mario-items',"mario-enemies","mario-enemies"]
name_costume=['player3','mushroom_liveup','star','plant_green','beetle_blue_go']
x=[50,100,150,200,250]
xp=[25,50,50,50,50]
speed=[5,5,9,5,5]
power=[100,100,100,100,100]
time_for_shoot=[5,5,9,5,5]
texts_name=['Type','Xp     ','Speed','Power']
prices=[200,250,400,500,500]
expl=['work out points','just shoot','shoot three bullet','None','shoot but not long']


towers_d={}
towers_on_the_game=[]
towers_on_the_shop=[]
towers_on_the_up=[]


#endregion


#region
"""Облака (появление и расчеты)"""
def test_clouds():
    if this_tower['Hand'] is True:
        show(clouds)
    else:
        hide(clouds)
def show(clouds):
    for i in clouds:
        sprite.show(i)
def hide(clouds):
    for i in towers_on_the_game:
        if sprite.is_collide_any_sprite(i['Name'],clouds):
            this_cloud=sprite.is_collide_any_sprite(i['Name'],clouds)
            sprite.hide(this_cloud)
            clouds.remove(this_cloud)
    for i in clouds:
        sprite.hide(i)



"""Башни (создание, расчеты  и ксание)"""
this_tower={'Hand': False,'this_tower': 0, 'x':0,'y':0,'Type':0}
def collide(tower_shop,target):
    global this_tower
    for i in tower_shop:
        if sprite.is_collide_sprite(target,i['Name']) and i in towers_on_the_shop:
            show(clouds)
            this_tower['this_tower']=i['Name']
            this_tower['Type']=i['Type']
            this_tower["Hand"] = not this_tower["Hand"]
            this_tower['Prices']=i['Prices']
            if this_tower['Hand'] is True:
                this_tower['x']=sprite.get_x(i['Name'])
                this_tower['y']=sprite.get_y(i['Name'])
            break

points=1000
def test_pos(clouds):
    if this_tower['this_tower'] !=0:
        global points
        if sprite.is_collide_any_sprite(this_tower['this_tower'],clouds) and points>=this_tower['Prices']:
            points-=this_tower['Prices']
            cloud=sprite.is_collide_any_sprite(this_tower['this_tower'],clouds)
            create_tower(this_tower['Type'],towers_on_the_game)
            sprite.move_to(towers_on_the_game[-1]['Name'],sprite.get_x(cloud),sprite.get_y(cloud))
            sprite.move_to(this_tower['this_tower'],this_tower['x'],this_tower['y'])
        else:
            sprite.move_to(this_tower['this_tower'],this_tower['x'],this_tower['y'])



"""Работа с башнями установленными на игровом поле (прокачка и их выбор)"""
avatar=[]
change_tower=0
a=0

def selections(target):
    global tower_power,change_tower
    for i in towers_on_the_game:
        if sprite.is_collide_sprite(target,i['Name']):
            if len(avatar)>0 :
                sprite.hide(avatar[-1]['Name'])
                avatar.clear()
            change_tower=i['Name']
            create_tower(i['Type'],avatar)
            ava=avatar[-1]
            sprite.move_to(ava['Name'],360,810)
            sprite.set_height_proportionally(ava['Name'],60)
            change_tower=i
            break
        else:
            if len(avatar)>0 :
                sprite.hide(avatar[-1]['Name'])
                avatar.clear()
                change_tower=0

def looks_settings_tower(price_xp,price_speed,price_power,price_name):
    if change_tower!=0:
        sprite_text.set_text(price_name,str(change_tower['Type']))
        if change_tower['Xp']<200:
            sprite_text.set_text(price_xp,str(change_tower['Xp'])+' '+'+(25)'+' '+str(change_tower['PriceXp'])+' '+'coins')
        else:
            sprite_text.set_text(price_xp, str('200 Hp - Max upgrade'))
        if change_tower['Speed']>2 and change_tower['Type']=='star':
            sprite_text.set_text(price_speed,str(change_tower['Speed'])+' '+'-(0.25)'+' '+str(change_tower['PriceSpeed'])+' '+'coins')
        else:
            sprite_text.set_text(price_speed, str('2 Speed - Max upgrade'))
        if change_tower['Speed']>=0.5 and change_tower['Type']!='star':
            sprite_text.set_text(price_speed,str(change_tower['Speed'])+' '+'-(0.25)'+' '+str(change_tower['PriceSpeed'])+' '+'coins')
        elif change_tower['Speed']<0.5 and change_tower['Type']!='star':
            sprite_text.set_text(price_speed, str('0.25 Speed - Max upgrade'))
        if change_tower['Power']<400:
            sprite_text.set_text(price_power, str(change_tower['Power']) + ' ' + '+(25)' + ' ' + str(change_tower['PricePower']) + ' ' + 'coins')
        else:
            sprite_text.set_text(price_power, str('400 Power - Max upgrade'))


    else:
        sprite_text.set_text(price_name, 'None')
        sprite_text.set_text(price_xp, 'None')
        sprite_text.set_text(price_speed, 'None')
        sprite_text.set_text(price_power, 'None')



def buy_upgrade(target,price_xp,button_l,price_speed,price_power,coins):
    global points
    if sprite.is_collide_sprite(target,price_xp) and points > change_tower['PriceXp'] and button_l==False and change_tower['Xp']<200:
        points=points-change_tower['PriceXp']
        change_tower['Xp']=change_tower['Xp']+25
        buy_upgrade_settings_hp(200,400,600,1000)
    elif sprite.is_collide_sprite(target,price_speed) and points > change_tower['PriceSpeed'] and button_l==False and change_tower['Time_for_shoot']>2 and change_tower['Type']=='star':
        points = points - change_tower['PriceSpeed']
        change_tower['Time_for_shoot'] -= 0.25
        change_tower['Speed'] = change_tower['Speed'] - 0.25
        buy_upgrade_settings_speed_star(400, 800, 1200, 1800)
    elif sprite.is_collide_sprite(target,price_speed) and points > change_tower['PriceSpeed'] and button_l==False and change_tower['Time_for_shoot']>=0.5 and change_tower['Type']!='star':
        points=points-change_tower['PriceSpeed']
        change_tower['Time_for_shoot']-=0.25
        change_tower['Speed']=change_tower['Speed']-0.25
        buy_upgrade_settings_speed(300,600,900,1500)
    elif sprite.is_collide_sprite(target,price_power) and points > change_tower['PricePower'] and button_l==False and change_tower['Power']<500:
        points=points-change_tower['PricePower']
        change_tower['Power']=change_tower['Power']+25
        buy_upgrade_settings_power(400,700,1100,2000)
    sprite_text.set_text(coins,'You points '+str(points))


def buy_upgrade_settings_power(a,b,c,d):
    if  change_tower['Power']<200:
        change_tower['PricePower']=a
    elif 300>=change_tower['Power']>=200:
        change_tower['PricePower']=b
    elif 400>=change_tower['Power']>=300:
        change_tower['PricePower']=c
    elif 500>=change_tower['Power']>=400:
        change_tower['PricePower']=d
def buy_upgrade_settings_hp(a,b,c,d):
    if  change_tower['Xp']<50:
        change_tower['PriceXp']=a
    elif 100>=change_tower['Xp']>=50:
        change_tower['PriceXp']=b
    elif 150>=change_tower['Xp']>=100:
        change_tower['PriceXp']=c
    elif 200>=change_tower['Xp']>=150:
        change_tower['PriceXp']=d
def buy_upgrade_settings_speed(a,b,c,d):
    if  change_tower['Speed']>4:
        change_tower['PriceSpeed']=a
    elif 3<=change_tower['Speed']<=4:
        change_tower['PriceSpeed']=b
    elif 2<=change_tower['Speed']<=3:
        change_tower['PriceSpeed']=c
    elif 1<=change_tower['Speed']<=2:
        change_tower['PriceSpeed']=d
def buy_upgrade_settings_speed_star(a,b,c,d):
    if  change_tower['Speed']>8:
        change_tower['PriceSpeed']=a
    elif 8<=change_tower['Speed']<=6:
        change_tower['PriceSpeed']=b
    elif 4<=change_tower['Speed']<=6:
        change_tower['PriceSpeed']=c
    elif 2<=change_tower['Speed']<=4:
        change_tower['PriceSpeed']=d


def backlight_three(target,price,price2,price3):
    backlight(target,price)
    backlight(target, price2)
    backlight(target, price3)
def backlight(target,price):
    if sprite.is_collide_sprite(target,price):
        sprite_text.set_font_bold(price,True)
        sprite_text.set_text_color(price, 150,0,0)
    else:
        sprite_text.set_font_bold(price, False)
        sprite_text.set_text_color(price, 0, 0, 0)


def explan(target,expl_text):
    for i in towers_on_the_shop:
        if sprite.is_collide_sprite(target,i['Name']):
            sprite_text.set_text(expl_text,str(i['Explan']))
            break
        else:
            sprite_text.set_text(expl_text, str('None'))

#endregion
