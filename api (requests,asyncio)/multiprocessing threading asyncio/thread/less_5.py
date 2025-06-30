import threading
import time

#  RLock (Рекурсивная блокировка)
# Тот же Lock, но один поток может захватывать его несколько раз.
# Полезно, если функция вызывает другую функцию, которая тоже требует блокировки.
#
# Пример:



# rlock = threading.RLock()
# #rlock = threading.Lock()#пример как все можно сломать!!!!
#
#
# def func1():
#     with rlock:
#         print("Захвачено в func1")
#         func2()  # Не приведёт к deadlock!
#
# def func2():
#     with rlock:
#         print("Захвачено в func2")
#
# func1()
#
# # Если бы был обычный Lock, поток заблокировал бы сам себя (deadlock).






# 3. Semaphore (Семафор)
# Ограничивает количество потоков, которые могут одновременно работать с ресурсом.
#
# Пример (ограничение до 3 потоков):




# sem = threading.Semaphore(3)
#
# def worker(id):
#     with sem:
#         print(f"Поток {id} начал работу")
#         time.sleep(2)
#         print(f"Поток {id} завершил работу")
#
# for i in range(10):
#     threading.Thread(target=worker, args=(i,)).start()

#args=(i,) — это аргумент, который передаётся в функцию worker при создании потока. Давайте разберём подробно:
# Что такое args в threading.Thread?
# args — это параметр конструктора Thread,
# который принимает кортеж аргументов для передачи в целевую функцию (в вашем случае — worker).


# Вывод:
# Сначала запустятся 3 потока, остальные будут ждать освобождения семафора.




#  Event (Событие)
# Механизм для ожидания сигнала между потоками.
#
# Методы:
# .set() — устанавливает флаг в True.
# .clear() — сбрасывает флаг в False.
# .wait(timeout=None) — Блокирует поток, пока флаг не станет True. Возвращает True, если событие произошло, и False, если истек таймаут.
# .is_set()	Проверяет текущее состояние флага (True/False).

# event = threading.Event()
#
# def waiter():
#     print("Ожидаем событие...")
#     event.wait()  # Блокируется, пока event не будет set()
#     print("Событие произошло!")
#
# def setter():
#     time.sleep(2)
#     print("Устанавливаем событие")
#     event.set()  # Разблокирует waiter()
#
# threading.Thread(target=waiter).start()
# threading.Thread(target=setter).start()





# Condition (Условная переменная)
# Позволяет потокам ждать определённого условия.
# Методы:
# wait() — освобождает блокировку и ждёт notify().
# notify(n=1) — пробуждает n потоков.
# notify_all() — пробуждает все ждущие потоки.
# Пример (производитель-потребитель):






# condition = threading.Condition()
# buffer = []
# MAX_ITEMS = 5

# def producer():
#     for i in range(10):
#         with condition:
#             while len(buffer) >= MAX_ITEMS:
#                 condition.wait()  # Ждём, пока потребитель не освободит место
#             buffer.append(i)
#             print(f"Произведено: {i}")
#             condition.notify()  # Уведомляем потребителя
#
# def consumer():
#     for _ in range(10):
#         with condition:
#             while not buffer:
#                 condition.wait()  # Ждём, пока производитель не добавит данные
#             item = buffer.pop(0)
#             print(f"Потреблено: {item}")
#             condition.notify()  # Уведомляем производителя
#
# threading.Thread(target=producer).start()
# threading.Thread(target=consumer).start()


# Вывод:
# Производитель добавляет элементы, а потребитель забирает их, синхронизируясь через Condition.