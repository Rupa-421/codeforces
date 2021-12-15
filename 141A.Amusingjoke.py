a=input()
b=input()
a=a+b
a=list(a)
a.sort()
a=''.join(a)
c=input()
c=list(c)
c.sort()
c=''.join(c)
if a==c:
    print("YES")
else:
    print("NO")