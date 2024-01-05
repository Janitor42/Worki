import random
colors=['red','green','blue']
use_colors=[]

def act():
    rd=random.choice(colors)
    colors.remove(rd)
    use_colors.append(rd)
    print(colors)




while True:
    input()
    act()