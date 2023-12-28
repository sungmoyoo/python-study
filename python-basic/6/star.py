# 1)

for i in range(3):
    for j in range(3):
        print("*",end = " ")
    print("")

print("\n")
# 2)

for i in range(3):
    print("*"*(i+1))
    
    for j in range(3):
        print("", end="")

print("\n")

# 3)

for i in range(3,0,-1):
    print("*"*i)
    for j in range(3):
        print("",end="")

print("\n")

# 4)
for i in range(3):
    for j in range(2-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print("")

print("\n")


    
