n=int(input())
s=input()
s=s.lower()
s=list(set(list(s)))
s.sort()
s=''.join(s)
if s=="abcdefghijklmnopqrstuvwxyz":
    print("YES")
else:
    print("NO")