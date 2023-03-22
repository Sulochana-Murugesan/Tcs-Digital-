n=input()
vov=['a','e','i','o','u']
final=[]
for i in range(len(n)-1):
    current=n[i]
    next=n[i+1]
    if current in vov:
        if next in vov:
            final.append(current)
            final.append(next)
        elif next not in vov:
            continue
    else:
        final.append(current)

if n[-1] not in  vov:
    final.append(n[-1])
    
    
for i in final:
    print(i,end="")