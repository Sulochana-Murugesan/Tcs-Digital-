
n=input()
words=n.split()
lid=[]
for i in words:
    if "9" in i:
        continue
    else:
        lid.append(i)
for i in lid:
    if i.isdigit():
        print(i)
        
#another way to solve it
import re
def ref(listy):
    k= re.findall('\d+',listy)
    for i in k:
        d=str(i)
        if "9" in d:
            continue
        else:
            print(d)

   

(ref(n))