# По каналу связи передаются сообщения, содержащие только четыре буквы: А, Б, В, Г;
# для передачи используется двоичный код, удовлетворяющий условию Фано.
# Для букв А, Б, В используются такие кодовые слова: А – 0; Б – 110; В – 101.
# Укажите кратчайшее кодовое слово для буквы Г, при котором код будет допускать однозначное декодирование.
# Если таких кодов несколько, укажите код с наибольшим числовым значением.



a = '0'
b = '110'
c = '101'
coding_letters=[a,b,c]
#
# singleton=min(coding_letters,key=len)
# max_l=len(max(coding_letters,key=len))
#
# variants=[]
#
# max_v=max_l*'1'+'1'
#
# for i in range(int(max_v)+1):
#     value=''
#     for q in str(i):
#         if str(q) not in '23456789':
#             value+=str(q)
#         else:
#             break
#     if value!='' and value not in variants:
#         variants.append(value)
#
# print(variants)

m = map(lambda x: int(x, 2) ,coding_letters)
m = (1+len(bin(max(m))[2:]))*"1"
m = int(m, 2)
m = [bin(i)[2:] for i in range(m+1)]
print( m )