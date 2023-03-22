l=[chr(i) for i in range(97,123)]
n=list(map(str,input().lower().split()))
print(n)
d=[]
for i in n:
    for j in i:
        if j not in d:
            d.append(j)
if len(d)==len(l):
     print("Sucessfull completion")  
else:
    print("Not sucessfull")
