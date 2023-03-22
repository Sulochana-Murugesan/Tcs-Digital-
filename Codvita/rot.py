from itertools import combinations,permutations
n,r=int(input()),int(input())
k=''
for i in range(1,r+1):
    s=str(i)
    k+=s
print(k)
lenth=len(k)
perm=permutations(k,lenth)
count=0
for i in perm:
    print(i)
    count+=1
print(count)

