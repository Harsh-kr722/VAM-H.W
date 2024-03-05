a=0 
b=1
print("Enter upto how many digits series should be printed:")
n=int(input())
while n<=0:
    print("Enter non zero positive integer.")
    n=int(input())
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b,end=" ")
    for x in range(1,n-1,1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    print("\n")    