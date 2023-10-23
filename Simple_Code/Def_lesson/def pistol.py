# def shoot(q):
#     if q=='F':
#         print('П ы щ ь ')
#         print('нужна перезарядка')
#     else:
#         print('нужна перезарядка')
#
# def reload():
#     q = input('Перезарядка на F'+'\n')
#     return q
#
# while True:
#     shoot(reload())


reload = True


def shoot(q):
    global reload
    if q == '1' and reload == True:
        print('П ы щ ь ')
        reload = False
    else:
        print('нужна перезарядка')


def reloading(q):
    global reload
    if q == '2' and reload == False:
        reload = True
        print('weapon is reloading')
    else:
        print('dont reloading, wrong')



while True:
    shoot(input('стрелять на 1 '))
    reloading(input('перезарядка на 2 '))
