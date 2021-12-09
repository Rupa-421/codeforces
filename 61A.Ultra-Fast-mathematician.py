a=input()
b=input()
c=int(a,2)
b=int(b,2)
res=bin(c^b)[2::]
print((len(a)-len(res))*'0'+res)