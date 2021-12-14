t=int(input())
for i in range(t):
    n,g=map(int,input().split())
    rem=n%g
    if rem==0:
        print(0)
    else:
        print(g-rem)