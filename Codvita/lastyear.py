k=input()
t=len(k)
s=[]
if t>1:
    for i in range(len(k)):
        s.append(int(k[i]))        
if t>2:
    for i in range(len(k)-1):
        o=k[i]+k[i+1]
        s.append(int(o))
if t>3:
    for i in range(len(k)-2):
        o=k[i]+k[i+1]+k[i+2]
        s.append(int(o))
if t>4:
    for i in range(len(k)-3):
        o=k[i]+k[i+1]+k[i+2]+k[i+3]
        s.append(int(o))
s.append(int(k))
print(sum(s))

def res(value):
    s=[]
    for i in range(len(value)):
        for j in range(i+1,len(value)+1):
            s.append(int(value[i:j]))
    print(sum(s))
    
res(k)

