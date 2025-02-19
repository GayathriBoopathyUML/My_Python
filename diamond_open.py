n=7
n = n if n%2!=0 else n+1
for i in range(n):
    for j in range(n):
        x=n//2
        if ((j+min(i,n-1-i)>(x) and j-min(i,n-1-i)<(x))):
            print(" ", end="")
        else:
            print("*", end="")
    print("",end="\n")
    