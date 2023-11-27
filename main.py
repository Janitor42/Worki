a=None
max1=max2=0

while a!=0:
    a = int(input())
    if a > max1:
        max2 = max1
        max1 = a

    else:
        if a < max1 and a!=0:
            max2 = a
            print(max2)



print(max2)