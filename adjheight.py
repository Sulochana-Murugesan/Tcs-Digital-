lit=list(map(int,input().split()))
count=0
for i in range(1,len(lit)-1):
    next=lit[i+1]
    current=lit[i]
    pre=lit[i-1]
    if  pre>current and current<next:
        count+=1
    else:
        continue
print(count)