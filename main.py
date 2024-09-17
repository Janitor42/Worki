import time

colors = [0, 0, 0]


def inversion():
    global colors
    if colors[0] < 255:
        colors[0] = colors[0] + 1
    else:
        colors[0] = 0
        if colors[1] < 255:
            colors[1] += 1
        else:
            colors[1] = 0
            if colors[2] < 255:
                colors[2] += 1
            else:
                colors = [0, 0, 0]
                time.sleep(10)


while True:
    inversion()
    # time.sleep(0.000001)
    print(colors)