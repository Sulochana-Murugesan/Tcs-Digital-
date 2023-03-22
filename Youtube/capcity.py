p=list(map(int,input().split()))
nlist=list(map(int,input().split()))
mlist=list(map(int,input().split()))

for i in range(p[0]):
    nlist[i]=nlist[i]-p[2]
for i in range(p[1]):
    mlist[i]=mlist[i]-p[2]

final=sum(mlist)-(sum(nlist))

if final==0:
    print("BALANCED")
else:
    print(final-p[2])
    