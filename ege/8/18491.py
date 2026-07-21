# Ольга составляет 5-буквенные коды из букв О, Л, Ь, Г, А.
# Каждую букву нужно использовать ровно 1 раз, при этом Ь нельзя ставить первым и нельзя ставить после гласной.
# Сколько различных кодов может составить Ольга?

#ответ 48
from itertools import permutations
word=list('ольга')

count=0
for x in permutations(word):
    str_word=''.join(x)
    if 'ь' == str_word[0]:
        continue
    if 'оь'in str_word or 'аь'in str_word:
        continue
    count+=1
print(count)