s=input()
if len(s)==1 or s.isupper() or (s[0].islower() and s[1::].isupper()):
    for i in range(len(s)):
        if s[i].isupper():
            print(s[i].lower(),end="")
        else:
            print(s[i].upper(),end="")
else:
    print(s)