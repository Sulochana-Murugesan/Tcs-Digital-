n=input()
if int(n)<1000000:
    for i in n:
        print(9-int(i),end="")
else:
    print("Wrong Input")
