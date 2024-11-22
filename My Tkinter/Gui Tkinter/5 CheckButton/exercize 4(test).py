import tkinter as tk

win = tk.Tk()

win.geometry('1000x500')
win.config(background='black')

count = 0




def restart_all():
    for i in all_elem:
        i['var'].set('No')
        q=i['name']
        q['state']='normal'
def restart():
    for i in all_elem:
        i['var'].set('No')
    normal()

true=0
def check():
    global true
    true=0
    for i in all_elem:
        if i['count'] == 2 and i['var'].get() == 'Yes' :
            true+=50
        if i['count']==0 and i['var'].get()=='Yes':
            true+=50
    state['text']=f'вы были правы на {true} %'
    if true!=100:
        restart_all()


def target():
    count=0
    for i in all_elem:
        if i['var'].get()=='Yes':
            count+=1
        if count>=2:
            disabled()
        else:
            normal()
def normal():
    for i in all_elem:
        if i['var'].get()=='No':
            q=i['name']
            q['state']='normal'


def disabled():
    for i in all_elem:
        if i['var'].get()=='No':
            q=i['name']
            q['state']='disabled'


variables=[]

for i in range(5):
    variables.append(tk.StringVar())
    variables[-1].set('No')



ocean = tk.Checkbutton(win, text='На Земле существует только один океан — Мировой океан.',
                       font=('Arial', 15),
                       width=60,
                       anchor='w',
                       variable=variables[0],
                       offvalue='No',
                       onvalue='Yes',
                       command=target,
                       state='normal'
                       )

chocolate = tk.Checkbutton(win, text='Шоколад является полезным продуктом для здоровья',
                           font=('Arial', 15),
                           width=60,
                           anchor='w',
                           variable=variables[1],
                           offvalue='No',
                           onvalue='Yes',
                           command=target,
                           state='normal'
                           )

water = tk.Checkbutton(win, text='Вода является основным компонентом человеческого организма.',
                       font=('Arial', 15),
                       width=60,
                       anchor='w',
                       variable=variables[2],
                       offvalue='No',
                       onvalue='Yes',
                       command=target,
                       state='normal'
                       )


atmosphere = tk.Checkbutton(win, text='Атмосфера Земли состоит преимущественно из кислорода.',
                            font=('Arial', 15),
                            width=60,
                            anchor='w',
                            variable=variables[3],
                            offvalue='No',
                            onvalue='Yes',
                            command=target,
                            state='normal'
                            )

freeze = tk.Checkbutton(win, text='нуль — это самая низкая температура, которая может быть достигнута.',
                        font=('Arial', 15),
                        width=60,
                        anchor='w',
                        variable=variables[4],
                        offvalue='No',
                        onvalue='Yes',
                        command=target,
                        state='normal'
                        )


state=tk.Label(win,text=f'вы были правы на {true} %')
state.grid(row=2)


checkbuttons=[ocean,chocolate,water,atmosphere,freeze]



all_elem=[]
for i in range(5):
    my_dici = {'name':checkbuttons[i], 'var':variables[i],'count':i}
    all_elem.append(my_dici)


answer = tk.Button(win, text='Проверить ответы',
                   pady=10, foreground='green',
                   font=('Arial', 15, 'bold'),
                   command=check)

restart = tk.Button(win, text='Перезапуск', command=restart)

ocean.grid(padx=150, pady=[150, 0])
chocolate.grid()
water.grid()
atmosphere.grid()
freeze.grid()

answer.grid(pady=60)
restart.grid(row=0, column=0)

win.mainloop()

# ctrl alt l преображает текст