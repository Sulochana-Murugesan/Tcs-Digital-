n_totaldays=int(input())
m_oblications=int(input())
k_cance=int(input())
mrange=[1]
for i in range(m_oblications):
    mrange.append(int(input()))

sotrang=sorted(mrange)

lowers=0
if k_cance>0:
    for i in range(len(sotrang)-k_cance):
        current=sotrang[i]
        next=sotrang[i+k_cance]
        counter=abs(current-next)+1
        if counter>lowers:
            lowers=counter
    print(lowers)
else:
    print(sotrang[1])



    
#3
#1 6 8 11 15

#1 2 3 6 7 9