number=int(input())
lists=[]
for i in range(number):
    k=input()
    lists.append(k)
count=0
for numbes in lists:
    if len(set(numbes))==len(numbes):
        count+=1

print(count)

