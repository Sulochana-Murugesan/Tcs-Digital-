def save(num,sweet,passe):
    if(sweet+passe-1)%num==0:
        return num
    else:
        return (sweet+passe-1)%num

    
numpri=int(input())
sweets=int(input())
passter=int(input())

print(save(numpri,sweets,passter))

    