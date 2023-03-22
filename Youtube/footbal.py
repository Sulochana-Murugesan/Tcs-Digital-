n=int(input())
tot=[]
for i in range(n):
    k=list(map(str,input().split()))
    tot.append(k)


d={}
for i in tot:
    team1=i[0]
    team2=i[1]
    if i[2]>i[4]:
        if team1 not in d:
            d[team1]=3
        else:
            d[team1]+=3
    elif i[2]==i[4]:
        if team1 not in d:
            d[team1]=1
        else:
            d[team1]+=1
        if team2 not in d:
            d[team2]=1
        else:
            d[team2]+=1
    elif i[2]<i[4]:
        if team2 not in d:
            d[team2]=3
        else:
            d[team2]+=3
    
p={}
for key ,values in d.items():
    p[values]=key

max=max(d.values())
print(p[max],max)

    
