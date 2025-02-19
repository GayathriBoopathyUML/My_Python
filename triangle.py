n=5
for i in range(n):
    for j in range(n, -1,-1):
        if ((j-i>0)):
            print(" ", end="")
        else:
            print("*", end="")
    print("",end="\n")

print("\n")
n=5
for i in range(n):
    for j in range(n):
        if ((i-j>0)):
            print(" ", end="")
        else:
            print("*", end="")
    print("",end="\n")


print("\n")
for i in range(5):
    for j in range(5):
        if (j-i>=0):
            print("*", end="")
    print("",end="\n")

print("\n")
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("",end="\n")