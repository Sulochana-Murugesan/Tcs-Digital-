n=int(input())
k=list(map(int,input().split()))
ne=[]
result=[]
ne.append(k[0])
result.append(0)
for i in range(1,len(k)):
    ma=max(ne)
    if ma<k[i]:
        result.append(0)
    else:
        result.append(k[i])
print(result)

