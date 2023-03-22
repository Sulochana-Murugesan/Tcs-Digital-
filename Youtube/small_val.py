n=int(input())
k=len(str(n))
v=[]
if k==2:
    for i in range(9):
        for j in range(9):
            if i*j==n:
                l=(str(i)+str(j))
                v.append(l)
                break

if k==3:
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if i*j*k==n:
                    l=(str(i)+str(j)+str(k))
                    v.append(l)
                    break
                
if k==4:
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    if i*j*k*l==n:
                        l=(str(i)+str(j)+str(k)+str(l))
                        v.append(l)
                        break

if k==5:
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for l in range(9):
                    for m in range(9):
                        if i*j*k*l*m==n:
                            l=(str(i)+str(j)+str(k)+str(l)+str(m))
                            v.append(l)
                            break

print(v[0])



        
    
        
                

