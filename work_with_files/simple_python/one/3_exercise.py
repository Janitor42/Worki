#
#
# def longest_word_in_file() -> str:
#     pass


from string import punctuation

name='files/from_exercise_3.txt'

def longest_word_in_file(file):
    file = open(file, 'r', encoding='utf-8')
    all_w = []

    for i in file:
        w = i.split()
        all_w += w

    count = 0
    for word in all_w:
        w = word
        for punct in punctuation:
            if punct in w:
                w = w.replace(punct, '')
        all_w[count] = w
        count += 1

    count = 0
    word = ''
    for i in all_w:
        if len(i) > count and i.isalpha():
            word = i
            count = len(i)
    return word


print(longest_word_in_file(file=name))