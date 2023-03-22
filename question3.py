numroom=int(input())
R1,R2=list(map(int,input().split()))
calam=int(input())
days=[]
for i in range(1,32):
    days.append(i)
year=1
people=0
for i in range(len(days)):
    pe=(6-1)**2+abs(days[i]-15)
    print(pe-1,days[i])
    people+=pe-1
print(people)


#unsolved

    

    

