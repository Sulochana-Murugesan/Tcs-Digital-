def encrypt(k=input()):
    s=[]
    s.append(ord(k[0]))
    for i in range(1,len(k)):
        current=ord(k[i])
        previous=ord(k[i-1])
        s.append((current-previous))
    return s

print(encrypt())

def decrypt(k=list(map(int,input().split()))):
    s=[]
    v=[]
    s.append(chr(k[0]))
    v.append(k[0])
    for i in range(1,len(k)):
        next=k[i]+abs(v[i-1])
        v.append(next)
        s.append(chr(next))
    v=""
    for i in s:
        v+=str(i)
    return v

print(decrypt())


