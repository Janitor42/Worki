import tkinter as tk
import time

win = tk.Tk()
win.geometry('500x500')
win.config(background='grey')
colors = ["alice blue","AliceBlue","antique white", "AntiqueWhite",
    "AntiqueWhite1","AntiqueWhite2","AntiqueWhite3","AntiqueWhite4",
    "aqua","aquamarine","aquamarine1","aquamarine2",
    "aquamarine3","aquamarine4","azure","azure1",
    "azure2","azure3","azure4","beige",
    "bisque","bisque1","bisque2","bisque3",
    "bisque4","black","blanched almond","BlanchedAlmond",
    "blue","blue violet","blue1","blue2",
    "blue3","blue4","BlueViolet","brown",
    "brown1","brown2","brown3","brown4",]

can = tk.Canvas(background=colors[10],
                height=400,
                width=400,
                borderwidth=0)
can.place(x=50, y=50)

kvd = can.create_rectangle(100, 100, 200, 200)
speedx = 2
speedy = 0

while True:
    can.move(kvd, speedx, speedy)
    x1, y1, x2, y2 = can.coords(kvd)
    print(x2)


    if x2 > 400 :
        speedx = -speedx
        print(x2)
    # if y1 < 0 or y2 > 400:
    #     speedy = -speedy

    time.sleep(0.01)
    win.update()

win.mainloop()