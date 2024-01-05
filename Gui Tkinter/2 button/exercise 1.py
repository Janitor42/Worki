import tkinter as tk
import random

rd_colors=['green','red','blue','yellow']
use_colors=[]



color_now=None
def random_color():
    global color_now
    if len(use_colors)>0:
        color_now=random.choice(use_colors)
        return color_now
    else:
        return 'Мы закончили'

def choice_color():
    rd=random.choice(rd_colors)
    rd_colors.remove(rd)
    use_colors.append(rd)
    return rd


def action_1():
    if bt_1['background']==color_now:
        bt_1['text']='Молодец'
        use_colors.remove(color_now)
        bt_message['text']=f'{random_color()}'
    else:
        bt_1['text']='Неа'

def action_2():
    if bt_2['background']==color_now:
        bt_2['text']='Молодец'
        use_colors.remove(color_now)
        bt_message['text']=f'{random_color()}'
    else:
        bt_2['text']='Неа'

def action_3():
    if bt_3['background']==color_now:
        bt_3['text']='Молодец'
        use_colors.remove(color_now)
        bt_message['text']=f'{random_color()}'
    else:
        bt_3['text']='Неа'

def action_4():
    if bt_4['background']==color_now:
        bt_4['text']='Молодец'
        use_colors.remove(color_now)
        bt_message['text']=f' {random_color()}'
    else:
        bt_4['text']='Неа'

win = tk.Tk()
win.title('four colors')

win.geometry('500x500')
win.config(background='black')

#создание переменной bt1 - вызов класса Button(прописываем текст для кнопки,
# в параметр command - ложем фун-цию которая будет запускаться при нажатии


#four buttons
#region
bt_1=tk.Button(win, text='Button1',
               background=choice_color(),
               command=action_1,
               font=('Times',30,'bold'))
bt_1.pack()
bt_2=tk.Button(win, text='Button2',
               background=choice_color(),
               command=action_2,
               font=('Times',30,'bold'))
bt_2.pack()
bt_3=tk.Button(win, text='Button3',
               background=choice_color(),
               command=action_3,
               font=('Times',30,'bold'))
bt_3.pack()
bt_4=tk.Button(win, text='Button4',
               background=choice_color(),
               command=action_4,
               font=('Times',30,'bold'))
bt_4.pack()
#endregion

bt_message=tk.Button(win,text=f'{random_color()}',
                     font=('Arial',25,'italic'))
bt_message.pack(side='bottom')




win.mainloop()