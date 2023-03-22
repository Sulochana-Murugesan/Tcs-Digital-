v=input()
odd=0
even=0
for i in range(0,len(v),2):
    odd+=int(v[i])
for j in range(1,len(v),2):
    even+=int(v[j])
print(abs(odd-even))