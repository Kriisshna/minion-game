a=input("enter the desired symbol")
n=int(input("enter the range"))
for i in range(0,n):
    for j in range(0,n):
        print(a, end='')
    print()
# print()
for i in range(0,n+1):
    for j in range(0,i):

        print(a, end='')
    
    print()

for i in range(0,n):
   
    for j in range(0,n-i):   
        print(" ",end='')
    for j in range(i):
        print(a, end='')
    print()

for i in range(0,n):
   
    for j in range(i,n):   
        print(" ",end='')
    for j in range(i):
        print(a, end='')
    for j in range(i+1):
        print(a,end='')
    print()

for i in range(0,n):
    for j in range(i):   
        print(" ",end='')
    for j in range(0,n-i):
        print(a, end='')
    
    print()