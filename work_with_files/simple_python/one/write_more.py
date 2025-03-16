import random

file = open('files/write_more', 'w')

all = []
for i in range(10_000):
    a = random.randint(-1000, 1000)
    all.append(a)
    file.write(f'{str(i)}\n')

file.close()
file = open('files/write_more', 'w')

for i in all:
    if i > 0:
        file.write(f'{str(i)}, add\n')
    else:
        file.write(f'{str(i)}, spend\n')
