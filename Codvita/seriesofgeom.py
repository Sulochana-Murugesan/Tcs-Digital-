geter=int(input())
list=[]
for i in range(abs(geter//2)+1):
    list.append(2**i)
    list.append(3**i)
print(list)
print(list[geter-1])


