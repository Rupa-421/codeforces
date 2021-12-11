n=int(input())
l=list(map(int,input().split()))
count=1
maxcount=1
for i in range(1,len(l)):
    if l[i-1]<=l[i]:
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=1
if count>maxcount:
    maxcount=count
print(maxcount)