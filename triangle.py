x=int(input("enter rows: "))

for x in range(x):
    for y in range(4,x-1,-1):
        print(" ",end="")
    for y in range(x):
        print("*",end="")
    print()