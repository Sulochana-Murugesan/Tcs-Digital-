
def co(chare,arr):
    count=0
    for val in arr:
        if val==chare:
            count+=1
    return count

n=input()
k=[]
for i in n:
    k.append(co(i,n))
    
if k[0]==k[1]==k[2]==k[3]:
    print("Returned")
else:
    print('Not Returned')