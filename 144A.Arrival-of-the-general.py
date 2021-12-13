n=int(input())
l=list(map(int,input().split()))
res=0
largeindex=l.index(max(l))
while largeindex!=0:
    res+=1
    l[largeindex],l[largeindex-1]=l[largeindex-1],l[largeindex]
    largeindex-=1
p=l[::-1]
smallindex=len(l)-p.index(min(p))-1
while smallindex!=len(l)-1:
    res+=1
    l[smallindex],l[smallindex+1]=l[smallindex+1],l[smallindex]
    smallindex+=1
print(res)