n=5
for i in range(n):
    str = "*"*(i+1)
    print(str)
print("\n")
for i in range(n):
    str = " "*(n-i) + "*"*(i+1)
    print(str)
print("\n")
for i in range(n,-1,-1):
    str = "*"*(i)
    print(str)
print("\n")
for i in range(n,-1,-1):
    str = " "*(n-i) + "*"*(i)
    print(str)
print("\n")
