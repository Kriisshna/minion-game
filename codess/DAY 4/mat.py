n=int(input())
a=[]

for r in range(n):
    b=[]
    for c in range(n):
        x=int(input())
        b.append(x)
    a.append(b)
print(a)

print("diagonal:")
for r in range(n):
    for c in range(n):
        if r==c:
            print(a[r][c],end=' ')
    print(" ")

print("not diagonal:")
for r in range(n):
    for c in range(n):
        if r!=c:
            print(a[r][c],end=' ')
    print(" ")

print("lower diagonal:")
for r in range(n):
    for c in range(n):
        if r>c:
            print(a[r][c],end=' ')
    print(" ")
    
print("upper diagonal:")
for r in range(n):
    for c in range(n):
        if r<c:
            print(a[r][c],end=' ')
            