n=int(input())
res=0
res+=n//100
n=n%100
res+=n//20
n=n%20
res+=n//10
n=n%10
res+=n//5
n=n%5
if n==1:
    res+=1
else:
    res+=n//1
    n=n%1
print(res)
