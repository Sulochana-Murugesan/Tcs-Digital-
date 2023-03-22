def Array(n1,n2):
    l=[]
    count=0
    for i in range(n1,n2+1):
        l.append(str(i))
    for i in l:
        if len(i)==len(set(i)):
            count+=1
    return count

n1=int(input())
n2=int(input())
print(Array(n1,n2))