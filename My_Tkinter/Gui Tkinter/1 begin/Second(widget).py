import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
win.title('Image Resize Example')
win.geometry('500x500')
win.config(background='black')

# Открываем изображение
pil_img = Image.open("image.png")

# Изменяем размер изображения (например, 200x200)
resized_img = pil_img.resize((200, 200))

# Преобразуем в формат, совместимый с Tkinter
img = ImageTk.PhotoImage(resized_img)

# Создаем и размещаем Label с изображением
label = tk.Label(win, image=img)
label.place(x=100, y=100)

win.mainloop()


