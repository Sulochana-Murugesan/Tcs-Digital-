p1=int(input())
p2=int(input())
p3=int(input())
q=int(input())
al=int(input())
r=int(input())
p1-=q
p2-=q
p3-=q

k=((al-r)+(2*q)-(p1+p2+p3+(3*q)))
print(p1+(k/3)+q+p3)
print(k)