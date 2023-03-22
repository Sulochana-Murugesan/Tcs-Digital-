def prime_number(low,up):
    primelist=[]
    if low>2:
        for i in range(low,up+1):
            prime=True
            for k in range(2,int(i**0.5)+1):
                if i%k==0:
                    prime=False
            if prime:
                primelist.append(i)
    return primelist
def prime_pair():
    count=0
    lists=prime_number(int(input()),int(input()))
    for i in range(len(lists)):
        for j in range(i+1,len(lists)):
            if lists[j]-lists[i]==6:
                count+=1
                print(lists[i],lists[j])
    return count

print(prime_pair())





