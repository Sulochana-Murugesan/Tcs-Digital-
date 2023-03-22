all=[]
for i in range(10):
    k=list(map(int,input().split()))
    all.append(k)

sum=0
for i in range(10):
    for j in range(10):
        if i==j:
            print(i,j)
            sum=sum+all[j][i]
print(sum)

#0 1 2 3 4 5 6 7 8 0
#3 4 5 6 7 8 9 6 4 0
#2 3 4 5 6 7 8 9 3 2
#3 4 5 6 7 4 3 2 1 3
#3 4 5 6 2 4 4 2 4 6
#2 3 4 6 2 4 6 2 3 5
#2 3 5 6 2 4 6 2 3 5
#2 4 6 2 1 4 3 3 5 2
#3 3 5 2 4 6 2 1 4 6

