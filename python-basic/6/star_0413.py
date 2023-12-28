# 5)
for i in range(4):
    for j in range(i):
        print(" ",end="")
    for j in range(6,1+i*2,-1):
        print("*",end="")

    print("")
