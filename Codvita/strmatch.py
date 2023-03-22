n=int(input())
search=input()
l=[]

def counter(word,array):
    array=array.split()
    count=0
    for i in array:
        if i==word:
            count+=1
    return count

for i in range(n):
    k=input()
    l.append(k)


d={}
for i in l:
    d[counter(search,i)]=i

sot=sorted(d.keys())

for i in sot:
    print(d[i])



            




