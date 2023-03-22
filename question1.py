def target_pairs(arr,val):
    count=0
    for i in range(len(arr)):
        for j in range(i+1):
            if i==j:
                continue
            elif i-j==val or i-j==-val:
                print(i,j)
                count+=1
    return count
s=input()
k,l=s.split()
arr=[]
for i in range(int(k)):
     val=int(input())
     arr.append(val)   
print(target_pairs(arr,int(l)))
