print("Enter a no")
n=int(input())
if n<=0:
    print(n,"is not a prime number.")  
else:    
    count=0
    for i in range(2,int(n/2),1):
        if n%i==0:
            count+=1
    if count==0:
        print(n,"is a prime number.")
    else:
        print(n,"is not a prime number.")            