n=int(input())
k=list(map(int,input().split()))
pos=int(input())

sum=0
for i in range(pos-1,len(k)-1):
        current=k[i]
        next=k[i+1]
        dif=abs(current-next)
        sum+=dif

print(sum)        
