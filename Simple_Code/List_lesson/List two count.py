import random
a=[]
for i in range(20):
    a.append(random.randint(-500,500))
print(a)
q=-1
for i in a:
    if i>0 and a[q]>0 or i<0 and a[q]<0:
        print(a[q],i)
        break
    q+=1

