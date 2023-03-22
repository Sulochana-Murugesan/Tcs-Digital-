n=int(input())
k=list(map(int,input().split()))
def sam(k):
    s=[]
    p=0
    for i in range(len(k)):
        val=0
        s.append(k[i])
        flag=True
        for j in range(i):
            if j not in s:
                flag=False
                val=k[i]
        if val>p:
            p=val
        
def fine(array):
    l=[]
    ma=0
    for i in range(len(array)):
        count=1
        flag=True
        l.append(array[i])
        for j in range(1,array[i]):
            if j in l:
                count+=1
            else:
                flag=False

        if flag==False:
            max=count
            if max>ma:
                ma=max
    print(ma)



def crt(array):
    cout=1
    for i in range(len(array)-1):
        m=1
        for j in range(i + 1, n):
            if array[i+1]>array[i]:
                m+=1
        cout=max(cout,m)
    print(cout)

crt(k)
        