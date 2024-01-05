import random

b = []
a = 0
while a != 2:
    h = random.randint(1,100)
    b.append(h)
    a += 1
print(b)
j = 0
while j != 2:
    if b[j] % 2 == 0 and b[j] % 12 == 0:
        print(b[j])
    j += 1

import random



# a = ['hello!','water','drinking','sons of the forest','dota 2 button reborn'] # наш список
#
# c = max(a, key=len)
# c2=len(c)
# for i in range(len(a)):
#     b=c2-len(a[i])
#     print("*"*b+str(a[i]))