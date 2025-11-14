file = open('files/numbers2.txt','r')
data=[]
for i in file:
    data.append(int(i))
file.close()
file = open('files/numbers3.txt','w')
for i in data:
    len_i=len(str(i))
    file.write(f'{i} - {len_i}\n')