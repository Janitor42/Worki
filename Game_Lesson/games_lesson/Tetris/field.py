import random
import time
import wrap
from wrap import sprite, sprite_text, world
import object

Remove=False
class Field():
    def __init__(self):
        self.fields = []
        self.work_fields = []
        self.work_fields_new=[]

        y_y = 590
        x_x = 20
        numbers = 1
        height=1
        for y in range(21):
            for x in range(11):
                if x != 11:
                    dici = {'x':x_x,'y':y_y, 'state': False, 'number': numbers,'height':height}
                    x_x += 30
                    self.fields.append(dici)
                numbers += 1
                x += 200
            y_y -= 30
            x_x = 20
            height+=1
        print(self.fields)



    def Add_field(self, names):
        if object.check:
            for name in names:
                for dot in self.fields:
                    if sprite.is_collide_point(name,dot['x'],dot['y']):
                        dot['state']=True



    def Remove_and_add_work_field(self):
        global Remove

        for i in self.fields:
            if i['state'] == True:
                name = sprite.add('pacman', i['x'], i['y'])
                sprite.set_size(name, 28, 28)
                listik=[i['x'],i['y']]
                dici = { 'name': name,'height':i['height'],"pos":listik}
                self.work_fields.append(dici)
                i['state']=False

        len_row = 0
        for value in range(1,21):
            for name in self.work_fields:
                if name['height']==value:
                    len_row+=1
                    if len_row==10:
                        remove_row(self.work_fields,value,self.work_fields_new)
                        move_row(self.work_fields,value)
            len_row=0


def remove_row(work_field,value,work_field_new):

    for i in work_field:
        if i['height']==value:
            sprite.hide(i['name'])

    work_field_new.clear()
    for i in work_field:
        if i['height'] != value:
            work_field_new.append(i)
    work_field.clear()
    work_field+=work_field_new




def move_row(work_field,value):
    for i in work_field:
        if i['height']>value:
            sprite.move(i['name'],0,30)
            i['height']=i['height']-1








