import time
import tkinter as tk

win2 = None
play = None
feed = None
clean = None

button_go = None
main_text = None
state = None
states = ['play', 'feed', 'clean']
state_cat = [False, False, False]

text_cat_before = ['Ты поиграл с котиком', 'Ты покормил котика', 'Ты прибрал за котиком']
text_cat_after = ['Котик больше не хочет играть', 'Котик больше не хочет есть', 'Ты уже все прибрал']


def create_radiobutton():
    global play, feed
    play = tk.Radiobutton(win2, text='play to cat',
                          font=('Arial', 20),
                          width=20,
                          anchor='w',
                          variable=state,
                          value='play'
                          )

    play.pack(pady=[150, 20])

    feed = tk.Radiobutton(win2, text='feed the cat',
                          font=('Arial', 20),
                          width=20,
                          anchor='w',
                          variable=state,
                          value="feed"
                          )
    feed.pack(pady=[20, 20])

    clean = tk.Radiobutton(win2, text='clean up after the cat',
                           font=('Arial', 20),
                           width=20,
                           anchor='w',
                           variable=state,
                           value="clean"
                           )
    clean.pack(pady=[20, 20])

    button_go = tk.Button(win2, text='GO',
                          font=('Times', 20, 'bold'),
                          background='yellow',
                          command=your_choice)
    button_go.pack()


def your_choice():
    global main_text
    for i in range(3):
        if state.get() == states[i] and state_cat[i] == False:
            main_text.set(text_cat_before[i])
            state_cat[i] = True
        elif state.get() == states[i] and state_cat[i] == True:
            main_text.set(text_cat_after[i])
    if False not in state_cat:
        fin(win2)


def create_variables():
    global state, main_text

    state = tk.StringVar()
    state.set('No')

    main_text = tk.StringVar()
    main_text.set('Сейчас котик просто отдыхает')


def create_win2():
    global win2
    win2 = tk.Toplevel()
    win2.geometry('500x500+900+200')
    win2.config(background='black')
    win2.title('select')


def fin(win):
    finish = tk.Label(win, text='Молодец ты все сделал!', font=('Arial', 20))
    finish.pack(pady=10)
