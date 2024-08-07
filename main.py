a = "McCain 10 McCain 5 Obama 9 Obama 8 McCain 1"
a = a.split(" ")
b = {"McCain": 0, "Obama": 0}

for i in range(len(a)):
    if a[i].isalpha():
        b[a[i]]=b[a[i]]+int(a[i+1])


print(b)