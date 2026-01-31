# import time
# import tkinter as tk
#
# win = tk.Tk()
# win.geometry('1200x800+100+200')
# win.config(background='black')
#
# can = tk.Canvas(width=1200, height=800, bg='black')
# can.place(x=0, y=0)
# coordsh = [725, 275, 725, 525]
# coordsh2 = [725, 275, 725, 525]
# base = can.create_oval(600, 400, 850, 650, fill='white')
# hour_hand = can.create_line(*coordsh, fill='black', width=8)
#
# minute_hand = can.create_line(coordsh2,fill='red', width=8)
# # second_hand = can.create_line()
#
# # a = [1, 2, 3, 4]
# # print(a)                - Памятка
# # print(*a)
#
# # while True:
#
# extra = [[16.7, 16.7], [-16.7, 16.7], [-16.7, -16.7], [16.7, -16.7]]
#
#
# def action():
#     for i in extra:
#         piece(x=i[0], y=i[1], hand=hour_hand, wd=8)
#
#
# def piece(x, y, hand, wd):
#     for i in range(15):
#         coordsh2[0], coordsh2[1], coordsh2[2], coordsh2[3] = coordsh2[0] + x, coordsh2[1] + y, coordsh2[2], coordsh2[3]
#         time.sleep(0.1)
#         can.delete(hand)
#         hand = can.create_line(*coordsh2, fill='black', width=wd)
#         if coordsh == coordsh2:
#             print(1)
#
#         win.update()
#     can.delete(hand)
#
#
# action()
# action()
# win.mainloop()

#
# import tkinter as tk
#
#
# def create_scrollable_window():
#     root = tk.Tk()
#     root.title("Окно с прокруткой")
#     root.geometry("400x300")
#
#     # Главный фрейм
#     main_frame = tk.Frame(root)
#     main_frame.pack(fill=tk.BOTH, expand=1)
#
#     # Canvas для прокрутки
#     my_canvas = tk.Canvas(main_frame)
#     my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
#
#     # Scrollbar
#     my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
#     my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#
#     # Настройка canvas
#     my_canvas.configure(yscrollcommand=my_scrollbar.set)
#     my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
#
#     # Фрейм для контента
#     content_frame = tk.Frame(my_canvas)
#     my_canvas.create_window((0, 0), window=content_frame, anchor="nw")
#
#     # Добавляем много элементов
#     for i in range(50):
#         tk.Label(content_frame, text=f"Элемент {i + 1}", font=("Arial", 12)).pack(pady=5)
#
#     return root
#
#
# root = create_scrollable_window()
# root.mainloop()



a=('23','111sfda','egsd')

print(a[2])