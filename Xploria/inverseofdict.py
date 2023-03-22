n=int(input())
oldd={}
newd={}
for i in range(n):
    key=input("Enter Key:")
    value=input("Enter value:")
    oldd[key]=value
    newd[value]=key
print(oldd)
print(newd)

def change(d:dict):
    new={}
    for key,values in d.items():
        new[values]=key
    return new

print(change(oldd))

