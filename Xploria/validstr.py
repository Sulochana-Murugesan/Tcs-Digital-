n=input()
d={}

for i in range(len(n)):
    if n[i] not in d:
        d[n[i]]=1
    else:
        d[n[i]]+=1

def para_check(d:dict):
    values=[]
    count=0
    print(d)
    for key,value in d.items():
        values.append(value)

    valid=True
    unique=set(values)
    v=[]
    for i in unique:
        v.append(i)
    
    if len(unique)==1:
        print("1")
        valid=True
    elif len(unique)==2:
        first=v[0]
        next=v[1]  
        f=first-next  
        if f==first:
            print("2")
            valid=True
    elif len(unique)>2:
        print("3")
        valid=False
    return valid
 

print(para_check(d))
#partially completely
#aabbcd
#{'a': 2, 'b': 2, 'c': 1, 'd': 1}
#True

#above is incompleted test case
