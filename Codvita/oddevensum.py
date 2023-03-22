n=int(input())
k=list(map(int,input().split()))
odd=0
eve=0
for i in range(len(k)):
    if i%2==0:
        eve+=k[i]
    else:
        odd+=k[i]

print(abs(odd-eve))