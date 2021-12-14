l=input()
l=l[1:-1:]
j=l.split(',')
if not j[0]:
    print(0)
else:
    j[0]=" "+j[0]
    print(len(list(set(j))))