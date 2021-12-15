n=int(input())
res=0
for j in range(n):
    i=input()
    if i=="Tetrahedron":
        res+=4
    elif i=="Cube":
        res+=6
    elif i=="Octahedron":
        res+=8
    elif i=="Dodecahedron":
        res+=12
    elif i=="Icosahedron":
        res+=20
print(res)