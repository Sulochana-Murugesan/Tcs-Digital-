n=int(input())
v=[]
for i in range(n):
    k=list(map(int,input().split()))
    v.append(k)

for i in range(n):
    for j in range(1,n):
        tem=v[i][j]
        v[i][j]=v[j][i]
        v[j][i]=tem

tem=v[1][2]
v[1][2]=v[2][1]
v[2][1]=tem
print(v)

for i in range(n-2):
        tem=v[i][0]
        v[i][0]=v[i][2]
        v[i][2]=tem


print(v)


                 
