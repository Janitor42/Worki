string = '5+10/3*8-18'
all = []
order = []


# region
def kick():
    q = ''
    for i in range(len(string)):

        if string[i] in '+-/*' or i == len(string) - 1:
            all.append(float(q))
            all.append(string[i])
            order.append(string[i])
            q = ''
        else:
            q = q + string[i]


def order_signs():
    place = 0
    for i in range(len(order)):
        if order[i] == '*' or order[i] == '/':
            find = order.pop(i)
            order.insert(place, find)
            place += 1


def mult():
    for i in range(len(all)):
        if all[i] == '*':
            all[i - 1] = all[i - 1] * all[i + 1]
            removes(i)
            break


def div():
    for i in range(len(all)):
        if all[i] == '/':
            all[i - 1] = all[i - 1] / all[i + 1]
            removes(i)
            break


def add():
    for i in range(len(all)):
        if all[i] == '+':
            all[i - 1] = all[i - 1] + all[i + 1]
            removes(i)
            break


def sub():
    for i in range(len(all)):
        if all[i] == '-':
            all[i - 1] = all[i - 1] - all[i + 1]
            removes(i)
            break


def removes(i):
    all.remove(all[i])
    all.remove(all[i])


def operations():
    for i in order:
        if i == '*':
            mult()
        if i == '/':
            div()
        if i == '+':
            add()
        if i == '-':
            sub()


kick()
order_signs()

# endregion
operations()
print(all[0])
