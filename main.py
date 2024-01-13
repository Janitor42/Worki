s='asfasAAfdsdfFFFss'
s2=s
new=str()
count=-1
l=[]
for i in s:
    if i.isupper():
        new=new+(s2[count+1])
        s=(s.replace(i,''))
    count+=1
s=new+s
print(s)


