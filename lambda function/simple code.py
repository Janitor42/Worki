'''lambda function beginner'''
import turtle
import random
import wrap



#'''1'''
# # #простое использование лямбды функции (без параметром)
# def simple():
#     return 'fight'
# print(simple())
#
# simple2=lambda :'fight2'
# print(simple2())






#'''2'''
# #простое использование лямбды функции (с параметром)
# def simple(x):
#     return x*2
# print(simple(4))
#
#
# simple2=lambda x:x*2
# print(simple2(4))





# '''3'''
# # #простое использование лямбды функции (с параметром, c кон-ции if else)
# def simple(x):
#     if x>0:
#         return '+'
#     else:
#         return '-'
# print(simple(10))
#
# simple2=lambda x:'+' if x>0 else '-'
# print(simple2(4))
#
# '''3.1'''
# #Дополнительный пример (параметр заводим ручками с клавиатуры)
#
# simple2=lambda x=int(input('use your count')):'+' if x>0 else '-'
# print(simple2())
#
# #или так
#
# simple2=lambda x:'+' if x>0 else '-'
# print(simple2(int(input('use your count'))))




'''подписать'''

# height=random.randrange(200,300,10)

# def square(height):
#     turtle.begin_fill()
#     if height>=250:
#         turtle.color('black','green')
#     else:
#         turtle.color('black','red')
#     for i in range(2):
#         turtle.forward(100)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.end_fill()

# square(height)
# turtle.mainloop()


# height=random.randrange(200,300,10)
# square_lam=lambda x: turtle.color('black','green') if x>=250 else turtle.color('black','red')
#
# def square(height):
#     turtle.begin_fill()
#     square_lam(height)
#     for i in range(2):
#         turtle.forward(100)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.end_fill()
#
# square(height)
#
# turtle.mainloop()




import wrap_py
wrap_py.app.start()