import time

start=time.time()
start=int(start)
times=0
while True:

    finish=time.time()

    if int(finish)>=int(start):
        start=time.time()
        start=int(start)+1
        print(times)
        times = times + 1




# start=time.time()
#
# b=0
#
# while True:
#     finish=time.time()
#     if int(finish)>=int(start):
#         a=int(finish)-int(start)
#
#     if a==b:
#         print(b)
#         b=b+1



