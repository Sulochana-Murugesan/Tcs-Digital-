def repdig(array):
    count=0
    for numbers in array:
        if len(set(str(numbers)))==len(str(numbers)):
            count+=1
    return count
n1=int(input())
n2=int(input())   
a=[i for i in range(n1,n2+1)]
print(repdig(a))
  