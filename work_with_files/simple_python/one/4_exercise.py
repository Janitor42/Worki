
import time

a=time.time()
file = open('files/numbers.txt','r')
# В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти
#
# количество трехзначных чисел;
# сумму двухзначных чисел
# В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов.
# Сперва количество, потом сумма

two=0
three=0
a=[]
for row in file:
    if len(row)-1==2:
        two+=int(row)
    if len(row)-1==3:
        three+=1
    q=row.strip()
    a.append(q)
file.close()



#
# file = open('files/numbers.txt','w')
# for i in a:
#     file.write(f'{i} {len(i)}\n')
#

# print(three,two)
# print(time.time()-a)

# 9041 46947