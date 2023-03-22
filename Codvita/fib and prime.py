k=int(input())

def prime(k):
    lit=[2]
    for i in range(3,k):
        prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
               prime=False
               break 
        if prime:
            lit.append(i)
    return (lit)

def fibo(n):
    ket=[1,1]
    for i in range(2,n):
        ket.append(ket[i-1]+ket[i-2])
    return (ket)
        


prim=prime(k+10)
fib=fibo(k+10)
lif=[]
primct=0
fibct=0
for i in range(k):
    if i%2!=0:
        lif.append(prim[primct])
        primct+=1
    elif i%2==0:
        lif.append(fib[fibct])
        fibct+=1
print(lif)
print(lif[-1])