# Генераторы в Python — это удобный способ создания итераторов,
# которые позволяют вам итерировать элементы без необходимости создания и хранения всех элементов в памяти одновременно.
# Это особенно полезно, когда нужно работать с большими объемами данных.
# Давайте разберём основные концепции и примеры использования генераторов.
#
# Что такое генераторы?
# Генераторы — это функции,
# которые вместо возвращения значения используют ключевое слово yield.
# Когда функция вызывает yield, она "замораживается" и сохраняет своё состояние,
# позволяя продолжить выполнение с того места, где она остановилась, при следующем вызове.



"""№1"""

# Простой пример генератора
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = simple_generator()
# print(next(gen))  # Вывод: 1
# print(next(gen))  # Вывод: 2
# print(next(gen))  # Вывод: 3


#print(next(gen))  # Вывод: StopIterator (генератор изчерпал свое значение)



"""№2"""
#генератор который возвращает простые числа (+1)

# def simple_number_generator():
#     n = 0
#     while True:
#         n += 1
#         yield n
#
# # Использование генератора
# gen = simple_number_generator()
# for _ in range(10):
#     print(next(gen))

# Вывод: 1 2 3 4 5 6 7 8 9 10

'''№3'''
#генератор можно создать с помощью выражений генераторов(более краткий способ)


# squares = (x*x for x in range(10))
# for square in squares:
#     print(square)

# Вывод: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81


#важно -

#Генераторы "ленивые", что означает, что они вычисляют свои значения по мере необходимости,
# и после того, как генератор исчерпан, вы не можете заново получить доступ к его элементам.
# Если вам нужно "перезапустить" генератор, вам нужно будет создать новый экземпляр генератора.

#next()-получить следующий элемент генератора(если исчерпан - StopIteration)
# def gener():
#     a=0
#     while True:
#         a+=1
#         yield a
# gen=gener()
# print(next(gen))

#iter()-возвращает сам генератор (??)
    #не смог найти нормального обьяснения

#list()- преобразует генератор в список, итерация всех элементов генератора
# def gener():
#     n = 0
#     while n!=5:
#         n+=1
#         yield n
# gen = gener()
# lst = list(gen)  # lst теперь [0, 1, 2, 3, 4,5]
# print(lst)
# print(type(lst[3]),type(lst))

#sum(), min(), max() и другие встроенные функции агрегации:
def gener():
    n = 0
    while n!=5:
        n+=1
        yield n
gen = gener()
print(sum(gen))#генератор как аргумент, выводит всю сумму, перебрав при этом весь генератор



