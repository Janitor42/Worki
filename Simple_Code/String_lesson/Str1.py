def new_word(word):
    a=0
    for i in word:
        a+=1
    return word[1:a]
print(new_word('bank'))


def is_safe_bridge(s):
    for i in s:
        if i ==' ':
            return False
    return True

print(is_safe_bridge('####### ##########'))


# Напишите функцию, которая принимает строку и возвращает крайнюю левую цифру в ней.
def left_digit(string):
    for i in string:
        if i.isdigit():
            print(string.find(i))
            break
left_digit('asdasdasdas1')

# В строку были добавлены лишние пробелы, напишите функцию, которая вернет ту же строку,
# но уже без лишних пробелов. В начале и конце строки не должно быть пробелов,
# а между словами может быть не более одного пробела.

def correct_spacing(sentence):
    new=' '.join(sentence.split())
    sentence.split()
correct_spacing("   Всем    привет Red!     ")
