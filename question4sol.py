
n = int(input())
p = int(input())
print(p//2)
print(n//2)
print(n//2-p//2)
print( min(p//2, n//2 - p//2))

#lets discuss:
#total number of books is n
#then i have to move to the page called p:
#so that p//2 will be the pages to be truned from the firstpage:
#and n//2 wil be total number of papers in the book:
#from subracting n//2 and p//2 will give the numbers of pages to be turned from backside:
#by printing the minimum of it will produce an output