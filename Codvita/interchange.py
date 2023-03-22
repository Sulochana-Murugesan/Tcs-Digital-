from itertools import combinations,permutations
n1=input()
n2=int(input())
k=len(n1)
k=permutations(n1,k)
l=[]
for i in k:
    s=''.join(i)
    l.append(int(s))
sot=sorted(l)

for i in sot:
    if i>n2:
        print(i)
        break
