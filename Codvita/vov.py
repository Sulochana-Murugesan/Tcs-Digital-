vov=["a",'e','i','o','u']

s1=input()
s2=input()
s3=input()

def arrs(a):
    k=[]
    for i in a:
        k.append(i)
    return k

k1=arrs(s1)
k2=arrs(s2)
k3=arrs(s3)

tot=[]
for i in range(len(k1)):
    for k in range(len(vov)):
        if k1[i]==vov[k]:
            k1[i]='*'
            break
tot.extend(k1)
             
for i in range(len(k2)):
    for k in range(len(vov)):
        if k2[i]==vov[k]:
            k2[i]='@'
        break

tot.extend(k2)

for i in k3:
    if i in vov:
       k3=s3.upper()

tot.extend(k3)   
for i in tot:
    print(i,end="")

