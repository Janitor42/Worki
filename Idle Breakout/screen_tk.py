import tkinter as tk
import frame_statistics
import frame_shop_balls
import frame_main
win = None



def run_tk_gui():
    global win

    win = tk.Tk()
    win.geometry('400x500+190+270')
    win.config()
    frame_statistics.Screen_statistics(win)
    frame_shop_balls.create_shop(win)
    frame_main.create_frame_main(win)


    win.mainloop()
