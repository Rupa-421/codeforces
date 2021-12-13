n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x=x[1::]
y=y[1::]
x=list(set(x+y))
if sum(x)!=(n*(n+1)//2):
    print("Oh, my keyboard!")
else:
    print("I become the guy.")