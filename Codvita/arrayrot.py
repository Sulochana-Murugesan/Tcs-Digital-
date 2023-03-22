def rotate(array,rot):
    count=0
    for i in range(len(array)-1,-1,-1):
        count+=1
        if count<=rot:
            first=array[i]
    #incompleted

def rep(array,rot):
    count=0
    for i in range(len(array)-1,-1,-1):
        print(i)
        if count<rot:
           
            k=array[i]
            first=array[count]
            array[count]=k
            array[i]=first
            count+=1
    print(array)
    #incompleted

def arr(array,rot):
    k=len(array)
    for i in range(rot):
        array.append(0)
    
    for i in range(k-1,-1,-1):
        array[i+rot]=array[i]

    first=rot-1
    last=len(array)-1
    print(first,last)
    for i in range(rot):
        array[first]=array[last]
        last-=1
        first-=1
    
    for i in range(k):
        print(array[i],end=" ")
    #perfectly completed

#to easly without knowledge
def easy(array,rot):
    print(array[-2:],array[:-2])

k=int(input())
p=[]
for i in range(k):
    s=int(input())
    p.append(s)
rot=int(input())
arr(p,rot)
easy(p,rot)