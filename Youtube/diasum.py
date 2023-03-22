k=int(input())
p=[]
for i in range(k):
    n=list(map(int,input().split()))
    p.append(n)

sumleft=0
sumright=0

for i in range(len(p)):
    for j in range(len(p)):
        #this is for left to right diagonal
        if i==j:
            sumleft+=p[i][j]

counter=0       
for i in range(len(n)-1,-1,-1): 
        sumright+=p[counter][i]
        counter+=1
      
print(abs(sumleft-sumright))
        
            