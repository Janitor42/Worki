import json
#1
# json_data = '{"name": "John", "age": 30}'
# json1=json.loads(json_data)#для строки
# print(json1)
#
# file=open('files/from_json_load.json', 'r')
# json2=json.load(file)#для загрузки файла
# print(json2)

#2
file=open('files/from_json_create.json','w+')
data = {"имя": "Bob", "age": 30}
json1=json.dump(data,file,indent=2)#хранение файла


# data = {"name": "Tom", "age": 22}
# print(data)
# json_string = json.dumps(data,indent=4)#приведение к json
# print(data)


