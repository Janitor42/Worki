



file=open('files/who_is_this.txt','a+',encoding='utf-8')
file.seek(0)
print(file.read())
file.close()

file=open('files/who_is_this.txt','a',encoding='utf-8')
name=input('who_is_this')
file.write(f'  {name}')
file.close()