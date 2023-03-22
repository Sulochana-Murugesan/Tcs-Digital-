n=int(input())
p=int(input())
val=n//p
if p<val:
    if p%2==0:
        print(p-1)
    else:
        print(p-2)
if p>val:
    if n%2==0:
        print((n-p+1)//2)
        print("d")
    else:
        print((n-p-1)//2)

#wrong approach
        