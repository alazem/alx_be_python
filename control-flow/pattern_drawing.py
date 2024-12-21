size = int(input("Enter the size of the pattern: "))
n=1
while n<=size:
    for i in range(1,size+1):
        print("*",end="")
    print()
    n+=1