import string
import random

big=6
small=3
count=3

password=[]
all_simbols=list(string.ascii_letters+string.digits)
password.append(random.choice(all_simbols))

while len(password)!=12:
    choice=random.choice(all_simbols)
    print(big,small,count)
    if password[-1]==choice :
        continue
    if choice in  string.ascii_uppercase and big==0:
        continue
    if choice in string.ascii_lowercase and small == 0:
        continue
    if choice in string.digits and count==0:
        continue

    if choice in  string.ascii_uppercase and big!=0:
        big-=1
        password.append(choice)
        continue
    if choice in  string.ascii_lowercase and small!=0:
        small-=1
        password.append(choice)
        continue
    if choice in  string.digits and count!=0:
        count-=1
        password.append(choice)
        continue

print(password)






