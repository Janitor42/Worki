import json
file=open('files/json_file.txt','w+')

all = {'жизни':3,'speed':10}

all_all=[all,all,all]

json.dump(all_all,file,indent=4)

file.close()

file=open('files/json_file.txt','r')
allll=json.load(file)
print(allll)

#requests