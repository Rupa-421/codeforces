n=int(input())
homes=[]
guest=[]
for i in range(n):
    ho,gu=map(int,input().split())
    homes.append(ho)
    guest.append(gu)
res=0
for i in range(n):
    for j in range(n):
        if homes[i]==guest[j]:
            res+=1
print(res)