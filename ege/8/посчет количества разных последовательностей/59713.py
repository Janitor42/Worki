# Составляют 5-буквенные слова из букв слова ПЯТНИЦА.
# Найти количество слов, которые не начинаются с Н и в которых есть только одна буква Я.
# Буквы в слове могут повторяться.

# 5616
import itertools

word=list('пятница')
count=0
for i in itertools.product(word,repeat=5):
    str_word=''.join(i)
    if 'н'!=str_word[0] and str_word.count('я')==1:
        count+=1
print(count)