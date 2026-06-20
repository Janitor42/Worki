import threading
import time


# для начала поговорим о методах и возможностях

# target,start
# def some():
#     print('hello world')
# thread = threading.Thread(target=some)#создание эк-ла класса в понлях target- вызов фун-ции которая запуститься
# thread.start()# запуск потока (запускаем его в отдельном потоке)


                                # thread.join()
# def some():
#     print('2-ой поток начал работать')
#     time.sleep(2)
#     print('2-ой поток закончил работать')
# thread=threading.Thread(target=some)
# thread.start()
# print('1-ый поток начал работать')
# thread.join() #если нужно подождать что бы поток завершился и только потом переходить к коду дальше
# #используется в безопасности и синхронизации
# #Можно указать таймаут: thread.join(timeout=5) - ждать не более 5 секунд.
# #join() не останавливает поток, он только блокирует вызывающий поток до завершения целевого.
# print('1-ый поток закончил рабоать')

                                # thread.is_alive(),threading.Thread(name="MyThread")

# def some():
#     print(thread.is_alive())# true or false о жизни потока
#     time.sleep(2)
#     print('2-ой поток закончил работать')
#
# thread=threading.Thread(target=some,name='2-ой')#параметр name -можно записать имя потока
# thread.start()
#
# while True:
#     if not thread.is_alive():#как работать в примере
#         print('поток не активен, программа завершена')
#         print(thread.name)#узнаем имя потока,если имя нет то обращаться не к чему
#         break
# в чем отличия от theard.join() thread.is_alive() - не блокирует а просто проверка статуса, полезно если нужно выполнять
# другие задачи вызова в момент ожидания


                                # daemon = True
# import tkinter as tk
# win=tk.Tk()
# win.geometry('500x500')
#
# def some():
#     while True:
#         print(f'{thread2.name} работает')
#         time.sleep(0.5)
#
# thread2=threading.Thread(target=some,daemon=False,name='2-ой')# поток не демон, будет работать после того как мы закроем
# #основное окно tk, то-есть мы закрыли программу по крестику а какие то потоки этой программы продолжают работать
# #если мы переставим на daemon = True  и перезапустим - при остановки главного потока, все демоны остановятся тоже,
# #другими словами закрыв окно мы автоматически выйдем из таких потоков и прекратим их
# #изначально если мы не указываем флаг у потока то там будет лежать daemon = False  и если мы завешим основной поток,
# #все дополнительные потоки продолжат сидеть в системе
# thread2.start()
#
# win.mainloop()

                            # другое

# for thread in threading.enumerate():# Возвращает список всех активных потоков.
#     print(thread.name)

# print(threading.active_count())#Возвращает количество активных потоков.

