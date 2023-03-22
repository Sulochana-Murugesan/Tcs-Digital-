from itertools import permutations
from itertools import combinations

a=list(map(int,input().split()))
lower=a[0]
upper=a[1]
kes=[]
for i in range(lower,upper+1):
    kes.append(i)
k=int(input())

def per(kes,perval):
    count=0
    kt=permutations(kes,perval)
    for i in kt:
        if sum(i)%2==0:
            count+=1
    return count

def com(kes,perval):
    count=0
    kt=combinations(kes,perval)
    for i in kt:
        if sum(i)%2==0:   
            count+=1
    return count

p=per(kes,k)
c=com(kes,k)
print(p)
print(c)
print(p+c)


#The formula for permutations is: nPr = n!/(n-r)!
#The formula for combinations is: nCr = n!/[r! (n-r)!]