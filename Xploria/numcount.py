n=input()
k=n
value=1000

def splitadd(n):
    k=[]
    for i in n:
        k.append(int(i))
    su=sum(k)
    return str(su)

def splitmul(n):
    k=[]
    s=1
    for i in n:
       k.append(int(i))
    for i in k:
        s*=i
    return str(s)

count=0

while len(n)>1:
    n=splitadd(n)
    count+=1

counter=0
while len(k)>1:
    k=splitmul(k)
    counter+=1



print("add",count)
print("mul",counter)