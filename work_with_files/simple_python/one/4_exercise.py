file = open('files/numbers.txt','r')


two=0
three=0

for row in file:
    if len(row)-1==2:
        two+=int(row)
    if len(row)-1==3:
        three+=1

print(three,two)