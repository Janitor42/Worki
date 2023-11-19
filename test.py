# Первый век охватывает от 1-го года до 100-го года включительно , второй век
# - от 101-го года до 200-го года включительно и т. д.
#
# Задача
# Учитывая год, верните столетие, в котором он находится.
#
# Примеры
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

# def century(year):
#
#     b=year%100
#     c=year//100
#     if year<1:
#         return 0
#     if c==0:
#         return 1
#     if b ==0:
#         c=c-1
#     return c+1
#
#
# print(century(0))




# Сможете ли вы найти иголку в стоге сена?
#
# Напишите функцию findNeedle(), которая принимает arrayполный мусор, но содержит один"needle"
#
# После того, как ваша функция найдет иглу, она должна вернуть сообщение (в виде строки), в котором говорится:
#
# "found the needle at position "плюс indexон нашел иголку, так что:
#
# Пример (Ввод -> Выход)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

# def find_needle(haystack):
#     for i in range(len(haystack)):
#         if haystack[i] == 'needle':
#             return ("found the needle at position "+str(i))
#
#
# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))




# Волки были вновь завезены в Великобританию. Вы разводите овец, и теперь вас преследуют волки, которые притворяются овцами. К счастью, вы хорошо их замечаете.
#
# Предупредите овцу перед волком, что ее собираются съесть. Помните, что вы стоите в начале очереди , которая находится в конце массива:
#
# [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    7      6      5      4      3            2      1
# Если волк вам ближе всего, вернитесь "Pls go away and stop eating my sheep".
# В противном случае вернитесь "Oi! Sheep number N! You are about to be eaten by a wolf!"к Nположению овцы в очереди.
#
# Примечание: в массиве всегда будет ровно один волк.
#
# Примеры
# Вход: ["sheep", "sheep", "sheep", "wolf", "sheep"]
# Выход:"Oi! Sheep number 1! You are about to be eaten by a wolf!"
#
# Вход: ["sheep", "sheep", "wolf"]
# Выход:"Pls go away and stop eating my sheep"

# def warn_the_sheep(queue):
#     count=-1
#     if queue[-1]=='wolf':
#         return 'Pls go away and stop eating my sheep'
#     for i in range(len(queue)-1,-1,-1):
#         count=count+1
#         print(queue[i])
#         if queue[i]=='wolf':
#             count=str(count)
#             return 'Oi! Sheep number ' + count+'! You are about to be eaten by a wolf!'
#
#
#
# print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf']))




# Напишите функцию, объединяющую два отсортированных массива в один.
# Массивы содержат только целые числа. Кроме того,
# конечный результат должен быть отсортирован и не иметь дубликатов.
# @test.describe('Example Tests')
# def example_tests():
#     test.assert_equals(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
#     test.assert_equals(merge_arrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8])

# def merge_arrays(first, second):
#     for i in first:
#         second.append(i)
#     q=set(second)
#     q=list(q)
#     q.sort()
#     return q
#
# merge_arrays([1,3,5,6],[2,4,6])


# Задача №3527. Упорядочить три числа
# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a, b, c, затем программа должна менять их значения так,
# чтобы стали выполнены условия a <= b <= c, затем программа выводит тройку a, b, c.
#
# Входные данные
# Вводятся три числа.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примечание
# Дополнительные ограничения: нельзя использовать дополнительные переменные (то есть единственной допустимой операцией присваивания является
# обмен значений двух переменных типа (a, b) = (b, a).
#
# Программа должна содержать ровно один вызов функции печати результата. И не больше 3 if.

# a<=b<=c
#
# a=454656465456456
# b=1
# c=14645
#
# #region
# if c<a:
#     c,a=a,c
# if c<b:
#     c,b=b,c
# if b<a:
#     b,a=a,b
# #endregion
#
#
#
# print('a is:',a, 'b is:',b,'c is:',c)

# Возвращает массив, содержащий числа от 1 до N, где N — значение параметра.
#
# Однако замените определенные значения, если выполнено любое из следующих условий:
#
# Если значение кратно 3: вместо этого используйте значение «Fizz».
# Если значение кратно 5: вместо этого используйте значение «Buzz».
# Если значение кратно 3 и 5: вместо этого используйте значение «FizzBuzz».
# N никогда не будет меньше 1.
#
# Пример вызова метода:
#
# fizzbuzz(3) -->  [1, 2, "Fizz"]


# def fizzbuzz(n):
#     arr=[]
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             arr.append('FizzBuzz')
#         elif i%3==0:
#             arr.append('Fizz')
#         elif i%5==0:
#             arr.append('Buzz')
#         else:
#             arr.append(i)
#     return arr
# print(fizzbuzz(31))

#
# Смешайте два массива вместе, чтобы возвращаемый массив содержал чередующиеся элементы этих двух массивов.
# Оба массива всегда будут иметь одинаковую длину.
#
# например. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']


# def array_mash(a, b):
#     arr=[]
#     for i in range(len(a)-1):
#         arr.append(a[i])
#         arr.append(b[i])
#     return arr


# Дана строка, состоящая из слов, разделенных ровно одним пробелом. Определите, сколько в ней слов. Используйте для решения задачи метод count.
#
# Входные данные
# Вводится строка.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# Hello world
# выходные данные
# 2


# Посчитать количество пробелов
# def world(a):
#     spase=0
#     for i in a:
#         if i==' ':
#            spase+=1
#     return spase
#
# print(world('Hello word anither'))

# Посчитать количество слов
# def world(a):
#     spase=1
#     for i in a:
#         if i==' ':
#            spase+=1
#     return spase
#
# print(world('Hello word'))
# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная
# , то длина первой части должна быть на один символ больше). Переставьте эти две части местами, результат запишите
# в новую строку и выведите на экран.
#
# При решении этой задачи нельзя пользоваться инструкцией if.
#
# Входные данные
# Вводится строка.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# Hi
# выходные данные
# iH
# входные данные
# Hello
# выходные данные
# loHel
# def world(a):
#     q=a[0:len(a)//2+len(a)%2]
#     b=a[len(q):len(a)]
#     return b+q
# print(world('Hello'))

# Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат
# запишите в строку и выведите получившуюся строку.
#
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.
#
# Входные данные
# Вводится строка.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# Hello, world!
# выходные данные
# world! Hello,

# def world(a):
#     spase=a.find(' ')
#     q=a[spase+1:len(a)]+' '
#     b=a[0:spase]
#     return q+b
# print(world('Hello, world!'))



# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается, ничего не выводите.
#
# При решении этой задачи нельзя использовать метод count и циклы.
#
# Входные данные
# Вводится строка.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# comfort
# выходные данные
# 3
# входные данные
# office
# выходные данные
# 1 2

# def world(a):
#     q=a.find('f')
#     b=a.rfind('f')
#     return str(q)+' '+str(b)
# print(world('office'))


# Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
#
# При решении этой задачи нельзя использовать метод count.
#
# Входные данные
# Вводится строка.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# comfort
# выходные данные
# -1
# входные данные
# coffee
# выходные данные
# 3

# def world(a):
#     count=-2
#     if a.find('f')!=-1:
#         count+=1
#         where=a.find('f')
#         if a.find('f')!=-1:
#             count=where-1+a.find('f')
#     return count
# print(world('coffee'))