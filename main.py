# import asyncio
#
# async def my_coroutine():
#    print("Корутина начала выполнение")
#    await asyncio.sleep(2)  # Асинхронная задержка на 2 секунды
#    print("Корутина завершила выполнение")
#
#
#
# asyncio.run(my_coroutine())
#
# a = 10
# b = "hello"
#
# print(f"world, {a} say\t {b} *")

import string

# a = '123 jhjk bhjip456qwerty 1x2y3 4 5 6 sfsd 0 dfgfd 10abc20de30pop5 5 5 5'
#
# val = ''
# all = []
# count = 0
# for i in a:
#     if i.isdigit():
#         val += i
#         if len(a) == count + 1:
#             all.append(val)
#             break
#     if not i.isdigit():
#         if val != '':
#             all.append(val)
#         val = ''
#     count += 1
#
# print(all)


# class Car:
#     a=0
#     def __init__(self):
#         self.x=10
#         self.y=10
#
# w=Car()
#
# print(w.x)
#
#
#
# w=Car()
#
# print(w.a)
# w.a=10
# print(w.a)
# w.c=10
# print(w.c)


# a=['w','w','w']

# import random
# color = None
# number = None
# size = None
# def random_number():
#     global color,size,number
#     number = random.randint(1,36)
#     if number % 2 == 0:
#         color = "black"
#     else:
#         color = "red"
#     if number <= 18:
#         size = "small"
#     else:
#         size = "big"
#     print(str(number) + color + size)
#     return number,size,color
#
# balance = 100
# want_to_play = input("do you want to play the roulette? ")
# while want_to_play == "yes" and balance > 0:
#     money_spent = int(input("how much money do you want to use? "))
#     if money_spent > balance:
#         print("you dont have enough money")
#         break
#     balance = balance - money_spent
#     type_of_play = input("choose the type of play: ")
#     if type_of_play == "color":
#         color_play = input("choose the color: ")
#         random_number()
#         if color == color_play:
#             score = "win"
#             balance = balance + 2*money_spent
#         else:
#             score = "lose"
#     if type_of_play == "number":
#         number_play = input("choose the number: ")
#         random_number()
#         if number == number_play:
#             score = "win"
#             balance = balance + 6 * money_spent
#         else:
#             score = "lose"
#     if type_of_play == "size":
#         big_small = input("choose big or small: ")
#         if size == big_small:
#             score = "win"
#             balance = balance + 2 * money_spent
#         else:
#             score = "lose"
#     result = "you " + score
#     print(result + " you have " + str(balance) + " left")
#     want_to_play = input("do you want to keep playing the roulette? ")


# a=('no',)
# a2=list(a)
# a3=a[0]
# print(a3)



