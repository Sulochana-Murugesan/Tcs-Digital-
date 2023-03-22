def numbersplit(number):
    sum=0
    s=str(number)
    for i in s:
        sum+=int(i)
    return sum

def check(bd):
    k=numbersplit(bd)
    while k>9:
        k=numbersplit(k)
    return k

k=int(input())
pre=(check(k))
print(pre)

if pre==1:
    print("UNO")
else:
    print("Not")
