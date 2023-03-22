n=int(input())
k=list(map(int,input().split()))
target=int(input())
count=0
for i in range(n):
    for j in range(i+1,n):
        if k[i]+k[j]==target:
            print("("+str(i)+","+str(j)+")")
            count+=1

if count==0:
    print("None")   

