def pary(a):
    b = []
    counter_par = 0
    for elem in a:
        if elem not in b:
            b.append(elem)
        else:
            for elem2 in b:
                if elem2 == elem:
                    counter_par += 1
            b.append(elem)
    return (counter_par)
print(pary([1, 2, 2, 2, 2]))