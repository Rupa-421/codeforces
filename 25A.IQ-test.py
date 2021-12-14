n=int(input())
l=list(map(int,input().split()))
c=0
b=0
x=0
y=0
for i in range(len(l)):
    if l[i]%2==0:
        c+=1
        x=i
    else:
        b+=1
        y=i
if(c==1):
    print(x+1)
if(b==1):
    print(y+1)