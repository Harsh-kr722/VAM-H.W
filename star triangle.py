print("Enter no. of rows needed in triangle:")
n=int(input())
for x in range(0,n):
    for y in range(x,n-1):
        print(" ",end="")
    if x==0:
        print("*",end="")
    elif x==n-1:
        for z in range(0,n+(n-1)):
            print("*",end="")        
    else:
        for w in range(0,x+x+1):
            print("*",end="") 
    print("\n")         

