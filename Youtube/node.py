lev=int(input())
profit=int(input())
percent=int(input())

for i in range(lev-1):
    profit=round(profit*percent/100)

print(profit)