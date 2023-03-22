k=int(input())
dir="R"
val=10
x,y=0,0
for i in range(k):
    if dir=="R": 
        x+=val
        dir="U"
        val+=10
    elif dir=="U":
        y+=val
        dir="L"
        val+=10
    elif dir=="L":
        x-=val
        y=y
        dir="D"
        val+=10
    elif dir=="D":
        y=y-val
        dir="k"
        val+=10
    elif dir=="k":
        x=x+val
        dir="R"
        val+=10
print(x,y)

