n=int(input())
v=[]
for i in range(n):
    k=list(map(int,input().split()))
    v.append(k)

sr=0
for i in range(sr+1):
    for j in range(0,n):
        print(v[i][j])
        
sr+=1
encol=n
for i in range(sr,sr+2):
    for j in range(encol,encol+1):
        print(i,j)

    
