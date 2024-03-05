print("enter a string.")
s=str(input())
d={}
for x in s:
    if x!=' ':
        if x in d:
            d[x]+=1
        else:
            d[x]=1
k=d.keys()            
for x in k:
    print(x,"occurs",d[x],"times")            
v=list(d.values())
print(max(v))
for x in d:
    if max(v)==d[x]:
        print(x,"occurs the most amount of times")


