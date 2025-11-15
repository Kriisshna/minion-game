n=int(input())
m=int(input())
mat=[]

for r in range(n):
    b=[]
    for c in range(m):
        x=int(input())
        b.append(x)
    mat.append(b)

for r in mat:
    print(r)
print()

transpose=[]

for r in range(n):
    b=[]
    for c in range(m):
        b.append(0)
    transpose.append(b)

for r in range(len(mat)):
    for c in range(len(mat[0])):
        
        transpose[r][c]=mat[c][r]
# for r in transpose:
#     print(r)
# print()
for r in range(len(mat)):
    transpose[r]=transpose[r][::-1]

for r in transpose:
    print(r)
print()
