import math
import csv

with open("D:/Daksh/WhiteHatJr/C98/C105/hi.csv") as f:
    
    reader=csv.reader(f)
    filedata=list(reader)
    data=filedata[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+int(x)
        mean=total/n
        return mean
squrelist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squrelist.append(a)
sum=0
for i in squrelist:
    sum=sum+i    
result=sum/(len(data)-1)
std=math.sqrt(result)
print(std)






